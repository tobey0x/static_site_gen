import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode("<a>gerrard</a>", "10",["<a>", "ad"], {
    "href": "https://www.google.com", 
    "target": "_blank",
})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(leaf.tag, "p")
        

if __name__ == "__main__":
    unittest.main()
