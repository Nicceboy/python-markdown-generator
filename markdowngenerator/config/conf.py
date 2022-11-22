TOOL_VERSION_INFO_DIR = "results/tool-version-info"
SHELLCODE_OUTPUT_DIR = "shellcode"

DEFAULT_FILE_LOCATION = "default_file"
MAX_HEADER_LEVEL = 6
MIN_HEADER_LEVEL = 1
TABLE_OF_CONTENT_LINE_POSITION = 1


TMP_HEADER_INFO_PREFIX = "headerinfo"
TMP_HEADER_INFO_SUFFIX = "json"

# Every extension should have at least following attributes:
# result_dir, tool_name, extension_name

# NOTE: result_dir is name of the directory, not path. Should be implemented in other way some day
EXTENSIONS_CONF = {
    "PEEPDF_CONF": {
        "result_dir": "peepdf",
        "tool_name": "peepdf",
        "extension_name": "peepdfResultGenerator",
    },
    "CLAMAV_CONF": {
        "result_dir": "clamav",
        "tool_name": "clamav",
        "extension_name": "ClamAVResultGenerator",
    },
    "STRINGS_CONF": {
        "result_dir": "strings",
        "tool_name": "strings",
        "extension_name": "stringsResultGenerator",
    },
    "OLEVBA_CONF": {
        "result_dir": "olevba",
        "tool_name": "olevba",
        "extension_name": "olevbaResultGenerator",
    },
    "PDFID_CONF": {
        "result_dir": "pdfid",
        "tool_name": "pdfid",
        "extension_name": "PDFiDResultGenerator",
    },
    "SCTEST_CONF": {
        "result_dir": "sctest",
        "tool_name": "sctest",
        "extension_name": "jsunpacknsctestResultGenerator",
    },
    "OLEDUMP_CONF": {
        "result_dir": "oledump",
        "tool_name": "oledump",
        "extension_name": "oledumpResultGenerator",
    },
}
