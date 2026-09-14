from textnode import TextNode, TextType
from extracter_tools import extract_markdown_links

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if not old_node.text_type == TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        current_text = old_node.text
        pairs = extract_markdown_links(current_text)

        if not pairs:
            new_nodes.append(old_node)
            continue

        for anchor, link in pairs:
            sections: list[str] = current_text.split(f"[{anchor}]({link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, link))
            current_text = sections[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


