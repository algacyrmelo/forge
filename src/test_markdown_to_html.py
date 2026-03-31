import unittest

from markdown_to_html import extract_title, markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# **Heading** level 1

## _Heading_ level 2

### `Heading` level 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1><b>Heading</b> level 1</h1><h2><i>Heading</i> level 2</h2><h3><code>Heading</code> level 3</h3></div>",
        )

    def test_quotes(self):
        md = """
> This is a quote
> with inline **bold**, _italic_ and `code` text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with inline <b>bold</b>, <i>italic</i> and <code>code</code> text</blockquote></div>",
        )

    def test_ulists(self):
        md = """
- **Bold** text
- _Italic_ text
- Inline `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li><b>Bold</b> text</li><li><i>Italic</i> text</li><li>Inline <code>code</code></li></ul></div>",
        )

    def test_olists(self):
        md = """
1. **Bold** text
2. _Italic_ text
3. Inline `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li><b>Bold</b> text</li><li><i>Italic</i> text</li><li>Inline <code>code</code></li></ol></div>",
        )

    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.
"""
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")


if __name__ == "__main__":
    unittest.main()
