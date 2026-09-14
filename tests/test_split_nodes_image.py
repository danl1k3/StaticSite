from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image
import unittest

class test_split_nodes_image(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_other_types(self):
        node = TextNode('code', TextType.CODE)
        node2 = TextNode("bold text", TextType.BOLD)
        node3 = TextNode("This is a ![image](https://...) and some text after **bold**", TextType.TEXT)
        new_nodes = split_nodes_image([node, node2, node3])
        self.assertListEqual(
            [
                TextNode('code', TextType.CODE),
                TextNode("bold text", TextType.BOLD),
                TextNode("This is a ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://..."),
                TextNode(" and some text after **bold**", TextType.TEXT) 
            ],
            new_nodes
        )

    def test_single_image_in_middle(self):
        node = TextNode(
            "Here is an ![alt](https://example.com/pic.png) in text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.TEXT),
                TextNode("alt", TextType.IMAGE, "https://example.com/pic.png"),
                TextNode(" in text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_start(self):
        node = TextNode(
            "![banner](https://example.com/banner.png) Welcome to my site",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("banner", TextType.IMAGE, "https://example.com/banner.png"),
                TextNode(" Welcome to my site", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_end(self):
        node = TextNode(
            "See the image below: ![footer](https://example.com/footer.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("See the image below: ", TextType.TEXT),
                TextNode("footer", TextType.IMAGE, "https://example.com/footer.png"),
            ],
            new_nodes,
        )

    def test_only_image(self):
        node = TextNode(
            "![solo](https://example.com/solo.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("solo", TextType.IMAGE, "https://example.com/solo.png"),
            ],
            new_nodes,
        )

    def test_adjacent_images(self):
        node = TextNode(
            "![first](https://example.com/1.png)![second](https://example.com/2.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://example.com/1.png"),
                TextNode("second", TextType.IMAGE, "https://example.com/2.png"),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode(
            "This is just plain text without any markdown images.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is just plain text without any markdown images.", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_non_text_type_node_preserved(self):
        nodes = [
            TextNode("![img](https://example.com/img.png)", TextType.TEXT),
            TextNode("already bold", TextType.BOLD),
            TextNode("code snippet", TextType.CODE),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("img", TextType.IMAGE, "https://example.com/img.png"),
                TextNode("already bold", TextType.BOLD),
                TextNode("code snippet", TextType.CODE),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()


