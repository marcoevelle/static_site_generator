import unittest
from markdown import *
from textnode import *

class TestMarkdown(unittest.TestCase):
    def test_split_node(self):
        """Testing spliting a single TextNode"""
        node = TextNode("This is a test of a `coded section` for my test suite", TextType.TEXT)
        results = split_nodes_delimiter([node], "`", TextType.CODE)
        result_text = [
            TextNode("This is a test of a ", TextType.TEXT),
            TextNode("coded section", TextType.CODE),
            TextNode(" for my test suite", TextType.TEXT)
        ]
        self.assertEqual(result_text, results)

    def test_split_node_bold(self):
        """Testing spliting a single TextNode with multiple delimiters"""
        node = TextNode("This is a test of a **bolded section** and a *italic section* for my test suite", TextType.TEXT)
        results = split_nodes_delimiter([node], "**", TextType.BOLD)
        result_text = [
            TextNode("This is a test of a ", TextType.TEXT),
            TextNode("bolded section", TextType.BOLD),
            TextNode(" and a *italic section* for my test suite", TextType.TEXT)
        ]
        self.assertEqual(result_text, results)

    def test_split_node_italic(self):
        """Testing spliting a single TextNode with multiple delimiters"""
        node = TextNode("This is a test of a __bolded section__ and a *italic section* for my test suite", TextType.TEXT)
        results = split_nodes_delimiter([node], "*", TextType.ITALIC)
        result_text = [
            TextNode("This is a test of a __bolded section__ and a ", TextType.TEXT),
            TextNode("italic section", TextType.ITALIC),
            TextNode(" for my test suite", TextType.TEXT)
        ]
        self.assertEqual(result_text, results)

    def test_split_node_fail(self):
        """Testing spliting a single TextNode with the incorrect number of delimiters"""
        with self.assertRaises(ValueError):
            node = TextNode("This is a test of a `coded section for my test suite", TextType.TEXT)
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_node_fail_incorrect_number(self):
        """Testing spliting a single TextNode with the incorrect number of delimiters"""
        with self.assertRaises(ValueError):
            node = TextNode("This is a test of a **bolded section* for my test suite", TextType.TEXT)
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_split_node_fail_incorrect_number_2(self):
        """Testing spliting a single TextNode with the incorrect number of delimiters"""
        with self.assertRaises(ValueError):
            node = TextNode("This is a test of a *bolded section** for my test suite", TextType.TEXT)
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_extract_markdown_image(self):
        """Testing regex search for multiple image markdown texts"""
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected_text = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(expected_text, result)

    def test_extract_markdown_image_2(self):
        """Testing regex search for single image markdown text"""
        text = "This is a map of the world ![asteria](https://starfinder.marcoevelle.games)"
        result = extract_markdown_images(text)
        expected_text = [('asteria', 'https://starfinder.marcoevelle.games')]
        self.assertEqual(expected_text, result)

    def test_extract_markdown_image_failure(self):
        """Testing regex search for single mistyped markdown image"""
        with self.assertRaises(ValueError):
            text = "This is a map of the world ![[asteria](https://starfinder.marcoevelle.games)"
            extract_markdown_images(text)

    def test_extract_markdown_image_failure_2(self):
        """Testing regex search for single mistyped markdown image with multiple hits"""
        with self.assertRaises(ValueError):
            text = "This is a map of the world ![[asteria](https://starfinder.marcoevelle.games) and here ![sector map](https://echos.marcoevelle.games)"
            extract_markdown_images(text)

    def test_extract_markdown_link(self):
        """Testing regex search for multiple link markdown texts"""
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        expected_text = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(expected_text, result)

    def test_extract_markdown_link_2(self):
        """Testing regex search for single link markdown text"""
        text = "This is a map of the world [asteria](https://starfinder.marcoevelle.games)"
        result = extract_markdown_links(text)
        expected_text = [('asteria', 'https://starfinder.marcoevelle.games')]
        self.assertEqual(expected_text, result)

    def test_extract_markdown_link_failure(self):
        """Testing regex search for single mistyped markdown link"""
        with self.assertRaises(ValueError):
            text = "This is a map of the world [[asteria]](https://starfinder.marcoevelle.games)"
            extract_markdown_links(text)

    def test_extract_markdown_link_failure_2(self):
        """Testing regex search for single mistyped markdown link with multiple hits"""
        with self.assertRaises(ValueError):
            text = "This is a map of the world [[asteria]](https://starfinder.marcoevelle.games) and here [sector map](https://echos.marcoevelle.games)"
            extract_markdown_links(text)

    def test_split_nodes_images(self):
        """Testing splitting multiple images inline"""
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_images(self):
        """Testing splitting multiple images inline"""
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_text_to_textnode(self):
        text = "This is **text** with an __italic__ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnode(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()