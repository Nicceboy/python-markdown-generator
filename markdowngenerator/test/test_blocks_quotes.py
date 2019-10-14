from . import BaseTestCase
from os import linesep
import textwrap

class TestMarkdownBlocksAndQuotes(BaseTestCase):
    def test_code_block(self):

        self.test_document.enable_TOC = False

        syntax = "python"
        code = textwrap.dedent("""\
               if title:
                   return f'![{alt_text}]({image_uri} \"{title}\")'
               return f\"![{alt_text}]({image_uri})\"""")

        self.test_document.addCodeBlock(code, syntax)

        validationlines = [
            f"```python{linesep}",
            f"if title:{linesep}",
            "    return f'![{alt_text}]({image_uri} \"{title}\")'",
            linesep,
            'return f"![{alt_text}]({image_uri})"',
            linesep,
            f"```  {linesep}",
        ]
        self._insert_test_info(validationlines, func_name=self.test_code_block_escape_html.__name__)



    def test_code_block_escape_html(self):

        self.test_document.enable_TOC = False

        syntax = "python"
        code = textwrap.dedent("""\
               if title:
                   return f'![{alt_text}]({image_uri} \"{title}\")'
               return f\"![{alt_text}]({image_uri})\"""")

        self.test_document.addCodeBlock(code, syntax, escape_html=True)

        validationlines = [
            f"```python{linesep}",
            f"if title:{linesep}",
            "    return f&#x27;![{alt_text}]({image_uri} &quot;{title}&quot;)&#x27;",
            linesep,
            'return f&quot;![{alt_text}]({image_uri})&quot;',
            linesep,
            f"```  {linesep}",
        ]
        self._insert_test_info(validationlines, func_name=self.test_code_block.__name__)

    def test_inline_code_block(self):
        self.test_document.enable_TOC = False


        inline_block1 = self.test_document.addInlineCodeBlock("print(\"This is it\")")
        self.test_document.writeTextLine(inline_block1, html_escape=False)
        self.test_document.addInlineCodeBlock("print(\"Did not except this!\")", write=True)
        self.test_document.addInlineCodeBlock("print(\"Oooooor, Did not except this!\")", write=True, escape_html=True)

        validationlines = [
            f"`print(\"This is it\")`  {linesep}",
            f"`print(\"Did not except this!\")``print(&quot;Oooooor, Did not except this!&quot;)`"

        ]

        self._insert_test_info(validationlines, func_name=self.test_inline_code_block.__name__)


    def test_single_line_blockquote(self):
        self.test_document.enable_TOC = False
        self.test_document.addSinglelineBlockQuote("What's up there? Just single block quoting.")
        validationlines = [
            f">What&#x27;s up there? Just single block quoting.  {linesep}"
                ]
        self._insert_test_info(validationlines, func_name=self.test_single_line_blockquote.__name__)

