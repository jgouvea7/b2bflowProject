from domain.entity import User
from infrastructure.model.model import session
''
''
def create_user_db(name:str, cell:str):
    new_user = User(
        name=name,
        cell=cell
    )
    session.add(new_user)
    session.commit()