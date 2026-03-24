from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                paragraph = block_to_paragraph(block)
                root_children.append(paragraph)
            case _:
                pass
    return ParentNode("div", root_children)


def block_to_paragraph(block):
    block = block.replace("\n", " ")
    block_children = text_to_children(block)
    return ParentNode("p", block_children)


def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        child = text_node_to_html_node(textnode)
        children.append(child)
    return children
