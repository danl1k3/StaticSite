import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_case1(self):
        node = LeafNode("p", "Yeeea")
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertEqual(
            node.props,
            None
        )
        self.assertEqual(
            node.value,
            "Yeeea"
        )
    
    def test_rerp(self):
        node = LeafNode("a", "Click!", {"bootdev": "https://"})
        node2 = LeafNode("b", "need you attention pls")

        self.assertEqual(
            repr(node),
            "LeafNode(a, Click!, {'bootdev': 'https://'})"
        )

        self.assertEqual(
            repr(node2),
            "LeafNode(b, need you attention pls, None)"
            
        )
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_any(self):
        node = LeafNode("a", "It is boot dev!", {"href": "https://bootdev.com"})
        self.assertEqual(node.to_html(), '<a href="https://bootdev.com">It is boot dev!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
