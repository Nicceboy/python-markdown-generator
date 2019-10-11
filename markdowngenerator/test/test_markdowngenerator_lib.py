# import logging
from . import BaseTestCase
from os import linesep


class TestMarkdownGenetarorLib(BaseTestCase):
    def test_header_generation(self):
        # Disable TOC
        self.test_document.enable_TOC = False

        self.test_document.addHeader(1, "My Very First HeAder")
        self.test_document.addHeader(2, "My second header.")
        self.test_document.addHeader(3, "My third header.")
        self.test_document.addHeader(4, "My fourth header.")
        self.test_document.addHeader(5, "My FiFtH HeAd3r.")
        self.test_document.addHeader(6, "My Sixth header...")
        line1 = f"# My Very First HeAder  {linesep}"
        # All headers except first header gets trailing new line. Note two spaces
        line2 = self._new_line()
        line3 = f"## My second header.  {linesep}"
        line4 = self._new_line()
        line5 = f"### My third header.  {linesep}"
        line6 = self._new_line()
        line7 = f"#### My fourth header.  {linesep}"
        line8 = self._new_line()
        line9 = f"##### My FiFtH HeAd3r.  {linesep}"
        line10 = self._new_line()
        line11 = f"###### My Sixth header...  {linesep}"
        self._insert_test_info(
            line1,
            line2,
            line3,
            line4,
            line5,
            line6,
            line7,
            line8,
            line9,
            line10,
            line11,
            func_name=self.test_header_generation.__name__,
        )

    def test_header_invalid_comparisions(self):

        # Disable TOC
        self.test_document.enable_TOC = False

        self.test_document.addHeader(1, "Header one for testINg!")
        self.test_document.addHeader(1, "Woaah, working huh??")
        line1 = f"# Header one for testing!  {linesep}"  # Some characters in lowercase
        line2 = self._new_line()
        line3 = f"# Woaah, working huh??  {linesep}"
        self._insert_test_info(
            line1,
            line2,
            line3,
            func_name=self.test_header_invalid_comparisions.__name__,
            test_if_UNEQUAL=True,
            unequal_lines=[1]
        )

    def test_header_abnormal_header_level_values(self):

        # Disable table of contents
        self.test_document.enable_TOC = False

        self.test_document.addHeader(-1, "Header size should be one.")
        self.test_document.addHeader(3242, "Header size should be in max size.")
        line1 = f"# Header size should be one.  {linesep}"
        line2 = self._new_line()
        line3 = f"###### Header size should be in max size.  {linesep}"
        self._insert_test_info(
            line1,
            line2,
            line3,
            func_name=self.test_header_abnormal_header_level_values.__name__,
        )
