from django.test import TestCase

from restaurant.views import MenuItemsView

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItemsView.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")