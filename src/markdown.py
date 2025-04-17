import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        node_string = node.text.split(delimiter)
        if len(node_string) % 2 == 0:
            raise ValueError("invalid markdown syntax: closing markdown delimiter is missing.")
        for x in range(0, len(node_string)):
            if node_string[x] == "":
                continue
            if x % 2 == 0:
                split_nodes.append(TextNode(node_string[x],TextType.TEXT))
            else:
                split_nodes.append(TextNode(node_string[x],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        try:
            images = extract_markdown_images(original_text)
        except Exception as e:
            raise e
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            splitter = f"![{image[0]}]({image[1]})"
            sections = original_text.split(splitter)
            for x in range(0, len(sections)):
                if sections[x] != "" and x != len(sections)-1:
                    new_nodes.append(TextNode(sections[x],TextType.TEXT)) 
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[-1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        try:
            links = extract_markdown_links(original_text)
        except Exception as e:
            raise e
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            splitter = f"[{link[0]}]({link[1]})"
            sections = original_text.split(splitter)
            for x in range(0, len(sections)):
                if sections[x] != "" and x != len(sections)-1:
                    new_nodes.append(TextNode(sections[x],TextType.TEXT)) 
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[-1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(markdown_text):
    lazy_check = re.findall(r"!\[(.*?)\]\((.*?)\)", markdown_text) #finds all instances of the ![alt-text](image-url) in a given string
    specific_check = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown_text)
    if len(specific_check) != len(lazy_check):
        raise ValueError("invalid markdown syntax: unable to locate image markdown in string.")
    return specific_check

def extract_markdown_links(markdown_text):
    lazy_check = re.findall(r"[^!]\[(.*?)\]\((.*?)\)", markdown_text) #finds all instances of the ![alt-text](image-url) in a given string
    specific_check = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown_text)
    if len(specific_check) != len(lazy_check):
        raise ValueError("invalid markdown syntax: unable to locate image markdown in string.")
    return specific_check

def text_to_textnode(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "__", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes