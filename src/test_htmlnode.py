import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_equals_empty_string(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
    def test_constructor_stored(self):
        node = HTMLNode(tag="beep", value="boop", children=["gremlin's"], props={})
        self.assertEqual(node.tag, "beep")
        self.assertEqual(node.value, "boop")
        self.assertEqual(node.children, ["gremlin's"])
        self.assertEqual(node.props, {})
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "BEEP This website is awesome?", {"href" :"www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="www.boot.dev">BEEP This website is awesome?</a>')

    def test_leaf_to_html_no_tag_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me", {"href": "https://www.boot.dev"})
        self.assertEqual(
        node.to_html(),
        '<a href="https://www.boot.dev">Click me</a>',
    )   
        
    def test_leaf_to_html_raises_without_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("span", "hi", {"class": "greeting", "id": "g1"})
        html = node.to_html()
        self.assertIn('<span ', html)
        self.assertIn('class="greeting"', html)
        self.assertIn('id="g1"', html)
        self.assertTrue(html.endswith(">hi</span>"))

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
  

if __name__ == "__main__":
    unittest.main()