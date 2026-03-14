import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
            "p",
            "Hello, world!",
            None,
            {"class": "primary"},
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "primary"})

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!", None, {"class": "primary"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Hello, world!, children: None, {'class': 'primary'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "boot.dev",
            {"href": "https://www.boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boot.dev" target="_blank">boot.dev</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("div", None)
        self.assertRaises(ValueError, node.to_html)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

    def test_to_html_many_children(self):
        parent_node = ParentNode(
            "div",
            [
                LeafNode("h1", "child"),
                LeafNode(None, "child2"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><h1>child</h1>child2</div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_empty_children(self):
        parent_node = ParentNode("div", {})
        self.assertEqual(parent_node.to_html(), "<div></div>")
