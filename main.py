from multiprocessing.sharedctypes import Value
from Usuario import *
from sistemadereglas import *
from random import choice
import json

usuario = Usuario()
engine = sistemadereglas()

informacion_json =  []
informacion_json_final = []

def existe_historial_usuarios():
    try:
        with open('users_data.json') as archivo:
            return True
    except FileNotFoundError as e:
        return False

def existe_historial():
    try:
        with open('historial.json') as archivo:
            return True
    except FileNotFoundError as e:
        return False
    
def agregar_cuenta_json(usuario, contra):
    if existe_historial_usuarios() == True:
        nuevos_datos = informacion_usuario = {"Usuario" : usuario, "Contra" : contra}
        with open("users_data.json") as archivo_json:
            datos = json.load(archivo_json)
        datos.append(nuevos_datos)

        with open("users_data.json", 'w') as archivo_json:
            json.dump(datos, archivo_json, indent=3)
            print("Se han añadido los siguientes datos al archivo " + archivo_json.name+"\n")
    else:    
        informacion_usuario = {"Usuario" : usuario, "Contra" : contra}
        with open("users_data.json", 'w') as archivo_json:
            informacion_json.append(informacion_usuario)
            json.dump(informacion_json, archivo_json, indent=3)
            print(archivo_json.name+" creado exitosamente")

def agregar_datos_generales_json(nombre, id, preguntas, respuestas):
    if existe_historial() == True:
        nuevos_datos = {"Id" : id, "Usuario" : nombre, "Preguntas": preguntas, "Respuesta": respuestas}
        with open("historial.json") as archivo_json:
            datos = json.load(archivo_json)
        datos.append(nuevos_datos)

        with open("historial.json", 'w') as archivo_json:
            json.dump(datos, archivo_json, indent=3)
            print("Se han añadido los siguientes datos al archivo " + archivo_json.name+"\n")
    else:    
        informacion_usuario = {"Id" : id, "Usuario" : nombre, "Preguntas": preguntas , "Respuesta": respuestas}
        with open("historial.json", 'w') as archivo_json:
            informacion_json_final.append(informacion_usuario)
            json.dump(informacion_json_final, archivo_json, indent=3)
            print(archivo_json.name+" creado exitosamente")
            
def asignar_id_usuario():
    if existe_historial_usuarios() == True:
        with open("users_data.json") as archivo_json:
            datos = json.load(archivo_json)
            return len(datos) + 1
    else:
        return 1  

#Funcion encaragda de buscar dentro del historial, un ID y mostrar los resutlados que contenga
def mostrar_json_id(id):
    if existe_historial() == True:
        with open("historial.json") as archivo_json:
            datos = json.load(archivo_json)
            try:
                v = [x for x in datos if x['Id'] == id]
                if len(v) == 0:
                    print("No existe ese id")
                else:
                    print(v)
            except:
                print("No existe registro")
    else:
        print("No existe el historial.json")     

def mostrar_json_usuario(usuario):
    if existe_historial() == True:
        with open("historial.json") as archivo_json:
            datos = json.load(archivo_json)
            try:
                v = [x for x in datos if x['Usuario'] == usuario]
                if len(v) == 0:
                    print("No existe ese usuario")
                else:
                    print(v)
            except:
                print("No existe registro")
    else:
        print("No existe el historial.json")     

def comprobar_existencia_usuario_json(nombre_usuario, contra):
    #Compara las listas
    if existe_historial_usuarios() == True:
        nose = {"Usuario": nombre_usuario, "Contra": contra}
        with open("users_data.json") as archivo_json:
            datos = json.load(archivo_json)
            while True:
                for elementos in datos:
                    for elementos2 in elementos.values():
                        ele1 = elementos2
                        for elementosnose in nose.values():
                            elenose1 = elementosnose
                    if ele1 == elenose1:
                        return True
                break    
    else:
        print("No existe el users_data.json")
        return False 

def iniciar_sesion():
    if existe_historial_usuarios() == True:
        while True:
            print("\nInicio de sesión, escribe tus datos a continuación")
            nombre_usuario= input("Nombre de usuario\n")
            contra = input("Contraseña\n")
            if comprobar_existencia_usuario_json(nombre_usuario, contra) == True:
                usuario.set_nombre(nombre_usuario)
                return True
            else:
                print("\nNo existe ese usuario y/o contraseña\n")   
    else:
        print("\nAun no existen cuentas, crea una.\n")
        return False
        
def creacion_usuario():
    while True:
        nombre_usuario = input("Escribe tu nombre\n")
        if len(nombre_usuario) == 0:
            print("El campo no puede estar vacío")
        else:    
            usuario.set_nombre(nombre_usuario)
            break
    while True:    
        contra_usuario  = input("Escribe tu contraseña\n")
        if len(contra_usuario) <= 4:
            print("El campo no puede estar vacío y tiene que ser mayor de 4 caracteres")
        elif contra_usuario == nombre_usuario:
            print("La contraseña no puede ser igual a tu nombre de usuario")
        else:
            usuario.set_contra(contra_usuario)
            break
    usuario.set_id(asignar_id_usuario())   
    agregar_cuenta_json(usuario.get_nombre(), usuario.get_contra())

def sbr_preguntas():
    
    engine.reset()
    preguntas = []
    respuestas = []
    pj85_pregunta = "Tu personaje es nivel 85"
    pjilvl_pregunta = "Tu nivel de objeto es de 300 o 299"
    pjjusticia_pregunta = "Cuantos puntos de justicia tienes 2000 o 1999"
    pj_elites_pregunta = "Haz completado la arena de Elites de Tierras Altas Crepusculares"
    pjguild_pregunta = "Estas en una hermandad nivel 25"

    while True: #pj85_pregunta
        print(pj85_pregunta)
        pj85_respuesta = input()    
        if validar_campo_texto(pj85_respuesta) == True:
            preguntas.append(pj85_pregunta)
            respuestas.append(pj85_respuesta)
            engine.declare(reglas(pj_level=choice([str(pj85_respuesta.upper())])))
            break
        
    while True: #pjilvl_pregunta
        try:
            print(pjilvl_pregunta)
            pjilvl_respuesta = int(input())
            if pjilvl_respuesta <= 298 or pjilvl_respuesta >= 301:
                print("Digita 299 ó 300")
            else:
                preguntas.append(pjilvl_pregunta)
                engine.declare(reglas(pj_ilvl=choice([pjilvl_respuesta])))    
                break    
        except ValueError:
            print("Tienes que digitar una de las opciones listadas") 
              
    while True: #pjjusticia_pregunta
        try:
            print(pjjusticia_pregunta)
            pjjusticia_respuesta = int(input())
            if pjjusticia_respuesta <= 1998 or pjjusticia_respuesta >= 2001:
                print("Digita 1999 ó 2000")
            else:
                preguntas.append(pjjusticia_pregunta)
                respuestas.append(pjjusticia_respuesta)
                engine.declare(reglas(pj_justicia=choice([pjjusticia_respuesta])))    
                break
        except ValueError:
            print("Tienes que digitar una de las opciones listadas")   
            
    while True: #pj_elites_pregunta
        print(pj_elites_pregunta)
        pj_elites_respuesta = input()    
        if validar_campo_texto(pj_elites_respuesta) == True:
            preguntas.append(pj_elites_pregunta)
            respuestas.append(pj_elites_respuesta)
            engine.declare(reglas(pj_elites=choice([str(pj_elites_respuesta.upper())])))
            break 
    
    while True: #pjguild_pregunta
        print(pjguild_pregunta)
        pjguild_respuesta = input()    
        if validar_campo_texto(pjguild_respuesta) == True:
            preguntas.append(pjguild_pregunta)
            respuestas.append(pjguild_respuesta)
            engine.declare(reglas(pj_guild=choice([str(pjguild_respuesta.upper())])))
            break           
    engine.run() 
       
    return preguntas, respuestas

def validar_campo_texto(opc):
    lista_si = ['si','sí','Si','Sí','sI', 'SI', 'SÍ','sÍ']
    lista_no = ['no','nó','No','Nó','nO', 'NO', 'NÓ','nÓ']
    
    if opc.isnumeric():
        print("Tienes que escribir texto")
    elif opc in lista_si or opc in lista_no:
        return True
    else:
        print("Tienes que escribir una de las opciones listadas Si o No")
        return False
    
def menu_principal():    
    while True:
        try:
            opc_menu = int(input("1. Iniciar sistemas basados en reglas\n2. Consultar historial\n3. Salir\n"))
            if opc_menu == 1:
                print("sistemas basados en reglas")
                preguntas, respuestas = sbr_preguntas()
                agregar_datos_generales_json(usuario.get_nombre(), usuario.get_id(), preguntas, respuestas)
                
            elif opc_menu == 2:
                while True:
                    try:
                        opcsub_menu = int(input("1. Consulta por id\n2. Consulta por usuario\n3. Retroceder\n"))
                        if opcsub_menu == 1:
                            mostrar_json_id(id = int(input("¿Número de id a buscar?\n")))
                        elif opcsub_menu == 2:
                            mostrar_json_usuario(usuario = input("¿Nombre de usuario?\n"))
                        elif opcsub_menu == 3:
                            break
                    except ValueError as e:
                        print("Tienes que digitar la opción")
                    
            elif opc_menu == 3:
                break
            else:
                print("Esa opción no existe")   
        except ValueError:
            print("Tienes que digitar la opción")
            
def inicio():
    while True:
        try:
            opc = int(input("1. Iniciar sesión\n2. Crear usuario\n3. Salir\n"))
            if opc == 1:
                if iniciar_sesion() == True:
                    menu_principal()
            elif opc == 2:
                creacion_usuario()
            elif opc == 3:
                exit()   
            else:
                print("Esa opcion no existe")    
        except ValueError as e:
            print("Tienes que digitar la opción")    
            
if __name__ == "__main__":
    inicio()