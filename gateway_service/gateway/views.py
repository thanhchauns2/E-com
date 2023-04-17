import random, json, requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            username = data.get('Username')
            password = data.get('Password')
            email = data.get('Email')
            address = data.get('Address')
            city = data.get('City')
            country = data.get('Country')
            first_name = data.get('First Name')
            last_name = data.get('Last Name')

            if username and password and email and address and city and country and first_name and last_name:
                address_id = requests.post('http://127.0.0.1:4000/users/create_address/', json={
                    "Address" : address,
                    "City" : city,
                    "Country" : country
                }).json()
                fullname_id = requests.post('http://127.0.0.1:4000/users/create_fullname/', json={
                    "First Name" : first_name,
                    "Last Name" : last_name
                }).json()
                account_id = requests.post('http://127.0.0.1:4000/users/create_account/', json={
                    "Username" : username,
                    "Password" : password,
                    "Email" : email
                }).json()
                customer_id = requests.post('http://127.0.0.1:4000/users/create_customer/', json={
                    "Address ID" : address_id['data']['Address ID'],
                    "Fullname ID" : fullname_id['data']['Fullname ID'],
                    "Account ID" : account_id['data']['Account ID']
                }).json()
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Successfully registered.'
                resp['data'] = {
                    "Address" : address_id, 
                    "Fullname" : fullname_id, 
                    "Account": account_id, 
                    "Customer ID" : customer_id
                } 
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def register_product(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            category_name = data.get('Category Name')
            author_name = data.get('Author Name')
            author_email = data.get('Author Email')
            author_address = data.get('Author Address')
            book_title = data.get('Book Title')
            published_date = data.get('Publishded Date')
            price = data.get('Price')
            description = data.get('Description')

            if category_name and author_name and author_email and author_address and book_title and published_date and price and description:
                requests.post('http://127.0.0.1:2100/books/categories/create/', json={
                    "Category Name" : category_name
                }).json()
                category_id = requests.post('http://127.0.0.1:2100/books/categories/search/', json={
                    "Category Name" : category_name
                }).json()
                requests.post('http://127.0.0.1:2100/books/authors/create/', json={
                    "Author Name" : author_name,
                    "Email" : author_email,
                    "Address" : author_address,
                }).json()
                author_id = requests.post('http://127.0.0.1:2100/books/authors/search/', json={
                    "Author Name" : author_name,
                    "Email" : author_email,
                    "Address" : author_address,
                }).json()
                print(author_id)
                print(category_id)
                book_id = requests.post('http://127.0.0.1:2100/books/books/create/', json={
                    "Author ID" : author_id['data'][0]['id'],
                    "Category ID" : category_id['data'][0]['id'],
                    "Title" : book_title,
                    "Published Date" : published_date,
                    "Price" : price,
                    "Description" : description
                }).json()
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Successfully registered.'
                resp['data'] = {
                    "Author" : author_id, 
                    "Category" : category_id, 
                    "Book" : book_id
                } 
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def inititate_inventory(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            requests.post('http://127.0.0.1:8000/inventory/initiate/', json={}).json()

            address = data.get('Address')
            book_quant = data.get('Book Quantity')
            clothes_quant = data.get('Clothes Quantity')
            elec_quant = data.get('Electronic Quantity')
            status = data.get('Status')

            data = requests.post('http://127.0.0.1:8000/inventory/initiate/', json={
                "Address" : address,
                "Book Quantity" : book_quant,
                "Clothes Quantity" : clothes_quant,
                "Electronic Quantity" : elec_quant,
                "Status" : status
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully updated.'
            resp['data'] = data

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def add_product_to_inventory(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            product_id = data.get('Product ID')
            quantity = data.get('Quantity')

            data = requests.post('http://127.0.0.1:8000/inventory/add_product/', json={
                "Product ID" : product_id,
                "Quantity" : quantity
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully added product to inventory.'
            resp['data'] = data

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def remove_product_from_inventory(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            product_id = data.get('Product ID')
            quantity = data.get('Quantity')

            data = requests.post('http://127.0.0.1:8000/inventory/remove_product/', json={
                "Product ID" : product_id,
                "Quantity" : quantity
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully removed product from inventory.'
            resp['data'] = data

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def show_inventory(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            inventory = requests.post('http://127.0.0.1:8000/inventory/show_inventory/', json={}).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully retrived data.'
            resp['data'] = inventory

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def add_product_to_cart(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            user_id = data.get('User ID')
            product_id = data.get('Product ID')
            quantity = data.get('Quantity')

            data = requests.post('http://127.0.0.1:5000/carts/add_item_to_cart/', json={
                "User ID" : user_id,
                "Product ID" : product_id,
                "Quantity" : quantity
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully added product to cart.'
            resp['data'] = data

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def remove_item_from_cart(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần xoá
            user_id = data.get('User ID')
            product_id = data.get('Product ID')
            quantity = data.get('Quantity')

            data = requests.post('http://127.0.0.1:5000/carts/remove_item_from_cart/', json={
                "User ID" : user_id,
                "Product ID" : product_id,
                "Quantity" : quantity
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully removed product from cart.'
            resp['data'] = data

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def show_cart(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            user_id = data.get('User ID')

            cart = requests.post('http://127.0.0.1:5000/carts/show_cart/', json={
                "User ID" : user_id
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully retrived information.'
            resp['data'] = cart

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def purchase(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            user_id = data.get('User ID')

            order_id = requests.post('http://127.0.0.1:3000/orders/create_order/', json={
                "User ID" : user_id
            }).json()

            requests.post('http://127.0.0.1:5000/carts/clear_cart/', json={
                "User ID" : user_id
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully retrieved information.'
            resp['data'] = {"Order ID" : order_id}

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def track_order(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            order_id = data.get('Order ID')

            order = requests.post('http://127.0.0.1:3000/orders/show_order/', json={
                "Order ID" : order_id
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully retrieved information.'
            resp['data'] = {"Order information" : order}

    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def update_order(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            data = json.loads(request.body)

            # Lấy thông tin cart và sản phẩm cần thêm
            order_id = data.get('Order ID')
            status = data.get('Status')

            requests.post('http://127.0.0.1:3000/orders/show_order/', json={
                "Order ID" : order_id,
                'Status' : status
            }).json()

            order = requests.post('http://127.0.0.1:3000/orders/show_order/', json={
                "Order ID" : order_id
            }).json()

            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Successfully updated information.'
            resp['data'] = {"Order information" : order}

    return HttpResponse(json.dumps(resp), content_type='application/json')