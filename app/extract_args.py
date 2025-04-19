import re
##re basedd arguments extaction
def extract_args_regex(text, intent):
    args={}
    if intent == "assign":
        match = re.search(r'(\w).*(\d+)', text)
        if match:
            args["var"], args["val"] = match.group(1), match.group(2)
    elif intent == "print":
        match = re.search(r'(\w+)', text)
        if match:
            args["var"] = match.group(1)
    elif intent == "input":
        match = re.search(r'(\w+)', text)
        if match:
            args["var"] = match.group(1)
    elif intent == "loop":
        nums = re.findall(r'\d+', text)
        if len(nums) >= 2:
            args["start"], args["end"] = nums[0], nums[1]
    elif intent == "condition":
        match = re.search(r'(\w+).*?(\d+)', text)
        if match:
            args["var"], args["val"] = match.group(1), match.group(2)
    return args