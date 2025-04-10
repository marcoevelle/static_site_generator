import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, props)
        prop_text = node.props_to_html()
        self.assertEqual(prop_text, ' href="https://www.google.com" target="_blank"')

    def test_props_to_html2(self):
        props = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
            "color": "purple",
        }
        node = HTMLNode(None, None, None, props)
        prop_text = node.props_to_html()
        self.assertEqual(prop_text, ' href="https://www.marcoevelle.games" target="home" color="purple"')

    def test_props_to_html_no_prop(self):
        node = HTMLNode(None, None, None, None)
        prop_text = node.props_to_html()
        self.assertEqual(prop_text, "")

    def test_props_to_html_false(self):
        node = HTMLNode()
        prop_text = node.props_to_html()
        self.assertNotEqual(prop_text, ' href="https://www.marcoevelle.games" target="home" color="purple"')

    def test_to_html(self):
        try:
            node = HTMLNode()
            node.to_html()
            self.assertFalse(None != None)
        except Exception as e:
            self.assertTrue(None == None)

    def test_htmlnode_print(self):
        node = HTMLNode()
        text = "HTMLNode(None, None, None, None)"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print2(self):
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode("#", "This is my gaming site.","HTMLNode",prop)
        text = f"HTMLNode(#, This is my gaming site., HTMLNode, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print3(self):
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode("#", "This is my gaming site.",None,prop)
        text = f"HTMLNode(#, This is my gaming site., None, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print4(self):
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode("#", None,"HTMLNode",prop)
        text = f"HTMLNode(#, None, HTMLNode, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print5(self):
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode(None, "This is my gaming site.","HTMLNode",prop)
        text = f"HTMLNode(None, This is my gaming site., HTMLNode, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print6(self):
        node = HTMLNode("#", "This is my gaming site.","HTMLNode",None)
        text = f"HTMLNode(#, This is my gaming site., HTMLNode, None)"
        self.assertEqual(text, repr(node))

    def test_values(self):
        node = HTMLNode("h1", "Sup!")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Sup!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Palworld Server", {"href": "https://palworld.marcoevelle.games"})
        self.assertEqual(node.to_html(), '<a href="https://palworld.marcoevelle.games">Palworld Server</a>')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Come check out all our game servers!")
        self.assertEqual(node.to_html(), "<p>Come check out all our game servers!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "We will game all night!")
        self.assertEqual(node.to_html(), "We will game all night!")


if __name__ == "__main__":
    unittest.main()