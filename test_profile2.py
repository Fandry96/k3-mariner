import timeit
import sys

setup_persist = """
from duckduckgo_search import DDGS
class MarinerSearchToolPersist:
    def __init__(self):
        self.ddgs = DDGS()
    def forward(self, query):
        return list(self.ddgs.text(query, max_results=5))
tool = MarinerSearchToolPersist()
"""

code_persist = """
try:
    tool.forward("python duckduckgo search")
except Exception as e:
    pass
"""

setup_context = """
from duckduckgo_search import DDGS
class MarinerSearchToolContext:
    def forward(self, query):
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=5))
tool = MarinerSearchToolContext()
"""

code_context = """
try:
    tool.forward("python duckduckgo search")
except Exception as e:
    pass
"""

print("Persist instance:", timeit.timeit(code_persist, setup=setup_persist, number=5))
print("Context manager:", timeit.timeit(code_context, setup=setup_context, number=5))
