import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from comic_inventory import ComicShop, ComicBook # Импортируем классы ComicShop и ComicBook
from discount_manager import DiscountManager # Импортируем класс DiscountManager
from exceptions import (ComicNotFoundError, NegativeInventoryError, DuplicateISBNError, InvalidDiscountError, ComicNotInStockError)
class TestComicShopAcceptance(unittest.TestCase):
    
    def setUp(self):
        self.shop = ComicShop("Ultimate Comic Store")
        self.comic1 = ComicBook("X-Men", "Chris Claremont", "11111", 7.99, 3)
        self.shop.add_comic(self.comic1)

    def test_complete_user_flow(self):
        # Пользователь ищет комикс по названию
        found_comics = self.shop.get_comics_by_title("X-Men")
        self.assertEqual(len(found_comics), 1)

        # Пользователь добавляет скидку на комикс
        discount_manager = DiscountManager(self.shop)
        discount_manager.define_discount("11111", 25)
        comic_with_discount = self.shop.get_comics_by_isbn("11111")[0]
        self.assertAlmostEqual(comic_with_discount.price, 5.99, places=2)

        # Пользователь покупает комикс
        self.shop.sell_comic(comic_with_discount)
        self.assertEqual(comic_with_discount.inventory_count, 2)

# запустить тесты
if __name__ == '__main__':
    unittest.main()
