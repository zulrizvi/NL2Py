def generate_code(intent, args):
    if intent == "assign":
        return f"{args['var']} = {args['val']}"
    elif intent == "print":
        if args['var']:
            return f"print({args['var']})"
    elif intent == "input":
        return f"{args['var']} = input()"
    elif intent == "loop":
        return f"for i in range({args['start']}, {args['end']}):\n    print(i)"
    elif intent == "condition":
        return f"if {args['var']} == {args['val']}:\n    print('Condition met')"
    return "# Unsupported intent"
