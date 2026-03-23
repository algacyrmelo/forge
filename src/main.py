from markdown_blocks import block_to_block_type


def main():
    # block = "###### This is a heading"
    block = """\
1. Ha decadas em que nada acontece
2. e ha semanas em que decadas acontecem\
"""
    block_type = block_to_block_type(block)
    print(block_type)


main()
