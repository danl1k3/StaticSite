import re

def extract_title(markdown):
    match = re.search(r"^#(?!#)(.*)$", markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    else:
        raise Exception("No h1 header!")

if __name__ == "__main__":
    print(extract_title("# hello"))
