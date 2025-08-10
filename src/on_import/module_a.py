print("hello from module.py")


def module_function() -> None:
    import src.on_import.module_b  # noqa: PLC0415

    print(dir(src.on_import.module_b))
    print("hello from module_function")


print("goodbye from module.py")

cc = 1
