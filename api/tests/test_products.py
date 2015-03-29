from django.test import TestCase
from django.test import Client
from django.conf import settings
from ecommerce.models import Product, Category
import json


class ProductsApiTest(TestCase):

    def test_products(self):
        headers = {
            "HTTP_X_AUTH_TOKEN": settings.AUTH_TOKEN
        }
        c = Client()
        category = {
            'name': 'Category Name',
            'description': 'Description name'
        }
        # create category with url encoded body
        response = c.post('/v1/categories/', category, **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)

        response = c.get('/v1/categories/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)

        response = c.get('/v1/categories/1/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)

        # create category with json body
        response = c.post('/v1/categories/',
                          data=json.dumps(category),
                          content_type='application/json',
                          **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)

        response = c.get('/v1/categories/2/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)

        response = c.put('/v1/categories/1/',
                         data=json.dumps({'name': 'Update'}),
                         content_type='application/json',
                         **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 202)

        response = c.get('/v1/categories/1/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)

        response = c.delete('/v1/categories/2/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 202)


        product = {
            "category_id": "1",
            "name": "Product Name",
            "description": "Product Description",
            "price": "12.00",
            "small_image": "/some/path/to/image.png",
            "large_image": "/some/path/to/image.png",
            "special": True,
            "featured": True,
            "status": Product.ACTIVE
        }

        # Create product with url encoded body
        response = c.post('/v1/products/', product, **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)
        del(product['price'])

        # create product with json body
        response = c.post('/v1/products/', data=json.dumps(product),
                          content_type='application/json',
                          **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)

        response = c.get('/v1/products/2/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)

        response = c.delete('/v1/products/1/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 202)

        # verify 404 for deleted product
        response = c.get('/v1/products/1/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 404)

        response = c.post('/v1/products/', product, **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)

        response = c.post('/v1/products/', product, **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)

        response = c.get('/v1/products/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)
