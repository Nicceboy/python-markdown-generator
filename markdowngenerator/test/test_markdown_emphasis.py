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
            validationlines, func_name=self.test_italicized_text.__name__
        )

    def test_bolded_italicized_text(self):

        self.test_document.enable_TOC = False
        self.test_document.addBoldedAndItalicizedText(
            "Is this boldy italicized?", write_as_line=True
        )
        self.test_document.writeTextLine("This is not boldy italicized.")
        self.test_document.addBoldedAndItalicizedText(
            "But this is.", write_as_line=True
        )

        # Test return value
        self.test_document.writeTextLine(
            self.test_document.addBoldedAndItalicizedText(
                "Complicated boldy italicizing..."
            )
        )
        validationlines = [
            f"***Is this boldy italicized?***  {linesep}",
            f"This is not boldy italicized.  {linesep}",
            f"***But this is.***  {linesep}",
            f"***Complicated boldy italicizing...***  {linesep}",
        ]
        self._insert_test_info(
            validationlines, func_name=self.test_bolded_italicized_text.__name__
        )

    def test_strikethrough_text(self):

        self.test_document.enable_TOC = False
        self.test_document.addStrikethroughText(
            "Is this strikethroughed?", write_as_line=True
        )
        self.test_document.writeTextLine("This is not strikethroughed.")
        self.test_document.addStrikethroughText("But this is.", write_as_line=True)

        # Test return value
        self.test_document.writeTextLine(
            self.test_document.addStrikethroughText("Complicated strikethroughing...")
        )
        validationlines = [
            f"~~Is this strikethroughed?~~  {linesep}",
            f"This is not strikethroughed.  {linesep}",
            f"~~But this is.~~  {linesep}",
            f"~~Complicated strikethroughing...~~  {linesep}",
        ]
        self._insert_test_info(
            validationlines, func_name=self.test_strikethrough_text.__name__
        )

    def test_emphasis_whitespace_stripping(self):

        self.test_document.enable_TOC = False
        self.test_document.addBoldedText(
            " This is very bolded text with trailing spaces on input.   ",
            write_as_line=True,
        )
        self.test_document.addItalicizedText(
            " This is very italiced text with trailing spaces on input.   ",
            write_as_line=True,
        )
        self.test_document.addStrikethroughText(
            " This is strikethrough text with some extra spaces.    ",
            write_as_line=True,
        )

        validationlines = [
            f"**This is very bolded text with trailing spaces on input.**  {linesep}",
            f"*This is very italiced text with trailing spaces on input.*  {linesep}",
            f"~~This is strikethrough text with some extra spaces.~~  {linesep}",
        ]

        self._insert_test_info(
            validationlines, func_name=self.test_emphasis_whitespace_stripping.__name__
        )