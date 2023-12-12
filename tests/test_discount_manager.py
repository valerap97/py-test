import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)
from main import ComicBook, ComicShop, DiscountManager
from exceptions import ComicNotFoundError, DuplicateISBNError, InvalidDiscountError

class TestComicShopIntegration(unittest.TestCase):
    def setUp(self):
        self.shop = ComicShop("Comic Book Store")
        self.comic = ComicBook("Spider-Man", "Stan Lee", "88888", 12.99, 5)
        self.shop.add_comic(self.comic)
        self.discount_manager = DiscountManager(self.shop)

    def test_add_and_get_comic(self):
        found_comic = self.shop.get_comics_by_isbn("88888")[0]
        self.assertEqual(found_comic, self.comic)

    def test_duplicate_isbn(self):
        with self.assertRaises(DuplicateISBNError):
            self.shop.add_comic(self.comic)

    def test_discount(self):
        self.discount_manager.define_discount("88888", 10)
        updated_comic = self.shop.get_comics_by_isbn("88888")[0]
        self.assertAlmostEqual(updated_comic.price, 11.69, places=2)

# запустить тесты
if __name__ == '__main__':
    unittest.main()
