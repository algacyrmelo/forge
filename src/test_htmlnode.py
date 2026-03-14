import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_attr(self):
        node = HTMLNode("h1", "Hello, world!", None, {"class": "title"})
        self.assertEqual(
            node.props_to_html(),
            ' class="title"',
        )

    def test_props_to_html_multiple_attrs(self):
        node = HTMLNode(
            "a",
            "Python docs",
            None,
            {"href": "https://www.python.org", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.python.org" target="_blank"',
        )

    def test_props_to_html_none(self):
        node = HTMLNode("h1", "Hello, world!", None, None)
        self.assertEqual(
            node.props_to_html(),
            "",
        )

    def test_props_to_html_empty(self):
        node = HTMLNode("a", "Boot.dev", None, {})
        self.assertEqual(
            node.props_to_html(),
            "",
        )

    def test_values(self):
        node = HTMLNode(
            "a",
            "boot.dev",
            None,
            {"href": "https://www.boot.dev", "target": "_blank"},
        )
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "boot.dev")
        self.assertEqual(node.children, None)
        self.assertEqual(
            node.props,
            {"href": "https://www.boot.dev", "target": "_blank"}
        )

    def test_values_with_children(self):
        h1 = HTMLNode("h1", "Hello world")
        p = HTMLNode("p", "This is an HTMLNode")
        div = HTMLNode(
            "div",
            None,
            [h1, p],
            {"class": "container"}
        )
        self.assertEqual(div.tag, "div")
        self.assertEqual(div.value, None)
        self.assertEqual(div.children, [h1, p])
        self.assertEqual(div.props, {"class": "container"})

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!", None, {"class": "primary"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Hello, world!, children: None, {'class': 'primary'})",
        )

