import unittest
from blocks import *

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        """Testing markdown to blocks"""
        markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected_blocks = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        resulted_blocks = markdown_to_blocks(markdown)
        self.assertEqual(expected_blocks, resulted_blocks)

if __name__ == "__main__":
    unittest.main()