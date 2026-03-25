from htmlnode import LeafNode, ParentNode
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
            case BlockType.HEADING:
                htmlnode = block_to_heading(block)
            case BlockType.CODE:
                htmlnode = block_to_code(block)
            case BlockType.ULIST:
                htmlnode = block_to_ulist(block)
            case BlockType.OLIST:
                htmlnode = block_to_olist(block)
            case BlockType.QUOTE:
                htmlnode = block_to_quote(block)
        children.append(htmlnode)
    return ParentNode("div", children)


def block_to_olist(block):
    items = block.split("\n")
    ol_children = []
    i = 1
    for item in items:
        li_children = text_to_children(item.lstrip(f"{i}. "))
        ol_children.append(ParentNode("li", li_children))
        i += 1
    return ParentNode("ol", ol_children)


def block_to_ulist(block):
    items = block.split("\n")
    ul_children = []
    for item in items:
        li_children = text_to_children(item.lstrip("- "))
        ul_children.append(ParentNode("li", li_children))
    return ParentNode("ul", ul_children)


def block_to_code(block):
    text = block.lstrip("`\n").rstrip("`")
    textnode = TextNode(text, TextType.CODE)
    child = text_node_to_html_node(textnode)
    return ParentNode("pre", [child])


def block_to_heading(block):
    text = block.lstrip("#")
    heading_level = len(block) - len(text)
    children = text_to_children(text.strip())
    return ParentNode(f"h{heading_level}", children)


def block_to_paragraph(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    return ParentNode("p", children)


def block_to_quote(block):
    lines = block.split("\n")
    lines = map(lambda line: line.lstrip("> "), lines)
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        child = text_node_to_html_node(textnode)
        children.append(child)
    return children
