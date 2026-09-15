from markdown_to_blocks import markdown_to_blocks
import unittest

class test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_single_block(self):
        md = """
Just a single paragraph without any block breaks.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single paragraph without any block breaks."])

    def test_multiple_consecutive_newlines(self):
        md = """
First block




Second block

Third block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block", "Third block"])

    def test_blocks_with_leading_and_trailing_whitespace(self):
        md = """

Paragraph with spaces around

Another block with indentation   

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Paragraph with spaces around",
                "Another block with indentation",
            ],
        )

    def test_headers_and_code_blocks(self):
        md = """
# Heading 1

```python
print('hello')
```

Paragraph text
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "```python\nprint('hello')\n```",
                "Paragraph text",
            ],
        )

   
if __name__ == "__main__":
    unittest.main()
