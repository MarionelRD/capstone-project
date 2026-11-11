from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Crear instancias de prueba para MenuItem
        MenuItem.objects.create(id=10,title="Pizza", price=10.50, inventory=50)
        MenuItem.objects.create(id=11, title="Burger", price=8.00, inventory=30)
        self.client = APIClient()

    def test_get_all_menu_items(self):
        # Obtener todos los objetos MenuItem
        response = self.client.get('/api/menu-items/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        # Verificar que la respuesta sea igual a los datos serializados
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)