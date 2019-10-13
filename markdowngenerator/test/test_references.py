from . import BaseTestCase
from os import linesep


class TestMarkdownReferences(BaseTestCase):
    def test_href_notation(self):

        self.test_document.enable_TOC = False
        self.test_document.writeTextLine(
            self.test_document.generateHrefNotation(
                "This text takes you into Google", "https://google.fi"
            )
        )
        self.test_document.writeTextLine(
            self.test_document.generateHrefNotation(
                "This text takes you into Google with title",
                "https://google.fi",
                "Such a title.",
            ),
            html_escape=False,
        )

        validationlines = [
            f"[This text takes you into Google](https://google.fi)  {linesep}",
            f'[This text takes you into Google with title](https://google.fi "Such a title.")  {linesep}',
        ]
        self._insert_test_info(
            validationlines, func_name=self.test_href_notation.__name__
        )

    def test_image_href(self):


        self.test_document.enable_TOC = False
        self.test_document.writeTextLine(
            self.test_document.generateImageHrefNotation(
                "/path/to/my/image", "Text once URI is broken"
            )
        )
        self.test_document.writeTextLine(
            self.test_document.generateImageHrefNotation(
                "http://smiley.image/yes.png",
                "Smiley image",
                "Such a title.",
            ),
            html_escape=False,
        )
        validationlines = [
            f"![Text once URI is broken](/path/to/my/image)  {linesep}",
            f'![Smiley image](http://smiley.image/yes.png "Such a title.")  {linesep}'

        ]

        self._insert_test_info(
            validationlines, func_name=self.test_image_href.__name__
        )