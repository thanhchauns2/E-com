import random, json
from .models import Cart
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def __create_cart(user_id):
    id = random.randint(100000000, 99999999999999)
    new_cart = Cart(id=id, user_id=user_id, items={'summary' : 'your items will be here'})
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
                resp['data'] = {'Cart ID': respdata}
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

def find_item_in_cart(cart, product_id):
    items = cart.items
    for item in items:
        if item['product_id'] == product_id:
            return item['quantity']
    return 0


@csrf_exempt
def add_item_to_cart(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            user_id = data.get('User ID')
            product_id = data.get('Product ID')
            quantity = data.get('Quantity')

            # Tìm cart theo cart_id và user_id
            try:
                cart = Cart.objects.get(user_id=user_id)
            except Cart.DoesNotExist:
                return HttpResponse('Cart not found', status=404)

            quan = find_item_in_cart(cart=cart, product_id=product_id)
            if quan == 0: # Thêm sản phẩm mới vào danh sách items của cart
                items = cart.items
                items.append({'Product ID': product_id, 'Quantity': quantity})
                cart.items = items
                cart.save()
            else: # Chỉnh sửa số lượng
                for item in items:
                    if item['Product ID'] == product_id:
                        item['Quantity'] = item['Quantity'] + quantity

            # Trả về thông tin của cart đã được cập nhật
            response_data = {'Cart ID': cart.cart_id, 'User ID': cart.user_id, 'Items': cart.items}
            return HttpResponse(json.dumps(response_data), content_type='application/json')

    return HttpResponse('Invalid request', status=400)

@csrf_exempt
def show_cart(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            user_id = data.get('User ID')

            # Tìm cart theo cart_id và user_id
            try:
                cart = Cart.objects.get(user_id=user_id)
            except Cart.DoesNotExist:
                return HttpResponse('Cart not found', status=404)
            
            items = cart.items
            response_data = []
            for item in items:
                response_data.append(item)

            return HttpResponse(json.dumps(response_data), content_type='application/json')

    return HttpResponse('Invalid request', status=400)


@csrf_exempt
def remove_item_from_cart(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần xoá
            user_id = data.get('User ID')
            product_id = data.get('Product ID')
            quantity = data.get('Quantity')

            # Tìm cart theo cart_id và user_id
            try:
                cart = Cart.objects.get(user_id=user_id)
            except Cart.DoesNotExist:
                return HttpResponse('Cart not found', status=404)

            quan = find_item_in_cart(cart=cart, product_id=product_id)
            if quan == 0: # Sản phẩm không tồn tại trong cart
                return HttpResponse('Item not found', status=404)
            else: # Cập nhật số lượng hoặc xoá sản phẩm
                for item in cart.items:
                    if item['Product ID'] == product_id:
                        new_quantity = item['Quantity'] - quantity
                        if new_quantity > 0:
                            item['Quantity'] = new_quantity
                        else:
                            cart.items.remove(item)
                
                cart.save()

            # Trả về thông tin của cart đã được cập nhật
            response_data = {'Cart ID': cart.cart_id, 'User ID': cart.user_id, 'Items': cart.items}
            return HttpResponse(json.dumps(response_data), content_type='application/json')

    return HttpResponse('Invalid request', status=400)

@csrf_exempt
def clear_cart(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần xoá
            user_id = data.get('User ID')

            # Tìm cart theo cart_id và user_id
            try:
                cart = Cart.objects.get(user_id=user_id)
            except Cart.DoesNotExist:
                return HttpResponse('Cart not found', status=404)
            
            items = cart.items
            for item in items:
                cart.items.remove(item)
            
            cart.save()

            # Trả về thông tin của cart đã được cập nhật
            response_data = {'Cart ID': cart.cart_id, 'User ID': cart.user_id, 'Items': cart.items, 'Message' : 'Cleared cart successfully.'}
            return HttpResponse(json.dumps(response_data), content_type='application/json')

    return HttpResponse('Invalid request', status=400)