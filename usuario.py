class Usuario():
    """
    Representa un usuario con información básica.

    Esta clase se utiliza para almacenar los detalles de un usuario, incluyendo 
    el nombre, apellido, email y género.

    Parámetros
    ----------
    nombre : str
        El nombre del usuario.
    apellido : str
        El apellido del usuario.
    email : str
        La dirección de correo electrónico del usuario.
    genero : str
        El género del usuario.
    """
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero


    