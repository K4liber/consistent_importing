from dag_structure.db import get_database
from dag_structure.model.interface import ModelInterface


class BaseModel(ModelInterface):
    pass


db = get_database()
