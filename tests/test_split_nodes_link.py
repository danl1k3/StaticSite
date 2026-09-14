import unittest
from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links_multiple(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_single_link_in_middle(self):
        node = TextNode(
            "Click [here](https://boot.dev) to learn more",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Click ", TextType.TEXT),
                TextNode("here", TextType.LINK, "https://boot.dev"),
                TextNode(" to learn more", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_start(self):
        node = TextNode(
            "[Homepage](https://boot.dev) contains all resources",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Homepage", TextType.LINK, "https://boot.dev"),
                TextNode(" contains all resources", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_end(self):
        node = TextNode(
            "Visit our site at [boot.dev](https://boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Visit our site at ", TextType.TEXT),
                TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_only_link(self):
        node = TextNode(
            "[solo link](https://boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("solo link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_adjacent_links(self):
        node = TextNode(
            "[first](https://one.com)[second](https://two.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.LINK, "https://one.com"),
                TextNode("second", TextType.LINK, "https://two.com"),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode(
            "This is just plain text without any markdown links.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is just plain text without any markdown links.", TextType.TEXT),
            ],
            new_nodes,
        )



    def test_non_text_type_node_preserved(self):
        nodes = [
            TextNode("[link](https://boot.dev)", TextType.TEXT),
            TextNode("already italic", TextType.ITALIC),
            TextNode("code block", TextType.CODE),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode("already italic", TextType.ITALIC),
                TextNode("code block", TextType.CODE),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
