# file: module_a.py
import sys

print(f'>>> PATH >>>')

for path in sys.path:
    print(path)

print(f'<<< PATH <<<')

import module_b

def function_a():
    print("A")

module_b.function_b()
