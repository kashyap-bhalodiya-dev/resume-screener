import re

def extract_name(text):

    # Clean text (remove extra spaces)
    text = text.replace("\n", " ")

    # Find ALL CAPS names (like KASHYAP BHALODIYA)
    matches = re.findall(r'\b[A-Z]{3,}\s[A-Z]{3,}\b', text)

    if matches:
        return matches[0].title()

    return "Unknown"