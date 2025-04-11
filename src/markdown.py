import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        split_nodes = []
        node_string = node.text.split(delimiter)
        if len(node_string) % 2 == 0:
            raise ValueError("invalid markdown syntax: closing markdown delimiter is missing.")
        for x in range(0, len(node_string)):
            if x % 2 == 0:
                split_nodes.append(TextNode(node_string[x],TextType.TEXT))
            elif x % 2 == 1:
                split_nodes.append(TextNode(node_string[x],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(markdown_text):
    image_matches = re.findall(r"!\[(.*?)\]\((.*?)\)", markdown_text) #finds all instances of the ![alt-text](image-url) in a given string
    for image in image_matches:
        #finds the ![alt-text] and returns the alt text
        alt_text = re.findall(r"!\[(.*?)\]")
    return 0