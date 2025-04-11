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
        node = TextNode("This is a test of a **bolded section** and a *italic section* for my test suite", TextType.TEXT)
        results = split_nodes_delimiter([node], "*", TextType.ITALIC)
        result_text = [
            TextNode("This is a test of a ", TextType.TEXT),
            TextNode("bolded section", TextType.ITALIC),
            TextNode(" and a *italic section* for my test suite", TextType.TEXT)
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

if __name__ == "__main__":
    unittest.main()