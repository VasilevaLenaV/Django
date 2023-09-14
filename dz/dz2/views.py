from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from .forms import OrderForm


# Create your views here.


def create_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return render(request, 'success.html')

    return render(request, 'create_client.html')


def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        client.name = name
        client.email = email
        client.phone_number = phone_number
        client.address = address
        client.save()
        return render(request, 'success.html')

    return render(request, 'update_client.html', {'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        client.delete()
        return render(request, 'success.html')

    return render(request, 'delete_client.html', {'client': client})


def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
        return render(request, 'success.html')

    return render(request, 'create_product.html')


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']

        product.save()
        return render(request, 'success.html')

    return render(request, 'update_product.html', {'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return render(request, 'success.html')

    return render(request, 'delete_product.html', {'product': product})

# Cписок всех заказов
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


# Создание нового заказа
def order_create(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    return render(request, 'order/order_create.html', {'form': form})


# Просмотр информации о заказе
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})


# Обновление заказа
def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    return render(request, 'order/order_update.html', {'form': form, 'order': order})


# Удаление заказа
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order/order_delete.html', {'order': order})

