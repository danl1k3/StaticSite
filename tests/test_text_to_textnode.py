import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class test_text_to_textnode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )
    def test_plain_text_only(self):
        text = "Just simple plain text without any formatting or markdown tokens."
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Just simple plain text without any formatting or markdown tokens.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_empty_string(self):
        text = ""
        new_nodes = text_to_textnodes(text)
        self.assertListEqual([], new_nodes)

    def test_single_bold(self):
        text = "**bold only**"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("bold only", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_single_italic(self):
        text = "_italic only_"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("italic only", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_single_code(self):
        text = "`code only`"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("code only", TextType.CODE),
            ],
            new_nodes,
        )

    def test_multiple_same_delimiter(self):
        text = "**first bold** normal text **second bold**"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("first bold", TextType.BOLD),
                TextNode(" normal text ", TextType.TEXT),
                TextNode("second bold", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_adjacent_different_types(self):
        text = "**bold**_italic_`code`"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code", TextType.CODE),
            ],
            new_nodes,
        )

    def test_image_and_link_together(self):
        text = "![logo](https://boot.dev/logo.png)[boot.dev](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("logo", TextType.IMAGE, "https://boot.dev/logo.png"),
                TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

    def test_image_syntax_not_parsed_as_link(self):
        text = "Here is an ![image alt](https://example.com/pic.png) not a link"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.TEXT),
                TextNode("image alt", TextType.IMAGE, "https://example.com/pic.png"),
                TextNode(" not a link", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
