import nltk
from nltk import pos_tag, word_tokenize

# Ensure NLTK data is available
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_args_nltk(text, intent):
    tokens = word_tokenize(text.lower())
    tagged = pos_tag(tokens)
    args = {}

    if intent == "assign":
        # Look for number (value) and noun (variable)
        for word, tag in tagged:
            if tag == "CD" and "val" not in args:
                args["val"] = word
            if tag.startswith("NN") and "var" not in args:
                args["var"] = word

    elif intent == "print":
        for word, tag in tagged:
            if tag.startswith("NN") or tag.startswith("CD"):
                args["var"] = word

    elif intent == "input":
        for word, tag in tagged:
            if tag.startswith("NN"):
                args["var"] = word

    elif intent == "loop":
        numbers = [word for word, tag in tagged if tag == "CD"]
        if len(numbers) >= 2:
            args["start"], args["end"] = numbers[:2]

    elif intent == "condition":
        for word, tag in tagged:
            if tag.startswith("NN") and "var" not in args:
                args["var"] = word
            if tag == "CD" and "val" not in args:
                args["val"] = word

    return args
