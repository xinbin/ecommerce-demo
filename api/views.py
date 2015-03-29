from django.http import HttpResponse
from django.http import QueryDict
from ecommerce.models import Product, Category
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from api.decorators import token_required
from blog.models import Article
import json


@csrf_exempt
@token_required
def products(request):
    def on_post(request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            try:
                data = json.loads(request.body)
            except ValueError:
                return {'message': 'Invalid json body'}, 400
        else:
            try:
                raw_data = request.POST
                data = {
                    'category_id': raw_data.get('category_id'),
                    'name': raw_data.get('name'),
                    'description': raw_data.get('description'),
                    'status': raw_data.get('status'),
                    'featured': raw_data.get('featured'),
                    'special': raw_data.get('special'),
                    'image': raw_data.get('image'),
                    'price': raw_data.get('price'),
                }
            except Exception as e:
                return {'message': 'Invalid product request'}, 400
        data = {k: v for k, v in data.items() if v}
        try:
            category = Category.objects.get(id=data.get('category_id'))
        except Category.DoesNotExist:
            return {'message': 'Invalid category id'}, 400
        del(data['category_id'])
        data['category'] = category
        product = Product(**data)
        try:
            product.save()
        except:
            return {'message': 'Invalid product request'}, 400
        return model_to_dict(product), 201

    def on_get(request):
        products = Product.objects.all()
        payload = [model_to_dict(product) for product in products]
        return payload, 200

    if request.method == 'POST':
        payload, status = on_post(request)
    elif request.method == 'GET':
        payload, status = on_get(request)
    else:
        payload = {'message': 'Method not allowed'}
        status = 400

    return HttpResponse(json.dumps(payload),
                        status=status,
                        content_type="application/json")


@csrf_exempt
@token_required
def product(request, cid):
    def on_put(request, cid):

        if request.META['CONTENT_TYPE'] == 'application/json':
            try:
                data = json.loads(request.body)
            except ValueError:
                return {'message': 'Invalid json body'}, 400
        else:
            try:
                raw_data = QueryDict(request.body)
                data = {
                    'name': raw_data.get('name'),
                    'description': raw_data.get('description')
                }
            except:
                return {'message': 'Invalid product request'}, 400
        data = {k: v for k, v in data.items() if v}
        try:
            Product.objects.filter(id=cid).update(**data)
            product = Product.objects.get(id=cid)
        except:
            return {'message': 'Invalid product request'}, 400
        return model_to_dict(product), 202

    def on_get(request, cid):
        try:
            product = Product.objects.get(id=cid)
        except Product.DoesNotExist:
            return {'message': 'Product not found'}, 404
        return model_to_dict(product), 200

    def on_delete(request, cid):
        try:
            product = Product.objects.get(id=cid)
            product.delete()
        except Product.DoesNotExist:
            return {'message': 'Product not found'}, 404
        return {"message": "Product removed"}, 202

    if request.method == 'PUT':
        payload, status = on_put(request, cid)
    elif request.method == 'GET':
        payload, status = on_get(request, cid)
    elif request.method == 'DELETE':
        payload, status = on_delete(request, cid)
    else:
        payload = {'message': 'Method not allowed'}
        status = 400

    return HttpResponse(json.dumps(payload),
                        status=status,
                        content_type="application/json")


@csrf_exempt
@token_required
def categories(request):
    def on_post(request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            try:
                data = json.loads(request.body)
            except ValueError:
                return {'message': 'Invalid json body'}, 400
        else:
            try:
                raw_data = request.POST
                data = {
                    'name': raw_data.get('name'),
                    'description': raw_data.get('description')
                }
            except Exception as e:
                return {'message': 'Invalid product request'}, 400

        data = {k: v for k, v in data.items() if v}
        category = Category(**data)
        try:
            category.save()
        except:
            return {'message': 'Invalid category request'}, 400
        return model_to_dict(category), 201

    def on_get(request):
        categories = Category.objects.all()
        payload = [model_to_dict(category) for category in categories]
        return payload, 200

    if request.method == 'POST':
        payload, status = on_post(request)
    elif request.method == 'GET':
        payload, status = on_get(request)
    else:
        payload = {'message': 'Method not allowed'}
        status = 400

    return HttpResponse(json.dumps(payload),
                        status=status,
                        content_type="application/json")

@csrf_exempt
@token_required
def category(request, cid):
    def on_put(request, cid):

        if request.META['CONTENT_TYPE'] == 'application/json':
            try:
                data = json.loads(request.body)
            except ValueError:
                return {'message': 'Invalid json body'}, 400
        else:
            try:
                raw_data = QueryDict(request.body)
                data = {
                    'name': raw_data.get('name'),
                    'description': raw_data.get('description')
                }
            except:
                return {'message': 'Invalid category request'}, 400

        data = {k: v for k, v in data.items() if v}
        try:
            Category.objects.filter(id=cid).update(**data)
            category = Category.objects.get(id=cid)
        except:
            return {'message': 'Invalid category request'}, 400
        return model_to_dict(category), 202

    def on_get(request, cid):
        try:
            category = Category.objects.get(id=cid)
        except Category.DoesNotExist:
            return {'message': 'Category not found'}, 404
        return model_to_dict(category), 200

    def on_delete(request, cid):
        try:
            category = Category.objects.get(id=cid)
            category.delete()
        except Category.DoesNotExist:
            return {'message': 'Category not found'}, 404
        return {"message": "Category removed"}, 202

    if request.method == 'PUT':
        payload, status = on_put(request, cid)
    elif request.method == 'GET':
        payload, status = on_get(request, cid)
    elif request.method == 'DELETE':
        payload, status = on_delete(request, cid)
    else:
        payload = {'message': 'Method not allowed'}
        status = 400

    return HttpResponse(json.dumps(payload),
                        status=status,
                        content_type="application/json")

@csrf_exempt
@token_required
def articles(request):
    def on_post(request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            try:
                data = json.loads(request.body)
            except ValueError:
                return {'message': 'Invalid json body'}, 400
        else:
            try:
                raw_data = request.POST
                data = {
                    'title': raw_data.get('title'),
                    'lead': raw_data.get('lead'),
                    'body': raw_data.get('body'),
                    'author': raw_data.get('author'),
                    'img': raw_data.get('image'),
                    'status': raw_data.get('status'),
                }
            except Exception as e:
                return {'message': 'Invalid product request'}, 400

        data = {k: v for k, v in data.items() if v}
        article = Article(**data)
        try:
            article.save()
        except:
            return {'message': 'Invalid blog request'}, 400
        return model_to_dict(article), 201

    def on_get(request):
        items = Article.objects.all()
        payload = [model_to_dict(item) for item in items]
        return payload, 200

    if request.method == 'POST':
        payload, status = on_post(request)
    elif request.method == 'GET':
        payload, status = on_get(request)
    else:
        payload = {'message': 'Method not allowed'}
        status = 400

    return HttpResponse(json.dumps(payload),
                        status=status,
                        content_type="application/json")

@csrf_exempt
@token_required
def article(request, cid):
    def on_put(request, cid):

        if request.META['CONTENT_TYPE'] == 'application/json':
            try:
                data = json.loads(request.body)
            except ValueError:
                return {'message': 'Invalid json body'}, 400
        else:
            try:
                raw_data = QueryDict(request.body)
                data = {
                    'title': raw_data.get('title'),
                    'lead': raw_data.get('lead'),
                    'body': raw_data.get('body'),
                    'author': raw_data.get('author'),
                    'img': raw_data.get('image'),
                    'status': raw_data.get('status'),
                }
                data = {k: v for k, v in data.items() if v}
            except:
                return {'message': 'Invalid category request'}, 400

        try:
            Article.objects.filter(id=cid).update(**data)
            item = Article.objects.get(id=cid)
        except:
            return {'message': 'Invalid article request'}, 400
        return model_to_dict(item), 202

    def on_get(request, cid):
        try:
            item = Article.objects.get(id=cid)
        except Article.DoesNotExist:
            return {'message': 'Article not found'}, 404
        return model_to_dict(item), 200

    def on_delete(request, cid):
        try:
            item = Article.objects.get(id=cid)
            item.delete()
        except Article.DoesNotExist:
            return {'message': 'Article not found'}, 404
        return {"message": "Article removed"}, 202

    if request.method == 'PUT':
        payload, status = on_put(request, cid)
    elif request.method == 'GET':
        payload, status = on_get(request, cid)
    elif request.method == 'DELETE':
        payload, status = on_delete(request, cid)
    else:
        payload = {'message': 'Method not allowed'}
        status = 400

    return HttpResponse(json.dumps(payload),
                        status=status,
                        content_type="application/json")