from textnode import TextNode, TextType
import os 
from copystatic import copy_static

def main():
    static_path = "../static"
    public_path = "../public"
    copy_static(static_path, public_path)


main()

