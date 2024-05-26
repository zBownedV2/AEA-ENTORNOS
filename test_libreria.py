import unittest
from libreria import Libreria

class TestLibreria(unittest.TestCase):

    def setUp(self):
        """Inicializa una librería para cada prueba."""
        self.libreria = Libreria()

    def test_anadir_libro(self):
        """Prueba añadir un libro a la librería."""
        resultado = self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(resultado, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 1)

    def test_buscar_libro(self):
        """Prueba buscar un libro por su título."""
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        resultado = self.libreria.buscar_libro("Cien años de soledad")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['autor'], "Gabriel García Márquez")

    def test_buscar_por_autor(self):
        """Prueba buscar libros por autor."""
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        resultado = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "Cien años de soledad")

    def test_modificar_libro(self):
        """Prueba modificar un libro existente."""
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        resultado = self.libreria.modificar_libro("Cien años de soledad", nuevo_titulo="Cien años")
        self.assertEqual(resultado, "Libro modificado")
        self.assertEqual(self.libreria.libros[0]['titulo'], "Cien años")

    def test_eliminar_libro(self):
        """Prueba eliminar un libro por su título."""
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        resultado = self.libreria.eliminar_libro("Cien años de soledad")
        self.assertEqual(resultado, "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 0)

    def test_guardar_y_cargar_libros(self):
        """Prueba guardar y cargar libros desde un archivo JSON."""
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.guardar_libros('test_libreria.json')
        nueva_libreria = Libreria()
        resultado = nueva_libreria.cargar_libros('test_libreria.json')
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(len(nueva_libreria.libros), 1)
        self.assertEqual(nueva_libreria.libros[0]['titulo'], "Cien años de soledad")

if __name__ == "__main__":
    unittest.main()
