import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Hello everyone", TextType.LINK, 'link...')
        self.assertEqual(repr(node), "TextNode(Hello everyone, link, link...)")
    
    def test_noteq(self):
        node = TextNode("Simple text", TextType.ITALIC)
        node2 = TextNode("Complex text..", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq3(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_noteq4(self):
        node = TextNode("This is a text node", TextType.LINK, 'https:/')
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
