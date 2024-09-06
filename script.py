import json
from usuario import Usuario

#Función para procesar los usuarios en el archivo usuario.txt y captar errores
def procesar_usuarios(ruta_archivo = "usuarios.txt", archivo_log = "error.log"):
    """
    Procesa un archivo de usuarios en formato JSON, crea instancias de la clase `Usuario` 
    y registra los errores en un archivo de log.

    Lee el archivo especificado por `ruta_archivo` línea por línea, tratando de interpretar 
    cada línea como un objeto JSON que representa un usuario. Si se encuentra un error de formato 
    JSON o datos inválidos, se registra un mensaje de error en el archivo de log especificado por 
    `archivo_log`. Los usuarios válidos se almacenan en una lista que se devuelve al final.

    Parámetros
    ----------
    ruta_archivo : str, opcional
        Ruta al archivo de entrada que contiene los datos de los usuarios en formato JSON. 
        El valor predeterminado es "usuarios.txt".
    archivo_log : str, opcional
        Ruta al archivo de log donde se registrarán los errores encontrados durante el procesamiento. 
        El valor predeterminado es "error.log".

    Retorna
    -------
    list
        Una lista de instancias de `Usuario` creadas a partir de las líneas válidas del archivo de entrada.
    """
    usuarios = [] #Se crea esta lista vacía para almacenar los datos de los usuarios

    #Método .close, sirve para cerrar el archivo y vaciarlo. Así mo hay repeticiñon en el registro de un mismo error.
    open(archivo_log,"w").close

    #Abre el archivo em modo leer
    with open(ruta_archivo, "r") as archivo:
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
                with open(archivo_log, "a") as log:
                    log.write(f"Error de formato JSON en la linea: {linea.strip()} - {str(e)}\n")
            except ValueError as e:
                #Si faltan campos en la línea, registrar el error en el archivo log
                with open(archivo_log, "a")as log:
                    log.write(f"Datos inválidos en la linea: {linea.strip()} - {str(e)}\n")
            except Exception as e:
                #Cualqueir otro error inesperado registrar error en el archivo log
                with open(archivo_log, "a")as log:
                    log.write(f"Error inesperado al procesar la linea: {linea.strip()} - {str(e)}\n")
    #Retornar la lista de usuarios procesados de manera correcta
    return usuarios

usuarios = procesar_usuarios()

#Mostrar el número de usuarios que se procesaron correctamente
print(f"Se procesaron correctamente {len(usuarios)} usuarios")
