from django.test import TestCase
from .models import Laboratorio

# Create your tests here.
class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Esto se ejecuta una vez para toda la clase
        Laboratorio.objects.create(nombre="Laboratorio A", ciudad="Santiago", pais="Chile")

    def test_laboratorio_creation(self):
        laboratorio = Laboratorio.objects.get(id=1)

        self.assertEqual(laboratorio.nombre, "Laboratorio A")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")

    def test_string_representation(self):
        laboratorio = Laboratorio(nombre="Laboratorio B")
        self.assertEqual(str(laboratorio), laboratorio.nombre)
