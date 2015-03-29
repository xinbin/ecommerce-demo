from django.shortcuts import render


def api(request):
    """
    {
            "id": "some-id",
            "method": "GET",
            "endpoint": "/v1/products",
            "description": "Some Description",
            "query_params": [
                {'name': 'foo-bar', 'description': 'description'}
            ],
            "request_headers": [
                {'name': 'foo-bar', 'description': 'description'}
            ],
            "response_headers": [
                {'name': 'foo-bar', 'description': 'description'}
            ],
            "status_codes": [
                {'code': '200', 'description': 'OK'}
            ],
            "example_request": "page/api/products/get_request.html"
        }
    :param request:
    :return:
    """
    apis = list()
    products = dict({
        'id': 'products',
        'title': 'Products',
        'description': 'Some description of products',
    })
    apis.append(products)
    products['endpoints'] = list([
        {
            "id": "products-get",
            "method": "GET",
            "endpoint": "/v1/products/",
            "description": "Fetch a list of all products.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '200', 'description': 'OK'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '400', 'description': 'Invalid request'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/products/get_response.html",
            "example_request": "page/api/products/get_request.html"
        },
        {
            "id": "products-post",
            "method": "POST",
            "endpoint": "/v1/products/",
            "description": "Create a new product in the catalog. You are required to have a valid category number.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '201', 'description': 'CREATED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/products/post_response.html",
            "example_request": "page/api/products/post_request.html"
        },
        {
            "id": "products-get-item",
            "method": "GET",
            "endpoint": "/v1/products/:id/",
            "description": "Fetch a list of all products.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '200', 'description': 'OK'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '400', 'description': 'Invalid request'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/products/get_item_response.html",
            "example_request": "page/api/products/get_item_request.html"
        },
        {
            "id": "products-put",
            "method": "PUT",
            "endpoint": "/v1/products/:id/",
            "description": "Edit an existing product in the catalog",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '202', 'description': 'ACCEPTED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/products/put_response.html",
            "example_request": "page/api/products/put_request.html"
        },
        {
            "id": "products-delete",
            "method": "DELETE",
            "endpoint": "/v1/products/:id/",
            "description": "Delete an existing product in the catalog",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '202', 'description': 'ACCEPTED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/products/delete_response.html",
            "example_request": "page/api/products/delete_request.html"
        }
    ])
    categories = dict({
        'id': 'categories',
        'title': 'Categories',
        'description': 'Managing product catalog'
    })
    apis.append(categories)
    categories['endpoints'] = list([
        {
            "id": "categories-get",
            "method": "GET",
            "endpoint": "/v1/categories/",
            "description": "Fetch a list of all categories.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '200', 'description': 'OK'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '400', 'description': 'Invalid request'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/categories/get_response.html",
            "example_request": "page/api/categories/get_request.html"
        },
        {
            "id": "categories-post",
            "method": "POST",
            "endpoint": "/v1/categories/",
            "description": "Create a new category in the catalog.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '201', 'description': 'CREATED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/categories/post_response.html",
            "example_request": "page/api/categories/post_request.html"
        },
        {
            "id": "categories-get-item",
            "method": "GET",
            "endpoint": "/v1/categories/:id/",
            "description": "Fetch a list of all categories.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '200', 'description': 'OK'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '400', 'description': 'Invalid request'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/categories/get_item_response.html",
            "example_request": "page/api/categories/get_item_request.html"
        },
        {
            "id": "categories-put",
            "method": "PUT",
            "endpoint": "/v1/categories/:id/",
            "description": "Edit an existing category in the catalog",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '202', 'description': 'ACCEPTED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/categories/put_response.html",
            "example_request": "page/api/categories/put_request.html"
        },
        {
            "id": "categories-delete",
            "method": "DELETE",
            "endpoint": "/v1/categories/:id/",
            "description": "Delete an existing category in the catalog",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '202', 'description': 'ACCEPTED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/categories/delete_response.html",
            "example_request": "page/api/categories/delete_request.html"
        }

    ])

    articles = dict({
        'id': 'articles',
        'title': 'Blog Articles',
        'description': 'Managing the blog'
    })
    apis.append(articles)
    articles['endpoints'] = list([
        {
            "id": "articles-get",
            "method": "GET",
            "endpoint": "/v1/articles/",
            "description": "Fetch a list of all articles.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '200', 'description': 'OK'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '400', 'description': 'Invalid request'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/articles/get_response.html",
            "example_request": "page/api/articles/get_request.html"
        },
        {
            "id": "articles-post",
            "method": "POST",
            "endpoint": "/v1/articles/",
            "description": "Create a new article in the blog.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '201', 'description': 'CREATED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/articles/post_response.html",
            "example_request": "page/api/articles/post_request.html"
        },
        {
            "id": "articles-get-item",
            "method": "GET",
            "endpoint": "/v1/articles/:id/",
            "description": "Fetch a list of all articles.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '200', 'description': 'OK'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '400', 'description': 'Invalid request'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/articles/get_item_response.html",
            "example_request": "page/api/articles/get_item_request.html"
        },
        {
            "id": "articles-put",
            "method": "PUT",
            "endpoint": "/v1/articles/:id/",
            "description": "Edit an existing article in the blog.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '202', 'description': 'ACCEPTED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/articles/put_response.html",
            "example_request": "page/api/articles/put_request.html"
        },
        {
            "id": "articles-delete",
            "method": "DELETE",
            "endpoint": "/v1/articles/:id/",
            "description": "Delete an existing article in the blog.",
            "request_headers": [
                {'name': 'X-Auth-Token', 'description': 'See settings.py for value'}
            ],
            "response_headers": [
                {'name': 'Content-Type', 'description': 'application/json'}
            ],
            "status_codes": [
                {'code': '202', 'description': 'ACCEPTED'},
                {'code': '301', 'description': 'requires trailing slash are you will be redirected to it'},
                {'code': '403', 'description': 'Forbidden. Missing Auth Token'}
            ],
            "example_response": "page/api/articles/delete_response.html",
            "example_request": "page/api/articles/delete_request.html"
        }

    ])
    return render(request, 'page/api.html', {'apis': apis})


def about(request):
    return render(request, 'page/about.html')