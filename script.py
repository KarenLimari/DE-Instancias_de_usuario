import json
from usuario import Usuario

#Función para leer el archivo usuario.txt
def leer_archivo(usuario.txt, error.log):
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
            
            except