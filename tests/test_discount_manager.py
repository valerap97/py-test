import unittest
import os
import sys
import io

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
        
    def test_apply_discount_to_nonexistent_isbn(self):
        with self.assertRaises(ComicNotFoundError):
            self.discount_manager.apply_discount_to_isbn("99999", 10)

    def test_define_invalid_discount(self):
        with self.assertRaises(InvalidDiscountError):
            self.discount_manager.define_discount("88888", -10)  # Недопустимый процент скидки
        with self.assertRaises(InvalidDiscountError):
            self.discount_manager.define_discount("88888", 150)  # Превышение 100%

    def test_display_no_discounts(self):
        # Предполагается, что в DiscountManager нет скидок,
        # можно очистить словарь для уверенности.
        self.discount_manager.discounts = {}
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.discount_manager.display_discounts()
            self.assertEqual(mock_stdout.getvalue().strip(), "Скидок нет!")

    def test_display_discounts(self):
        # Прежде чем проверить вывод, необходимо обеспечить, что скидки уже определены.
        self.discount_manager.define_discount("88888", 10)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.discount_manager.display_discounts()
            self.assertIn("Комикс 'Spider-Man': 10% скидка.", mock_stdout.getvalue().strip())

# запустить тесты
if __name__ == '__main__':
    unittest.main()
