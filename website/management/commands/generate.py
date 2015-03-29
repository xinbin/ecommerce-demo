from django.core.management.base import BaseCommand, CommandError
from ecommerce.models import Product, Category
from blog.models import Article
import random
from faker import Factory

class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    help = 'Generates sample data for the website'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Article.objects.all().delete()

        product_images = list()
        article_images = list()
        for i in range(1, 5):
            image = {
                "small_image": "/static/images/products/image%s_320x150.jpg" % i,
                "large_image": "/static/images/products/image%s_800x300.jpg" % i,
            }
            product_images.append(image)
            image = {
                "image": "/static/images/articles/image%s_900x300.jpg" % i,
            }
            article_images.append(image)


        fake = Factory.create()
        self.stdout.write('Generating sample website')
        self.stdout.write('Adding Categories')

        categories = list()
        for _ in range(5):
            item = {
                "name": "%s %s" % (fake.color_name(), fake.word()),
                "description": fake.paragraph(),
                "carousel": fake.boolean()
            }
            category = Category(**item)
            category.save()
            categories.append(category)
        self.stdout.write('Adding Products')

        for _ in range(20):
            image = random.choice(product_images)
            item = {
                "category": random.choice(categories),
                "name": "%s %s" % (fake.color_name(), fake.word()),
                "description": fake.paragraph(),
                "special": fake.boolean(),
                "featured": fake.boolean(),
                "price": random.randint(5, 50),
                "small_image": image['small_image'],
                "large_image": image['large_image'],
                }
            product = Product(**item)
            product.save()
        self.stdout.write('Adding Articles')
        for _ in range(10):
            image = random.choice(article_images)
            item = {
                "title": "%s %s" % (fake.color_name(), fake.word()),
                "body": " ".join(fake.paragraphs(nb=5)),
                "lead": fake.paragraph(),
                "author": fake.name(),
                "img": image['image']
            }
            article = Article(**item)
            article.save()



