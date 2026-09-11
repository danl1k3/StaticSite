from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    cont = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, cont)
        case TextType.BOLD:
            return LeafNode("b", cont)
        case TextType.ITALIC:
            return LeafNode("i", cont)
        case TextType.CODE:
            return LeafNode("code", cont)
        case TextType.LINK:
            return LeafNode("a", cont, {"href": f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
        case _:
            raise Exception("Not supported type of text")

