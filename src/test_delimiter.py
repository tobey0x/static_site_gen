import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_text_split_with_code_delimiter(self):
        # Test splitting with ` for inline code
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_bold_split(self):
        # Test splitting with ** for bold text
        node = TextNode("This is text with a **bold phrase** in the middle", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_split(self):
        # Test splitting with * for italic text
        node = TextNode("This is *italic text* in the sentence", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in the sentence", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiter_found(self):
        # Test with no delimiter match
        node = TextNode("This is a text without special formatting", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter_raises_error(self):
        # Test unmatched delimiter raises an error
        node = TextNode("This text has an unmatched `delimiter", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "Unmatched delimiter found")

    def test_multiple_splits(self):
        # Test multiple splits for different delimiters in the same text
        node = TextNode("This is **bold** and *italic* text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

# Run the tests
if __name__ == '__main__':
    unittest.main()
