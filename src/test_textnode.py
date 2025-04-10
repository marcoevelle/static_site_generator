import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """Testing TextNode value assignment with optional left out"""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        """Testing TextNode all value assignment"""
        node = TextNode("I need to test that this works!!!", TextType.LINK, "https://www.marcoevelle.games")
        node2 = TextNode("I need to test that this works!!!", TextType.LINK, "https://www.marcoevelle.games")
        self.assertEqual(node, node2)

    def test_eq3(self):
        """Testing TextNode value assignment with optional specified"""
        node = TextNode("I need to test that this works!!!", TextType.LINK, None)
        node2 = TextNode("I need to test that this works!!!", TextType.LINK)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        """Testing TextNode enum bold and italic are different"""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        """Testing TextNode enum text and code are different"""
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        """Testing TextNode enum link and image are different"""
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        """Testing TextNode printing"""
        node = TextNode("Let's change it up some", TextType.LINK, "https://www.marcoevelle.games")
        text = "TextNode(Let's change it up some, link, https://www.marcoevelle.games)"
        self.assertEqual(text, repr(node))
    
    def test_textnode_convert_text(self):
        """Testing TextNode to HTMLNode using text type"""
        node = TextNode("Testing text!", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Testing text!")

    def test_textnode_convert_bold(self):
        """Testing TextNode to HTMLNode using bold type"""
        node = TextNode("Testing text!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Testing text!")

    def test_textnode_convert_italic(self):
        """Testing TextNode to HTMLNode using italic type"""
        node = TextNode("Testing text!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Testing text!")

    def test_textnode_convert_code(self):
        """Testing TextNode to HTMLNode using code type"""
        node = TextNode("dangerous malware!!!", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "dangerous malware!!!")

    def test_textnode_convert_link(self):
        """Testing TextNode to HTMLNode using link type"""
        node = TextNode("Click me!", TextType.LINK, "https://www.marcoevelle.games")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me!")
        self.assertEqual(html_node.props, {"href": "https://www.marcoevelle.games"})

    def test_textnode_convert_link(self):
        """Testing TextNode to HTMLNode using image type"""
        node = TextNode("Puppies!", TextType.IMAGE, "https://dogs.marcoevelle.games")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://dogs.marcoevelle.games", "alt": "Puppies!"})

    def test_textnode_convert_invalid(self):
        """Testing TextNode to HTMLNode using an unknown type"""
        with self.assertRaises(ValueError):
            node = TextNode("Puppies!", "texttype_CSS", "https://dogs.marcoevelle.games")
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()