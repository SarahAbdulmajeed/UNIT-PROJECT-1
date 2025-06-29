class Person:
    def __init__(self, name:str ,username:str, password:str):
        self.name:str = name
        self.username:str = username
        self.password:str = password
    

class User(Person):
    def __init__(self, name:str, username:str, password:str):
        super().__init__(name, username, password)
        self.interviews:list = []
        self.skills:dict = {}
        
class Admin(Person):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)
        