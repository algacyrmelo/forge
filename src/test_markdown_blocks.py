import unittest

from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        blocks = [
            "# This is an h1",
            "## This is an h2",
            "### This is an h3",
            "#### This is an h4",
            "##### This is an h5",
            "###### This is an h6",
        ]
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.HEADING,
            )

    def test_block_to_block_type_code(self):
        block = "```bash\necho 'hello world')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.CODE,
        )

    def test_block_to_block_type_quote(self):
        block = ">block\n> quote"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.QUOTE,
        )

    def test_block_to_block_type_ulist(self):
        block = "- First item\n- Second item\n- Third item"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.ULIST,
        )

    def test_block_to_block_type_olist(self):
        block = "1. First item\n2. Second item\n3. Third item"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.OLIST,
        )


if __name__ == "__main__":
    unittest.main()
