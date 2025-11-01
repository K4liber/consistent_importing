from pkg_a.module_a import ClassA


class ClassB:
    def compare(self, other: ClassA) -> bool:
        return str(self) == str(other)
