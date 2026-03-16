from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def main():
    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    node = TextNode("**This is bold text**", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)


main()
