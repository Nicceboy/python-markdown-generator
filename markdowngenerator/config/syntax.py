"""
MARKDOWN
"""

MARKDOWN_HEADER = "#"
MARKDOWN_HORIZONTAL_RULE = "---"
MARKDOWN_CODE_BLOCK = "```"
MARKDOWN_SINGLE_LINE_BLOCKQUOTE = ">"
MARKDOWN_MULTILINE_BLOCKQUOTE = ">>>"  # GitLab only
MARKDOWN_INLINE_CODE_HL = "`"
"""
HTML

Some charcters used for generating HTML

For escaping, following library has been used:
https://docs.python.org/3/library/html.html#html.escape
"""
# Hard space
HTML_SPACE_ALT = u"\u00A0"
HTML_SPACE = ""
HTML_AND = "&amp;"
HTML_LESS_THAN = "&lt;"
HTML_GRETER_THAN = "&gt;"
HMTL_SINGLE_QUOTE = "&#39;"
HTML_DOUBLE_QUOTE = "&quot;"

"""
OTHER
"""
# FOOTNOTE IDENTIFIER is string which is replaced with actual reference
# when inserting footnote reference and content into the text
FOOTNOTE_IDENTIFIER = "[footnote_id]"
