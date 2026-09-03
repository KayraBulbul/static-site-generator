import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://kayrabulbul.dev", "target": "_blank"})
        self.assertEqual(
            ' href="https://kayrabulbul.dev" target="_blank"', node.props_to_html()
        )

    def test_props_to_html_eq(self):
        node = HTMLNode(props={"href": "https://kayrabulbul.dev", "target": "_blank"})
        node2 = HTMLNode(props={"href": "https://kayrabulbul.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
