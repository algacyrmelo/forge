from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                htmlnode = block_to_paragraph(block)
                children.append(htmlnode)
            case BlockType.HEADING:
                htmlnode = block_to_heading(block)
                children.append(htmlnode)
            case BlockType.CODE:
                htmlnode = block_to_code(block)
                children.append(htmlnode)
            case _:
                pass
    return ParentNode("div", children)


def block_to_code(block):
    text = block.lstrip("`\n").rstrip("`")
    textnode = TextNode(text, TextType.CODE)
    child = text_node_to_html_node(textnode)
    return ParentNode("pre", [child])


def block_to_heading(block):
    text = block.lstrip("#")
    heading_level = len(block) - len(text)
    block_children = text_to_children(text.strip())
    return ParentNode(f"h{heading_level}", block_children)


def block_to_paragraph(block):
    text = block.replace("\n", " ")
    block_children = text_to_children(text)
    return ParentNode("p", block_children)


def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        child = text_node_to_html_node(textnode)
        children.append(child)
    return children
