from . import BaseTestCase
from os import linesep
import textwrap

class TestMarkdownBlocksAndQuotes(BaseTestCase):
    def test_code_block_escape_html(self):

        self.test_document.enable_TOC = False

        syntax = "python"
        code = textwrap.dedent("""\
               if title:
                   return f'![{alt_text}]({image_uri} \"{title}\")'
               return f\"![{alt_text}]({image_uri})\"""")

        self.test_document.addCodeBlock(code, syntax, escape_html=False)

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
            "    return f&#x27;![{alt_text}]({image_uri} &quot;{title}&quot;)&#x27;",
            linesep,
            'return f&quot;![{alt_text}]({image_uri})&quot;',
            linesep,
            f"```  {linesep}",
        ]
        self._insert_test_info(validationlines, func_name=self.test_code_block.__name__)