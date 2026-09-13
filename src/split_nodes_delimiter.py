from textnode import TextNode, TextType


def split_nodes_delimiter(
        old_nodes: list[TextNode], 
        delimiter: str, 
        text_type: TextType
        ) -> list[TextNode]:
        delimited_text = []
        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                delimited_text.append(old_node)
                continue

            splitted_node_text = old_node.text.split(delimiter)
            if len(splitted_node_text) % 2 == 0:
                raise Exception("No matching delimiter!")
            nodes_batch = []
            for i, split in enumerate(splitted_node_text):
                if not split:
                    continue
                if i % 2 == 0:
                    nodes_batch.append(TextNode(split, TextType.TEXT))
                else:
                    nodes_batch.append(TextNode(split, text_type))
            delimited_text.extend(nodes_batch)

        return delimited_text
            

           


