from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import torch


class Model:
    def add_module(self, module: "torch.Module") -> None:
        print(f"Adding module: {module}")
        ...
