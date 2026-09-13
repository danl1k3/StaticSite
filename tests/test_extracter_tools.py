import unittest
from extracter_tools import extract_markdown_links, extract_markdown_images

class test_extracter_tools(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
                "This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")])
    
    def test_extract_markdown_images_double(self):
        matches = extract_markdown_images(
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertListEqual(
                [
                    ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                    ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                ]
                , matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual(
                [
                    ("to boot dev", "https://www.boot.dev"), 
                    ("to youtube", "https://www.youtube.com/@bootdotdev")
                ], matches)

if __name__ == "__main__":
    unittest.main()    
