import json


class Libreria:
    """Sistema de gestión de librería virtual."""

    def __init__(self):
        """Inicializa una lista vacía de libros."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la colección.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.

        Returns:
            str: Mensaje confirmando que el libro ha sido añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            list: Lista de libros que coinciden con el título buscado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por el nombre del autor.

        Args:
            autor (str): El nombre del autor a buscar.

        Returns:
            list: Lista de libros que coinciden con el autor buscado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def modificar_libro(self, titulo, nuevo_titulo=None, nuevo_autor=None, nuevo_genero=None, nuevo_anio=None):
        """
        Modifica la información de un libro existente.

        Args:
            titulo (str): El título del libro a modificar.
            nuevo_titulo (str, optional): El nuevo título del libro.
            nuevo_autor (str, optional): El nuevo autor del libro.
            nuevo_genero (str, optional): El nuevo género del libro.
            nuevo_anio (int, optional): El nuevo año de publicación del libro.

        Returns:
            str: Mensaje indicando si el libro fue modificado o no encontrado.
        """
        for libro in self.libros:
            if libro['titulo'].lower() == titulo.lower():
                if nuevo_titulo:
                    libro['titulo'] = nuevo_titulo
                if nuevo_autor:
                    libro['autor'] = nuevo_autor
                if nuevo_genero:
                    libro['genero'] = nuevo_genero
                if nuevo_anio:
                    libro['anio'] = nuevo_anio
                return "Libro modificado"
        return "Libro no encontrado"

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por su título.

        Args:
            titulo (str): El título del libro a eliminar.

        Returns:
            str: Mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la colección de libros en un archivo JSON.

        Args:
            archivo (str): El nombre del archivo donde se guardarán los libros.

        Returns:
            str: Mensaje confirmando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la colección de libros desde un archivo JSON.

        Args:
            archivo (str): El nombre del archivo desde el cual se cargarán los libros.

        Returns:
            str: Mensaje indicando si los libros fueron cargados o si el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


# Ejemplo de uso
if __name__ == "__main__":
    mi_libreria = Libreria()
    mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
    mi_libreria.guardar_libros('libreria.json')
    print(mi_libreria.cargar_libros('libreria.json'))
    print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))
