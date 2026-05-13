import time
from agent import MarinerSearchTool

tool = MarinerSearchTool()

start = time.time()
print(tool.forward("python"))
print("First query took:", time.time() - start)

start = time.time()
print(tool.forward("python"))
print("Second query took:", time.time() - start)
