import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)
from exceptions import NegativeInventoryError
from main import ComicBook

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

# запустить тесты
if __name__ == '__main__':
    unittest.main()
