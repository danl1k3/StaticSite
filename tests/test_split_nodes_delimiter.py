from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class Test_split_nodes_delimiter(unittest.TestCase):
    def test_code_in_middle(self):
        node = TextNode("some `code text` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("some ", TextType.TEXT),
                TextNode("code text", TextType.CODE),
                TextNode(" here", TextType.TEXT)
            ]
        )

    def test_bold_in_middle(self):
        node = TextNode("normal **bold text** normal", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("normal ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" normal", TextType.TEXT),
            ],
        )

    def test_italic_in_middle(self):
        node = TextNode("normal *italic text* normal", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            result,
            [
                TextNode("normal ", TextType.TEXT),
                TextNode("italic text", TextType.ITALIC),
                TextNode(" normal", TextType.TEXT),
            ],
        )

    def test_bold_at_start(self):
        node = TextNode("**bold text** normal", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("bold text", TextType.BOLD),
                TextNode(" normal", TextType.TEXT),
            ],
        )

    def test_bold_at_end(self):
        node = TextNode("normal **bold text**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("normal ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
            ],
        )

    def test_whole_string_delimited(self):
        node = TextNode("**all bold**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("all bold", TextType.BOLD),
            ],
        )

    def test_no_delimiter_present(self):
        node = TextNode("plain text with no marks", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("plain text with no marks", TextType.TEXT),
            ],
        )

    def test_multiple_sections(self):
        node = TextNode("word `code1` middle `code2` end", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("word ", TextType.TEXT),
                TextNode("code1", TextType.CODE),
                TextNode(" middle ", TextType.TEXT),
                TextNode("code2", TextType.CODE),
                TextNode(" end", TextType.TEXT),
            ],
        )

    def test_non_text_node_passes_through(self):
        node = TextNode("already code", TextType.CODE)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("already code", TextType.CODE),
            ],
        )

    def test_multiple_input_nodes(self):
        node1 = TextNode("text with `code`", TextType.TEXT)
        node2 = TextNode("bold text", TextType.BOLD)
        node3 = TextNode("more `code` text", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("text with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode("bold text", TextType.BOLD),
                TextNode("more ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_empty_input_list(self):
        result = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(result, [])

    def test_unclosed_delimiter_raises(self):
        node = TextNode("broken `inline code with no closing mark", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_chained_delimiters(self):
        node = TextNode("start **bold** and *italic* end", TextType.TEXT)
        bold_split = split_nodes_delimiter([node], "**", TextType.BOLD)
        italic_split = split_nodes_delimiter(bold_split, "*", TextType.ITALIC)
        self.assertEqual(
            italic_split,
            [
                TextNode("start ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" end", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
