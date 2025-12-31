from textnode import TextNode, TextType


def main():
    dummy_text = TextNode(
        "This is some anchor text",
        TextType.PLAIN_TEXT,
        "http://www.boot.dev",
    )
    print(dummy_text)


main()