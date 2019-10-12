# import logging
from . import BaseTestCase
from os import linesep


class TestMarkdownEmphasis(BaseTestCase):
    def test_bolded_text(self):

        self.test_document.enable_TOC = False
        self.test_document.addBoldedText("Is this bolded?", write_as_line=True)
        self.test_document.writeTextLine("This is not bolded.")
        self.test_document.addBoldedText("But this is.", write_as_line=True)

        # Test return value
        self.test_document.writeTextLine(
            self.test_document.addBoldedText("Complicated bolding...")
        )

        validationlines = [
            f"**Is this bolded?**  {linesep}",
            f"This is not bolded.  {linesep}",
            f"**But this is.**  {linesep}",
            f"**Complicated bolding...**  {linesep}",
        ]
        self._insert_test_info(
            validationlines, func_name=self.test_bolded_text.__name__
        )

    def test_italicized_text(self):

        self.test_document.enable_TOC = False
        self.test_document.addItalicizedText("Is this italicized?", write_as_line=True)
        self.test_document.writeTextLine("This is not italicized.")
        self.test_document.addItalicizedText("But this is.", write_as_line=True)

        # Test return value
        self.test_document.writeTextLine(
            self.test_document.addItalicizedText("Complicated italicizing...")
        )
        validationlines = [
            f"*Is this italicized?*  {linesep}",
            f"This is not italicized.  {linesep}",
            f"*But this is.*  {linesep}",
            f"*Complicated italicizing...*  {linesep}",
        ]
        self._insert_test_info(
            validationlines, func_name=self.test_bolded_text.__name__
        )
