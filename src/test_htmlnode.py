import unittest

from htmlnode import HTMLNode


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
