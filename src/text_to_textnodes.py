from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    node_with_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    node_with_italic = split_nodes_delimiter(node_with_bold, "_", TextType.ITALIC)
    node_with_code = split_nodes_delimiter(node_with_italic, "`", TextType.CODE)
    node_with_images = split_nodes_image(node_with_code)
    new_nodes = split_nodes_link(node_with_images)

    return new_nodes

