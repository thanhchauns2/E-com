import random, json
from .models import Cart
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def __create_cart(user_id):
    id = random.randint(100000000, 99999999999999)
    new_cart = Cart(id=id, user_id=user_id)
    new_cart.save()
    return new_cart.id

@csrf_exempt
def create_cart(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            
            user_id = val1.get("User ID")
            
            if user_id:
                respdata = __create_cart(user_id)
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Added cart.'
                resp['data'] = {'cart_id': respdata}
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
