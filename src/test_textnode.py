import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("I need to test that this works!!!", TextType.LINK, "https://www.marcoevelle.games")
        node2 = TextNode("I need to test that this works!!!", TextType.LINK, "https://www.marcoevelle.games")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("I need to test that this works!!!", TextType.LINK, None)
        node2 = TextNode("I need to test that this works!!!", TextType.LINK)
        self.assertEqual(node, node2)

    def test_not_eq4(self):
        node = TextNode("I need to test that this works!!!", TextType.LINK)
        node2 = TextNode("Why did this BREAK!!!", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Let's change it up some", TextType.LINK, "https://www.marcoevelle.games")
        text = "TextNode(Let's change it up some, link, https://www.marcoevelle.games)"
        self.assertEqual(text, repr(node))

if __name__ == "__main__":
    unittest.main()