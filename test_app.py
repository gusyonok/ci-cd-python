import unittest
from unittest.mock import patch, MagicMock
from app import app, Products, Product

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_products(self):
        with patch('app.ProductModel.select') as mock_select:
            mock_select.return_value = [MagicMock(to_dict=lambda: {'id': 1, 'name': 'Test Product', 'price': 10.0})]
            response = self.app.get('/api/products')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [{'id': 1, 'name': 'Test Product', 'price': 10.0}])

    def test_create_product(self):
        with patch('app.create_product') as mock_create:
            mock_create.return_value = MagicMock(id=1)
            response = self.app.post('/api/products', json={'name': 'Test Product', 'price': 10.0})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, {'message': 'Product added successfully.', 'productId': 1})

    # Write similar test methods for other endpoints (GET /api/products/<id>, PATCH /api/products/<id>, DELETE /api/products/<id>)

if __name__ == '__main__':
    unittest.main()
