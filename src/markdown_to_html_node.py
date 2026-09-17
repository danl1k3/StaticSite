from block_to_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def block_to_html_node(block_type: BlockType, block: str) -> ParentNode:
    match block_type:
        case BlockType.PARAGRAPH:
            lines = block.split("\n")
            paragraph_text = " ".join(lines)
            return ParentNode("p", text_to_children(paragraph_text))

        case BlockType.HEADING:
            header_level = len(block) - len(block.lstrip("#"))
            heading_text = block[header_level:].strip()
            return ParentNode(f"h{header_level}", text_to_children(heading_text))

        case BlockType.CODE:
            lines = block.split("\n")
            code_text = "\n".join(lines[1:-1]) + "\n"
            raw_node = TextNode(code_text, TextType.TEXT)
            code_node = ParentNode("code", [text_node_to_html_node(raw_node)])
            return ParentNode("pre", [code_node])
        
        case BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = [line.lstrip(">").strip() for line in lines]
            quote_text = " ".join(cleaned_lines)
            return ParentNode("blockquote", text_to_children(quote_text))

        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                item_text = line[2:]
                items.append(ParentNode("li", text_to_children(item_text)))
            return ParentNode("ul", items)

        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                item_text = line.split(". ", 1)[1]
                items.append(ParentNode("li", text_to_children(item_text)))
            return ParentNode("ol", items)

        case _:
            raise ValueError(f"Unknown block type: {block_type}")


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        node = block_to_html_node(block_type, block)
        children.append(node)

    return ParentNode("div", children)
