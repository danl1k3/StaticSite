import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_case(self):
        node = HTMLNode()
        node2 = HTMLNode()
        nodes = [node, node2]
        h_node = HTMLNode(
                "p", 
                "hello everyone", 
                nodes, 
                {"<p>": "addada", "href": "https"}
        )
        h_node2 = HTMLNode(
                "p", 
                "hello everyone", 
                nodes, 
                {"<p>": "addada", "href": "https"}
        )
        self.assertEqual(repr(h_node), repr(h_node2))

    def test_case2(self):
        node = HTMLNode()
        node2 = HTMLNode()
        nodes = [node, node2]
        h_node = HTMLNode(
                "a", 
                "hello everyone", 
                nodes, 
                {"<a>": "addada", "href": "https"}
        )
        h_node2 = HTMLNode(
                "p", 
                "hello everyone", 
                nodes, 
                {"<p>": "addada", "href": "https"}
        )
        self.assertNotEqual(repr(h_node), repr(h_node2))

    def test_case3(self):
        node = HTMLNode()
        node2 = HTMLNode()
        nodes = [node, node2]
        h_node = HTMLNode(
                "a", 
                "hello everyone", 
                nodes, 
                {"<p>": "addada", "href": "https"}
        )
        h_node2 = HTMLNode(
                "a", 
                "hello everyone", 
                nodes, 
                {"<a>": "addada", "href": "https"}
        )
        self.assertNotEqual(h_node.props_to_html(), h_node2.props_to_html())

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()
