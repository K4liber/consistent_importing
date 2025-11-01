# pkg_a/module_a.py


class ClassA:
    pass


# pkg_b/module_b.py


class ClassB:
    def compare(self, other: ClassA) -> bool:
        return str(self) == str(other)
