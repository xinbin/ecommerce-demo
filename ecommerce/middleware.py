

class EcommerceMiddleware(object):

    def process_request(self, request):
        if 'cart' not in request.session:
            request.session['cart'] = dict()
