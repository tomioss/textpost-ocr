from PIL import Image
import sys

import pyocr
import pyocr.builders


def get_available_tool():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    return tools[0]

tool = get_available_tool()
print("Will use tool: '%s'" % (tool.get_name()))


def get_available_language(tool):
    langs = tool.get_available_languages()
    return langs[0]

lang = get_available_language(tool)
print("Will use lang: '%s'" % (lang))
