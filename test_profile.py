import timeit

setup = """
from duckduckgo_search import DDGS

ddgs_instance = DDGS()
"""

code_reuse = """
try:
    list(ddgs_instance.text("python duckduckgo search", max_results=5))
except Exception as e:
    pass
"""

code_context = """
try:
    with DDGS() as ddgs:
        list(ddgs.text("python duckduckgo search", max_results=5))
except Exception as e:
    pass
"""

print("Reusing instance:", timeit.timeit(code_reuse, setup=setup, number=5))
print("Context manager:", timeit.timeit(code_context, setup=setup, number=5))
