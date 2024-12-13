import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_split(self):
        markdown = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        )
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_lines(self):
        markdown = (
            "# Heading\n\n\n"
            "Paragraph with text.\n\n"
            "* List item 1\n* List item 2\n\n\n"
        )
        expected = [
            "# Heading",
            "Paragraph with text.",
            "* List item 1\n* List item 2"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_only_whitespace(self):
        markdown = "   \n\n\n  "
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_single_block(self):
        markdown = "This is just one block of text."
        expected = ["This is just one block of text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == "__main__":
    unittest.main()
