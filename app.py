import streamlit as st
import io
import contextlib

from app.predict import detect_intent_nltk
from app.extract_args_nltk import extract_args_nltk
from app.code_generator import generate_code

st.title("🐒 Natural Language to Python Code")

# Use session_state to persist full_code between button clicks
if "full_code" not in st.session_state:
    st.session_state.full_code = ""

user_input = st.text_area("Enter instruction in natural language")

if st.button("Generate Code"):
    
    if user_input.strip():
        lines = [line.strip() for line in user_input.splitlines() if line.strip()]
        full_code = ""
        for line in lines:
            intent = detect_intent_nltk(line)
            args = extract_args_nltk(line, intent)
            code = generate_code(intent, args)
            full_code += code.strip() + "\n"
        
        st.session_state.full_code = full_code.strip()  # Save to session state
        # st.code(st.session_state.full_code, language="python")
    else:
        st.warning("Please enter at least one instruction.")

# Show the code if it's already generated
if st.session_state.full_code:
    # st.balloons()
    st.subheader("🧠 Generated Code:")
    st.code(st.session_state.full_code, language="python")

# Run the code
if st.session_state.full_code and st.button("▶️ Run Code"):
    output_buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec_globals = {}
            exec(st.session_state.full_code, exec_globals)

        st.success("✅ Code executed successfully!")

        output = output_buffer.getvalue()
        if output.strip():
            st.subheader("🖨️ Output:")
            st.text(output)
        else:
            st.info("⚠️ No output was printed.")

        st.subheader("🔍 Variables created:")
        for var, val in exec_globals.items():
            if not var.startswith("__"):
                st.write(f"**{var}** = {val}")

    except Exception as e:
        st.error(f"❌ Error while running code:\n\n{e}")

# Download button
st.download_button(
    label="📥 Download Code as .py",
    data=st.session_state.full_code,
    file_name="generated_code.py",
    mime="text/x-python"
)
