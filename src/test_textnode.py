import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import split_node_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node =  text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")
    
    def test_italic(self):
        node = TextNode("italic text", TextType.ITALIC)
        html_node =  text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text") 
    
    def test_code(self):
        node = TextNode('print("hello boots")', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, 'print("hello boots")')
    
    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href" : "https://boot.dev"} )
    
    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://boot.dev/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, { "src" : "https://boot.dev/img.png", "alt" : "alt text"})

    def test_split_nodes_delimiter_code_simple(self):
        node = TextNode("hello `world` bear", TextType.TEXT)
        result = split_node_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "world")
        self.assertEqual(result[1].text_type, TextType.CODE)

        self.assertEqual(result[2].text, " bear")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_code_no_delimiter(self):
        node = TextNode("hello world bear", TextType.TEXT)
        result = split_node_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "hello world bear")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    
    def test_split_nodes_delimiter_code_bold(self):
        node = TextNode("boots is a **bear** wizard", TextType.TEXT)
        result = split_node_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "boots is a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "bear")
        self.assertEqual(result[1].text_type, TextType.BOLD)

        self.assertEqual(result[2].text, " wizard")
        self.assertEqual(result[2].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()

