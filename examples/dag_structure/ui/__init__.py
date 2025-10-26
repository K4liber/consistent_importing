from dag_structure.ui.cli import Cli
from dag_structure.ui.gui import Gui
from dag_structure.ui.interface import UserInterface

_USER_INTERFACE: UserInterface | None = None
_ui_type = "gui"


def _initialize_user_interface() -> None:
    global _USER_INTERFACE

    if _ui_type == "gui":
        _USER_INTERFACE = Gui()
    elif _ui_type == "cli":
        _USER_INTERFACE = Cli()
    else:
        raise ValueError(f"Unknown UI type: {_ui_type}")


def get_user_interface() -> UserInterface:
    if _USER_INTERFACE is None:
        _initialize_user_interface()

    return _USER_INTERFACE
