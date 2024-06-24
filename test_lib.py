import unittest
import os
from lib import *

class TestLib(unittest.TestCase):

    def setUp(self):
        # Limpia los archivos antes de cada test
        clear_ingresos()
        clear_gastos()

    def tearDown(self):
        # Limpia los archivos después de cada test
        clear_ingresos()
        clear_gastos()

    def test_crear_nuevo_ingreso(self):
        crear_nuevo_ingreso("1", "Mateo", 1000)
        self.assertTrue(os.path.exists(file_in))
        with open(file_in, "r") as f:
            content = f.read().strip()
            self.assertEqual(content, "1-Mateo-1000")

    def test_crear_nuevo_egreso(self):
        crear_nuevo_egreso("1", "Mateo", 1000)
        self.assertTrue(os.path.exists(file_out))
        with open(file_out, "r") as f:
            content = f.read().strip()
            self.assertEqual(content, "1-Mateo-1000")

    def test_ingresos(self):
        crear_nuevo_ingreso("1", "Mateo", 1000)
        result = ingresos()
        self.assertIn("Mateo", result)
        self.assertEqual(result["Mateo"], [("1", "Mateo", "1000")])

    def test_gastos(self):
        crear_nuevo_egreso("1", "Mateo", 1000)
        result = gastos()
        self.assertIn("Mateo", result)
        self.assertEqual(result["Mateo"], [("1", "Mateo", "1000")])

    def test_clear_ingresos(self):
        crear_nuevo_ingreso("1", "Mateo", 1000)
        clear_ingresos()
        result = ingresos()
        self.assertEqual(result, {})

    def test_clear_gastos(self):
        crear_nuevo_egreso("1", "Mateo", 1000)
        clear_gastos()
        result = gastos()
        self.assertEqual(result, {})

    def test_empty_ingresos(self):
        result = ingresos()
        self.assertEqual(result, {})

    def test_empty_gastos(self):
        result = gastos()
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
