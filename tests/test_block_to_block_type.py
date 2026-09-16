import unittest
from block_to_block_type import BlockType, block_to_block_type

class test_block_to_block_type(unittest.TestCase):
    import unittest
from block_to_block_type import BlockType, block_to_block_type


class test_block_to_block_type(unittest.TestCase):
    def test_headings_valid(self):
        h1 = """# Heading 1"""
        h3 = """### Heading 3"""
        h6 = """###### Heading 6"""
        self.assertEqual(block_to_block_type(h1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h6), BlockType.HEADING)

    def test_headings_invalid_fallback_paragraph(self):
        no_space = """#Heading without space"""
        too_many_hashes = """####### Heading 7 with seven hashes"""
        empty_hash = """# """
        self.assertEqual(block_to_block_type(no_space), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(too_many_hashes), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(empty_hash), BlockType.PARAGRAPH)

    def test_code_block_valid(self):
        code ="""
```
def hello():
    print("world")
```
"""
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_code_block_invalid_fallback_paragraph(self):
        no_closing = """
```
unclosed code block
"""
        no_newline_after_start = """
```def hello():
```
"""
        not_enough_backticks = """``
missing backtick
``
"""
        self.assertEqual(block_to_block_type(no_closing), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(no_newline_after_start), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(not_enough_backticks), BlockType.PARAGRAPH)

    def test_quote_block_valid(self):
        quote_with_space = """> Single quote line"""
        multiline_quote = """
>First line
> Second line with space
>Third line
"""
        self.assertEqual(block_to_block_type(quote_with_space), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(multiline_quote), BlockType.QUOTE)

    def test_quote_block_invalid_fallback_paragraph(self):
        missing_quote_on_second_line = """
> First line is quoted
Second line is not quoted
"""
        self.assertEqual(block_to_block_type(missing_quote_on_second_line), BlockType.PARAGRAPH)

    def test_unordered_list_valid(self):
        single_item = """
- Single list item
"""
        multiline_list = """
- First item
- Second item
- Third item
"""
        self.assertEqual(block_to_block_type(single_item), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(multiline_list), BlockType.UNORDERED_LIST)

    def test_unordered_list_invalid_fallback_paragraph(self):
        no_space = """
-Item without space
- Another
"""
        different_marker = """
* Asterisk instead of dash
* Item 2
"""
        broken_middle = """
- Item 1
Missing dash item
- Item 3
"""
        self.assertEqual(block_to_block_type(no_space), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(different_marker), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(broken_middle), BlockType.PARAGRAPH)

    def test_ordered_list_valid(self):
        single_item = """1. Single ordered item"""
        multiline_ordered = """
1. First step
2. Second step
3. Third step
"""
        self.assertEqual(block_to_block_type(single_item), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(multiline_ordered), BlockType.ORDERED_LIST)

    def test_ordered_list_invalid_fallback_paragraph(self):
        start_not_at_one = """
2. Step two
3. Step three
"""
        wrong_increment = """
1. First step
3. Skipped step two
"""
        missing_space = """
1.First without space
2. Second
"""
        missing_dot = """
1 First without dot
2 Second
"""
        broken_middle = """
1. First step
Broken text
3. Third step
"""
        self.assertEqual(block_to_block_type(start_not_at_one), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(wrong_increment), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(missing_space), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(missing_dot), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(broken_middle), BlockType.PARAGRAPH)

    def test_paragraph_general(self):
        normal_text = """
This is just a simple paragraph of text.
It spans across multiple lines without special block prefixes.
"""
        self.assertEqual(block_to_block_type(normal_text), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
