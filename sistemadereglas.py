from reglas import *

class sistemadereglas(KnowledgeEngine): 

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m1 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m2 (self):
        print("Puedes ingresar a mazmorras crepusculares y no es necesario los elites de Tierras Altas Crepusculares pues ya tienes buen nivel de armadura")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m3 (self):
        print("Aun no tienes el nivel de armadura necesaria, sin embargo, puedes gastar los puntos de justicia para comprar armadura nuvea y así subir tu nivel de objeto")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m4 (self):
        print("No puedes ingresar a mazmorras crepusculares, te falta nivel de objeto por encima de 300. Prueba derrotando los elites de Tierras altas Crepusculares para conseguir una armadura de mayor nivel. Tambien puedes comprar una mejor armadura con los puntos de justicia") 

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m5 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m6 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m7 (self):
        print("No puedes ingresar a mazmorras crepusculares, tienes el nivel de objeto por debajo de lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m8 (self):
        print("No puedes ingresar a mazmorras crepusculares, prueba derrotando los elites de Tierras altas Crepusculares para conseguir una armadura de mayor nivel ")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="NO")))
    def m9 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m10 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="NO")))
    def m11 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m12 (self):
        print("No puedes ingresar a mazmorras crepusculares, tienes el nivel de objeto por debajo de lo necesario prueba derrotando los elites de Tierras altas Crepusculares para conseguir una armadura de mayor nivel y con los beneficios de una hermandad nivel 25, puedes ganar un poco más de Puntos de Justicia") 

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="NO")))
    def m13 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m14 (self):
        print("Si puedes ingresar a mazmorras crepusculares, tienes lo necesario")

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="NO")))
    def m15 (self):
        print("No puedes ingresar a mazmorras crepusculares, tienes el nivel de objeto por debajo de lo necesario, consigue una hermandad nivel 25, puedes ganar un poco más de Puntos de Justicia") 

    @Rule(AND(reglas(pj_level = "SI")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m16 (self):
        print("No puedes ingresar a mazmorras crepusculares, tienes el nivel de objeto por debajo de lo necesario prueba derrotando los elites de Tierras altas Crepusculares para conseguir una armadura de mayor nivel y con los beneficios de una hermandad nivel 25, puedes ganar un poco más de Puntos de Justicia") 

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m17 (self):
        print("Es necesario el nivel 85 para entrar a mazmorras crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m18 (self):
        print("Es necesario el nivel 85 para entrar a mazmorras crepusculares, ya te falta poco. Recuerda derrotar a los Elites de Tierras Altas Crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m19 (self):
        print("Tienes el nivel de objeto de armadura necesaria pero necesitas llegar al nivel 85 para hacer mazmorras crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m20 (self):
        print("Aún no tienes el nivel 85 y nivel de objeto de armadura para entrar a mazmorras crepusculares, ya te falta poco. Recuerda derrotar a los Elites de Tierras Altas Crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m21 (self):
        print("Tienes el nivel de objeto de armadura necesaria pero necesitas llegar al nivel 85 para hacer mazmorras crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m22 (self):
        print("Aún no tienes el nivel 85 para entrar a mazmorras crepusculares, ya te falta poco. Recuerda derrotar a los Elites de Tierras Altas Crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="SI")))
    def m23 (self):
        print("Aún no tienes el nivel 85 y nivel de objeto de armadura para entrar a mazmorras crepusculares, ya te falta poco")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="SI")))
    def m24 (self):
        print("Aún no tienes el nivel 85 y nivel de objeto de armadura para entrar a mazmorras crepusculares, ya te falta poco. Recuerda derrotar a los Elites de Tierras Altas Crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="NO")))
    def m25 (self):
        print("Aún no tienes el nivel 85 para entrar a mazmorras crepusculares, ya te falta poco. Consigue una hermandad nivel 25 para tener más puntos de experiencia y subir de nivel más rápido")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m26 (self):
        print("Aún no tienes el nivel 85 para entrar a mazmorras crepusculares, ya te falta poco. Consigue una hermandad nivel 25 para tener más puntos de experiencia y recuerda derrotar a los Elites de Tierras Altas Crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "SI")), (reglas(pj_guild="No")))
    def m27 (self):
        print("Aún no tienes el nivel 85 para entrar a mazmorras crepusculares, ya te falta poco. Consigue una hermandad nivel 25 para tener más puntos de experiencia y subir de nivel más rápido")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 2000)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m28 (self):
        print("Aún no tienes el nivel 85 y nivel de objeto de armadura para entrar a mazmorras crepusculares, ya te falta poco. Consigue una hermandad nivel 25 para tener más puntos de experiencia y recuerda derrotar a los Elites de Tierras Altas Crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="NO")))
    def m29 (self):
        print("Aún no tienes el nivel 85 y nivel de objeto de armadura para entrar a mazmorras crepusculares, ya te falta poco. Consigue una hermandad nivel 25 para tener más puntos de experiencia")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 300)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m30 (self):
        print("Aún no tienes el nivel 85 para entrar a mazmorras crepusculares, ya te falta poco. Consigue una hermandad nivel 25 para tener más puntos de experiencia y recuerda derrotar a los Elites de Tierras Altas Crepusculares")

    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "SI")), (reglas(pj_guild="NO")))
    def m31 (self):
        print("Aún no tienes el nivel 85 y nivel de objeto de armadura para entrar a mazmorras crepusculares, ya te falta poco. Consigue una hermandad nivel 25 para tener más puntos de experiencia")
     
    @Rule(AND(reglas(pj_level = "NO")), (reglas(pj_ilvl = 299)), (reglas(pj_justicia = 1999)), (reglas(pj_elites = "NO")), (reglas(pj_guild="NO")))
    def m32 (self):
        print("No puedes ingresar a mazmorras crepusculares, es necesario el nivel 25 y tener un buen nivel de armadura. Consigue una hermandad nivel 25 para tener más puntos de experiencia y recuerda derrotar a los Elites de Tierras Altas Crepusculares")        