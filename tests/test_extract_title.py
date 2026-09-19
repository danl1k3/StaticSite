from extract_title import extract_title
import unittest

class test_extract_title(unittest.TestCase):
    def test_basic_title(self):
        md = """# Hello
This is some text."""
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_title_not_first_line(self):
        md = """Some text
Another line

# My title

More markdown here."""

        title = extract_title(md)
        self.assertEqual(title, "My title")

    def test_title_with_whitespace(self):
        md = """#     Hello World     
Some text."""
        
        title = extract_title(md)
        self.assertEqual(title, "Hello World")

    def test_no_h1(self):
        md = """## Hello
### Another title

Some text."""

        with self.assertRaises(Exception):
            extract_title(md)
    

