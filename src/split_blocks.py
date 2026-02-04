from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = []
    markdown_list = markdown.split("\n\n")
    for markdown in markdown_list:
        striped_markdown = markdown.strip()
        if striped_markdown != "":
            blocks.append(striped_markdown)
    return blocks
    