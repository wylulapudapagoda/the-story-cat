class RegisterHandler:
    class ressources:
        _models = []
        _character = []
        
        def get(self,name):
            pass
        def getAll(self):
            pass
    class Register:
        def __init__(self,name:str):
            self.name = name
        def models(self):
            RegisterHandler.ressources._models.
