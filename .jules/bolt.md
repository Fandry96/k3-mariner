## 2024-05-22 - Regex Compilation Optimization
**Learning:** Pre-compiling regex patterns to module level avoids recompilation overhead in hot loops.
**Action:** Always look for `re.compile` inside loops or frequently called functions and move them to global scope.
