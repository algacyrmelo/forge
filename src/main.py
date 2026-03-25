from markdown_to_html import markdown_to_html_node


def main():
    md = """
> This is a
>block quote
"""

    root = markdown_to_html_node(md)
    print(root.to_html())


main()
