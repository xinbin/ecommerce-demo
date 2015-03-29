from django.test import TestCase
from django.test import Client
from django.conf import settings
from ecommerce.models import Product, Category
import json


class ArticlesApiTest(TestCase):

    def test_products(self):
        headers = {
            "HTTP_X_AUTH_TOKEN": settings.AUTH_TOKEN
        }

        c = Client()
        article = {
            'title': 'Category Name',
            'lead': 'Some lead',
            'author': 'Brady Vitrano'
        }
        response = c.post('/v1/articles/', article, **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)
        response = c.get('/v1/articles/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)
        response = c.get('/v1/articles/1/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)

        response = c.put('/v1/articles/1/',
                         json.dumps({'title': 'Update'}),
                         content_type='application/json', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 202)

        response = c.get('/v1/articles/1/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 200)

        # create article with json body
        response = c.post('/v1/articles/', data=json.dumps(article),
                          content_type='application/json',
                          **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 201)

        response = c.delete('/v1/articles/2/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 202)

        response = c.get('/v1/articles/2/', **headers)
        self.assertEquals(response['Content-Type'], 'application/json')
        self.assertEquals(response.status_code, 404)

