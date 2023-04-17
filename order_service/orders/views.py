import random, json, requests
from .models import Order
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# - Thêm một hoá đơn
# - Cập nhật trạng thái hoá đơn

def __create_order(user_id, description, status):
    id = random.randint(100000000, 99999999999999)
    new_order = Order(id=id, user_id=user_id, description = description, status=status)
    new_order.save()
    return id

@csrf_exempt
def create_order(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            
            user_id = val1.get("User ID")
            # description = val1.get("Description")
            description = requests.post('http://127.0.0.1:5000/carts/show_cart/', json={"User ID": user_id}).json()
            status = "Delivering"
            
            if user_id:
                respdata = __create_order(user_id, description, status)
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Added order.'
                resp['data'] = {'order': respdata}
                requests.post('http://127.0.0.1:5000/carts/clear_cart/', json={"User ID": user_id}).json()
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

def __get_order(order_id):
    orders = Order.objects.all()
    for order in orders:
        if order.id == order_id:
            return order
    
    return None

@csrf_exempt
def update_order(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            
            order_id = val1.get("Order ID")
            
            order = __get_order(order_id)
            
            if order != None: # Giỏ hàng không thể bị thay đổi
                stat = val1.get("Status")
                order.status = stat
                order.save()

                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Status updated succesfully.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Cannot find object.'
    return HttpResponse(json.dumps(resp), content_type='application/json')