import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)
from exceptions import NegativeInventoryError, DuplicateISBNError, ComicNotFoundError, ComicNotInStockError
from main import ComicBook, ComicShop

class TestComicBook(unittest.TestCase):
    
    def test_comic_creation(self):
        comic = ComicBook("Batman", "Bob Kane", "12345", 9.99, 10)
        self.assertEqual(comic.title, "Batman")
        self.assertEqual(comic.author, "Bob Kane")
        self.assertEqual(comic.isbn, "12345")
        self.assertEqual(comic.price, 9.99)
        self.assertEqual(comic.inventory_count, 10)

    def test_negative_inventory_error(self):
        with self.assertRaises(NegativeInventoryError):
            ComicBook("Batman", "Bob Kane", "12345", 9.99, -5)

    def test_update_inventory(self):
        comic = ComicBook("Batman", "Bob Kane", "12345", 9.99, 10)
        comic.update_inventory(15)
        self.assertEqual(comic.inventory_count, 15)
        
    def setUp(self):
        self.shop = ComicShop("Comics R Us")

        # Создаем несколько комиксов для тестирования
        self.sample_comic = ComicBook("Superman", "Jerry Siegel", "12345", 5.99, 5)
        self.sample_comic2 = ComicBook("Batman", "Bob Kane", "67890", 7.99, 5)

        # Добавляем комикс в магазин
        self.shop.add_comic(self.sample_comic)

    def test_duplicate_isbn_error(self):
        with self.assertRaises(DuplicateISBNError):
            self.shop.add_comic(self.sample_comic)

    def test_comic_not_found_by_title_error(self):
        with self.assertRaises(ComicNotFoundError):
            self.shop.get_comics_by_title("Nonexistent Title")

    def test_comic_not_found_by_author_error(self):
        with self.assertRaises(ComicNotFoundError):
            self.shop.get_comics_by_author("Nonexistent Author")

    def test_comic_not_found_by_isbn_error(self):
        with self.assertRaises(ComicNotFoundError):
            self.shop.get_comics_by_isbn("00000")

    def test_not_in_stock_error(self):
        with self.assertRaises(ComicNotInStockError):
            self.sample_comic.inventory_count = 0
            self.shop.sell_comic(self.sample_comic)

    def test_remove_comic(self):
        self.shop.remove_comic(self.sample_comic)
        with self.assertRaises(ComicNotFoundError):
            self.shop.get_comics_by_isbn(self.sample_comic.isbn)

    def test_edit_comic_info_not_found_error(self):
        with self.assertRaises(ComicNotFoundError):
            self.shop.edit_comic_info(self.sample_comic2)
            
    def test_edit_comic_info(self):
        new_title = "Superman: Earth One"
        new_author = "J. Michael Straczynski"
        new_price = 10.99
        self.shop.edit_comic_info(self.sample_comic, title=new_title, author=new_author, price=new_price)
        self.assertEqual(self.sample_comic.title, new_title)
        self.assertEqual(self.sample_comic.author, new_author)
        self.assertEqual(self.sample_comic.price, new_price)

# запустить тесты
if __name__ == '__main__':
    unittest.main()
