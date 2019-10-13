import unittest
import os
import sys
import logging
from markdowngenerator.markdowngenerator import MarkdownGenerator

from dataclasses import dataclass
from typing import List

# from standardizer.markdown.config.conf import logger


LOGGING_LEVEL = logging.DEBUG
test_logger = logging.getLogger("markdowngenerator.test")
test_logger.setLevel(LOGGING_LEVEL)

# Formatter of log
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(LOGGING_LEVEL)
handler.setFormatter(formatter)
test_logger.addHandler(handler)
test_filename = "unittest.md"


class BaseTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)
        self.expected_output = EXPECTED_OUTPUT()
        self.test_document = None

    def __call__(self, result=None):
        """
        Does the required configuration for each
        testcase function. No need to repeat when writing actual
        testcase.
        """
        try:
            self._pre_setup()
            super(BaseTestCase, self).__call__(result)
        finally:
            self._post_teardown()

    def _pre_setup(self):
        """
        Generate library instance and file creation.
        Doing this manually, since library is designed to be used
        with 'with' statement to handle all automatically.
        """
        self.test_document = MarkdownGenerator(
            filename=test_filename,
            enable_write=False,
            syntax="gitlab",
        )
        self.test_document.__enter__()

    def _post_teardown(self):
        """
        Manually use exit function to write final file.
        Compare file content to expected values.

        Cleanup afterwards. (delete instance and file)
        """
        self.test_document.__exit__()
        with open(test_filename, "r") as final_file:
            self.assertIsMarkdownEqual(final_file)
        del self.test_document
        try:
            os.remove(test_filename)
        except OSError:
            pass

    def assertIsMarkdownEqual(self, final_file):
        """
        Method for comparing file contents to expected values.
        """
        if self.expected_output.value is None:
            raise AssertionError(
                "Testcase invalid. Expected output value should not be None."
            )
        expected_output_val = self.expected_output.value.split(os.linesep)
        generated_output = final_file.read()
        generated_output = generated_output.split(os.linesep)
        test_logger.debug(
            f"Expected lines: '{self.expected_output.value}', actual lines:'{generated_output}'"
        )
        assert len(expected_output_val) == len(
            generated_output
        ), f"Amount of expected and generated output lines is not equal. Generated: '{len(generated_output)}' Expected: '{len(expected_output_val)}'"

        for index, (expected_line, generated_line) in enumerate(
            zip(expected_output_val, generated_output)
        ):
            test_logger.debug(
                f"\nEXPECTED LINE: {expected_line}\nGENERATED LINE: {generated_line}\n"
            )
            if (
                self.expected_output.if_unequal.enabled
                and index + 1 in self.expected_output.if_unequal.lines
            ):
                assert (
                    expected_line != generated_line
                ), f"Expected line '{expected_line}' is match for final line '{generated_line}'"
            else:
                assert (
                    expected_line == generated_line
                ), f"Expected line '{expected_line}' is not match for final line '{generated_line}' when it shoud not."
        test_logger.info(f"{self.expected_output.func_name} Successful")

    def _insert_test_info(
        self, expected_output, func_name=None, test_if_UNEQUAL=False, unequal_lines=None
    ):
        """
        Method for getting test case function expected values
        and test case function name.

        Additionally using attribute 'test_if_UNEQUAL' for reverse testcase:
        expecting that specific lines are not matching.
        :param func_name: Name of the testcase function
        :param test_if_UNEQUAL: Paramater to define if tested for inequality, defaults to 'False'
        :param unequal_lines: List of lines from the input, which should be unequal. 
        """

        test_logger.debug(expected_output)
        self.expected_output.value = "".join(expected_output)
        test_logger.debug(f"Merged list is {self.expected_output.value}")
        self.expected_output.func_name = func_name.upper() if func_name else "Unknown?"
        self.expected_output.if_unequal.enabled = test_if_UNEQUAL
        self.expected_output.if_unequal.lines = unequal_lines

    def _new_line(self):
        """
        Method for generating newline string in
        Markdown syntax to help testing.

        Two spaces before newline mark.
        """
        return f"  {os.linesep}"


@dataclass
class IF_LINES_UNEQUAL:
    lines: List[int] = None
    enabled: bool = False


@dataclass
class EXPECTED_OUTPUT:
    value: str = None
    if_unequal: IF_LINES_UNEQUAL = IF_LINES_UNEQUAL()
    func_name: str = "Unknown"
