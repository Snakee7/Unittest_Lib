import unittest
import Model

class TestModel(unittest.TestCase):
    def test_getAlbumsSQL(self):
        self.model = Model.Model()
        test = self.model.getAlbumsSQL()
        self.assertIn('Barcelona', test)


if __name__ == '__main__':
    unittest.main()