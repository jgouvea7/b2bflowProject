from uuid import uuid4


class User:
    def __init__(self, name: str, cell: str):
        self.id = uuid4()
        self.name = name
        self.cell = cell