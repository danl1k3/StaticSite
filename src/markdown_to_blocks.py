

def markdown_to_blocks(markdown: str):
    raw_blocks = markdown.split("\n\n")
    stripped_blocks = map(str.strip, raw_blocks)
    non_empty_blocks = filter(None, stripped_blocks)
    return list(non_empty_blocks)
