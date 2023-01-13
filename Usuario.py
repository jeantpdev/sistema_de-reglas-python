from msilib.schema import Class


class Usuario:
    def __init__(self):
        self.nombre = None
        self.contra = None
        self.identificacion = 0
        
    def set_nombre(self, nombre):
            self.nombre = nombre
            
    def get_nombre(self):
        return self.nombre
    
    def set_contra(self, contra):
            self.contra = contra
            
    def get_contra(self):
        return self.contra
    
    def set_id(self, id):
            self.identificacion = id
            
    def get_id(self):
        return self.identificacion