import unittest
from libreria import Libreria

class TestLibreria(unittest.TestCase):

    def setUp(self):
        self.libreria = Libreria()

    def test_anadir_libro(self):
        result = self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(result, "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 1)
        self.assertEqual(self.libreria.libros[0]['titulo'], "Cien años de soledad")

    def test_buscar_por_autor(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        result = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['titulo'], "Cien años de soledad")

    def test_modificar_libro(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        result = self.libreria.modificar_libro("Cien años de soledad", nuevo_titulo="Cien años de soledad (Edición Especial)")
        self.assertEqual(result, "Libro modificado")
        self.assertEqual(self.libreria.libros[0]['titulo'], "Cien años de soledad (Edición Especial)")

    def test_eliminar_libro(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        result = self.libreria.eliminar_libro("Cien años de soledad")
        self.assertEqual(result, "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 0)

    def test_guardar_y_cargar_libros(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.guardar_libros('test_libreria.json')
        self.libreria.libros = []  # Vaciar la lista para probar la carga
        result = self.libreria.cargar_libros('test_libreria.json')
        self.assertEqual(result, "Libros cargados")
        self.assertEqual(len(self.libreria.libros), 1)
        self.assertEqual(self.libreria.libros[0]['titulo'], "Cien años de soledad")

if __name__ == '__main__':
    unittest.main()
