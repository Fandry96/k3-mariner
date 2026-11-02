import timeit
import re

setup = """
import re

ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

def clean_ansi(text):
    return ANSI_ESCAPE.sub("", text)

text_to_clean = "This is some text \x1b[31mwith ANSI\x1b[0m escape codes."
"""

code1 = """
clean_ansi(text_to_clean)
"""

print("clean_ansi (sub):", timeit.timeit(code1, setup=setup, number=100000))
