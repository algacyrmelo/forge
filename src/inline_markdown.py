import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
                continue
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(
        r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",
        text,
    )


def extract_markdown_links(text):
    return re.findall(
        r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",
        text,
    )


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        curr_text = old_node.text
        for image in images:
            image_text, image_url = image
            sections = curr_text.split(f"![{image_text}]({image_url})", 1)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(image_text, TextType.IMAGE, image_url))
            curr_text = sections[1]
        if curr_text:
            split_nodes.append(TextNode(curr_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        curr_text = old_node.text
        for link in links:
            link_text, link_url = link
            sections = curr_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            curr_text = sections[1]
        if curr_text:
            split_nodes.append(TextNode(curr_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
