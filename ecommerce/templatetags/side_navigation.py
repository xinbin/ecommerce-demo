from django import template
from django.template import Context
from ecommerce.models import Category, Product

register = template.Library()


def get_categories(parser, token):
    return CategoriesNode()


class CategoriesNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        categories = Category.objects.all()
        t = template.loader.get_template('ecommerce/side-navigation.html')
        return t.render(Context({'categories': categories}, autoescape=context.autoescape))

register.tag('side_nav_categories', get_categories)