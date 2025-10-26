from dag_structure.db.file import FileDatabase
from dag_structure.db.interface import DatabaseInterface
from dag_structure.db.sql import SQLDatabase

_db_type = "sql"
_DB_INTERFACE: DatabaseInterface | None = None


def _init_db() -> None:
    if _db_type == "sql":
        _DB_INTERFACE = SQLDatabase()
    elif _db_type == "file":
        _DB_INTERFACE = FileDatabase()
    else:
        raise ValueError(f"Unknown database type: {_db_type}")


def get_database() -> DatabaseInterface:
    if _DB_INTERFACE is None:
        _init_db()

    return _DB_INTERFACE
