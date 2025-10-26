from dag_structure.db import get_database
from dag_structure.model import get_model
from dag_structure.ui import get_user_interface

model = get_model()
db = get_database()
ui = get_user_interface()
