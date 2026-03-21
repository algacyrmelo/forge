def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(
        filter(
            lambda block: block != "",
            map(lambda block: block.strip(), blocks),
        ),
    )
