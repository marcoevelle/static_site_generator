def markdown_to_blocks(markdown):
    blocks = []
    stripped_blocks = []
    split_blocks = markdown.split("\n\n")
    for split_block in split_blocks:
        stripped_blocks.append(split_block.strip('\n'))
    for block in stripped_blocks:
        if block != "":
            blocks.append(block)
    return blocks