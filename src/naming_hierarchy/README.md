```
for module_name, module in sys.modules.items():
    if 'time' in module_name or 'random' in module_name:
        file = module.__file__ if hasattr(module, '__file__') else 'build-in'
        print(f'Found module "{module_name}", file: {file}')

print('random' in sys.builtin_module_names)  # False, not a built-in module
print('time' in sys.builtin_module_names)    # True, built-in module
```