import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestParentNode(unittest.TestCase):

    def test_parentnode_with_nested_children(self):
        leaf_1 = LeafNode(value="Nested Content", tag="em")
        nested_parent = ParentNode(tag="section", children=[leaf_1])
        main_parent = ParentNode(tag="div", children=[nested_parent])

        expected_html = "<div><section><em>Nested Content</em></section></div>"
        self.assertEqual(main_parent.to_html(), expected_html)

        

if __name__ == "__main__":
    unittest.main()
