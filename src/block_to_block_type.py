from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def is_ordered_list(text: str) -> bool:
    text_lines = text.split("\n")
    for i, line in enumerate(text_lines, start=1):
        prefix = f"{i}. "
        if not line.startswith(prefix) or len(line) <= len(prefix):
            return False
    return True


def block_to_block_type(text: str) -> BlockType:
    text = text.strip()
    if re.fullmatch(r"#{1,6} .+", text):
        return BlockType.HEADING
    elif re.fullmatch(r"```\n[\s\S]*\n```", text):
        return BlockType.CODE
    elif re.fullmatch(r"(>.*(\n|$))+", text):
        return BlockType.QUOTE
    elif re.fullmatch(r"(- .*(\n|$))+", text):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(text):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
