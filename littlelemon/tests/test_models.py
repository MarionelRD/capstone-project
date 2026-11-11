from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):

    def test_get_items(self):
        item = MenuItem.objects.create(id=10,title='Pizza', price=10.99, inventory=5)
        self.assertEqual(str(item), 'Pizza: 10.99')