import json
from usuario import Usuario

#Función para procesar los usuarios en el archivo usuario.txt y captar errores
def procesar_usuarios(usuario.txt, error.log):
    usuarios = [] #Se crea esta lista vacía para almacenar los datos de los usuarios

#Abre el archivo em modo leer
    with open(usuario.txt, "r") as archivo:
        for linea in archivo:   #Lee el archivo línea por línea
            
            try:
                datos_usuario = json.loads(linea.strip())

                #Condición que verifica si estás todos los campos presentes
                if not all(key in datos_usuario for key in ("nombre", "apellido", "email", "genero")):
                    raise ValueError("Faltan campos en los datos del usuario")
                #Crear instancia de la clase Usuario, usando los datos extraídos
                usuario = Usuario(
                    nombre=datos_usuario["nombre"],
                    apellido=datos_usuario["apellido"],
                    email=datos_usuario["email"],
                    genero=datos_usuario["genero"]
                )
                #Añadir usuario a la lista de usuarios
                usuarios.append(usuario)
            
            except json.JSONDecodeError as e:
                #Si hay un error con el formato JSON, registra el error en el archo log.
                with open(error.log, "a") as log:
                    log.write(f"Error de formato JSON en la línea: {linea.strip()} - {str(e)}\n")
            except ValueError as e:
                #Si faltan campos en la línea, registrar el error en el archivo log
                with open(error.log, "a")as log:
                    log.write(f"Datos inválidos en la línea: {linea.strip()} - {str(e)}\n")
             except Exception as e:
                #Cualqueir otro error inesperado registrar error en el archivo log
                with open(error.log, "a")as log:
                    log.write(f"Error inesperado al procesar la línea: {linea.strip()} - {str(e)}\n")
    #Retornar la lista de usuarios procesados de manera correcta
    return usuarios            