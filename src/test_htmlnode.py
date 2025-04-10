import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        """Testing HTMLNode Prop Only"""
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, props)
        prop_text = node.props_to_html()
        self.assertEqual(prop_text, ' href="https://www.google.com" target="_blank"')

    def test_props_to_html2(self):
        """Testing HTMLNode Prop Only test 2"""
        props = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
            "color": "purple",
        }
        node = HTMLNode(None, None, None, props)
        prop_text = node.props_to_html()
        self.assertEqual(prop_text, ' href="https://www.marcoevelle.games" target="home" color="purple"')

    def test_props_to_html_no_prop(self):
        """Testing HTMLNode No prop returns an empty string"""
        node = HTMLNode(None, None, None, None)
        prop_text = node.props_to_html()
        self.assertEqual(prop_text, "")

    def test_props_to_html_false(self):
        """Testing HTMLNode empty instance"""
        node = HTMLNode()
        prop_text = node.props_to_html()
        self.assertNotEqual(prop_text, ' href="https://www.marcoevelle.games" target="home" color="purple"')

    def test_to_html(self):
        """Testing HTMLNode to_html is not implemented"""
        with self.assertRaises(NotImplementedError):
            node = HTMLNode()
            node.to_html()

    def test_htmlnode_print(self):
        """Testing HTMLNode printing empty"""
        node = HTMLNode()
        text = "HTMLNode(None, None, None, None)"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print2(self):
        """Testing HTMLNode printing with values"""
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode("#", "This is my gaming site.","HTMLNode",prop)
        text = f"HTMLNode(#, This is my gaming site., HTMLNode, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print3(self):
        """Testing HTMLNode printing with empty children"""
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode("#", "This is my gaming site.",None,prop)
        text = f"HTMLNode(#, This is my gaming site., None, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print4(self):
        """Testing HTMLNode printing with empty value"""
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode("#", None,"HTMLNode",prop)
        text = f"HTMLNode(#, None, HTMLNode, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print5(self):
        """Testing HTMLNode printing with empty tag"""
        prop = {
            "href": "https://www.marcoevelle.games",
            "target": "home",
        }
        node = HTMLNode(None, "This is my gaming site.","HTMLNode",prop)
        text = f"HTMLNode(None, This is my gaming site., HTMLNode, {prop})"
        self.assertEqual(text, repr(node))

    def test_htmlnode_print6(self):
        """Testing HTMLNode printing with empty properties"""
        node = HTMLNode("#", "This is my gaming site.","HTMLNode",None)
        text = f"HTMLNode(#, This is my gaming site., HTMLNode, None)"
        self.assertEqual(text, repr(node))

    def test_values(self):
        """Testing HTMLNode value assignment"""
        node = HTMLNode("h1", "Sup!")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Sup!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_leaf_to_html_a(self):
        """Testing LeafNode to_html with properties"""
        node = LeafNode("a", "Palworld Server", {"href": "https://palworld.marcoevelle.games"})
        self.assertEqual(node.to_html(), '<a href="https://palworld.marcoevelle.games">Palworld Server</a>')

    def test_leaf_to_html_p(self):
        """Testing LeafNode to_html with no properties"""
        node = LeafNode("p", "Come check out all our game servers!")
        self.assertEqual(node.to_html(), "<p>Come check out all our game servers!</p>")

    def test_leaf_to_html_no_tag(self):
        """Testing LeafNode to_html with properties and no tag"""
        node = LeafNode(None, "We will game all night!")
        self.assertEqual(node.to_html(), "We will game all night!")

    def test_leaf_to_html_no_value(self):
        """Testing LeafNode error when no value provided"""
        with self.assertRaises(ValueError):
            node = LeafNode("h1", None)
            node.to_html()
    
    def test_parent_repr(self):
        """Testing ParentNode printing"""
        child = LeafNode("a", "just, testing", {"href": "https://www.boot.dev"})
        child2 = LeafNode("h1", "Writing here!")
        node = ParentNode("p",[child2,child])
        text = "ParentNode(p, children: [LeafNode(h1, Writing here!, None), LeafNode(a, just, testing, {'href': 'https://www.boot.dev'})], None)"
        self.assertEqual(repr(node), text)

    def test_parent_to_html_no_rec(self):
        """Testing ParentNode to_html with no recurssion"""
        child = LeafNode("a", "just, testing", {"href": "https://www.boot.dev"})
        child2 = LeafNode("h1", "Writing here!")
        node = ParentNode("p",[child2,child])
        text = '<p><h1>Writing here!</h1><a href="https://www.boot.dev">just, testing</a></p>'
        self.assertEqual(node.to_html(), text)

    def test_parent_to_html_one_lvl(self):
        """Testing ParentNode to_html with 1 level of recurssion"""
        child2 = LeafNode("a", "just, testing", {"href": "https://www.boot.dev"})
        child = LeafNode("h2","Exciting late night code!")
        parent = ParentNode("p",[child2])
        test_node = ParentNode("p",[child, parent])
        text = '<p><h2>Exciting late night code!</h2><p><a href="https://www.boot.dev">just, testing</a></p></p>'
        self.assertEqual(test_node.to_html(), text)

    def test_parent_to_html_three_level(self):
        """Testing ParentNode to_html with 3 level of recurssion"""
        child3 = LeafNode("p", "last bit of testing.")
        child2 = LeafNode("a", "just, testing", {"href": "https://www.boot.dev"})
        child = LeafNode("h2","Exciting late night code!")
        parent3 = ParentNode("p",[child2, child3])
        parent2 = ParentNode("h2",[parent3])
        parent = ParentNode("p",[parent2])
        test_node = ParentNode("p",[child, parent])
        text = '<p><h2>Exciting late night code!</h2><p><h2><p><a href="https://www.boot.dev">just, testing</a><p>last bit of testing.</p></p></h2></p></p>'
        self.assertEqual(test_node.to_html(), text)

    def test_parent_to_html_no_tag(self):
        """Testing ParentNode to_html error for no tag"""
        with self.assertRaises(ValueError):
            child = LeafNode("a", "this does not matter")
            node = ParentNode(None, [child])
            node.to_html()

    def test_parent_to_html_no_child(self):
        """Testing ParentNode to_html error for no child"""
        with self.assertRaises(ValueError):
            node = ParentNode("h5", None)
            node.to_html()

if __name__ == "__main__":
    unittest.main()