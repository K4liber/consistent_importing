import inspect

from src.on_import.module_a import module_function

print("hello from main.py")
print(dir(module_function))
print(inspect.getsource(module_function))
module_function()
print("goodbye from main.py")
