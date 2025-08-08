print("hello from module.py")

def module_function() -> None:
    import examples.on_import.another_module
    print(dir(examples.on_import.another_module))
    print("hello from module_function")

print("goodbye from module.py")
