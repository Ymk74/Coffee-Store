from django.shortcuts import render ,redirect
from django.contrib import messages
from products.models import Product
from orders.models import Order , OrderDetail
from django.utils import timezone
# Create your views here.

# def add_to_cart(request):

#     if id in request.GET and 'qty' in request.GET and 'price' in request.GET and request.user.is_authenticated and not request.user.is_anonymous :
#         id = request.GET['id']
#         qty = request.GET['qty']
#         order = Order.objects.all().filter(user=request.user,is_finished=False)

#         if order:
#             messages.success(request, 'an old order is available')
#         else:
#             messages.success(request,'you can make new order here')
#             new_order = Order()
#             new_order.user = request.user
#             new_order.created_at = timezone.now()
#             new_order.is_finished = False
#             new_order.save()
#             # orderdetails = OrderDetail.objects.create()

#         return redirect('/products/'+ request.GET['id'])
#     else :
#         return redirect('products')

def add_to_cart(request):
    if 'product_id' in request.GET and 'quantity' in request.GET and 'price' in request.GET and request.user.is_authenticated and not request.user.is_anonymous:
        product_id = request.GET['product_id']
        quantity = request.GET['quantity']
        order = Order.objects.all().filter(user=request.user,is_finished=False)
        if not Product.objects.all().filter(id=product_id).exists():
            return redirect('products')
        product = Product.objects.get(id=product_id)
        if order:
            #messages.success(request,'Find old order')
            old_order = Order.objects.get(user=request.user,is_finished=False)
            if OrderDetails.objects.all().filter(product=product,order=old_order).exists():
                orderdetails = OrderDetails.objects.get(order=old_order,product=product)
                orderdetails.quantity += int(quantity)
                orderdetails.save()
            else:
                orderdetails = OrderDetails.objects.create(product=product,order=old_order,quantity=quantity)
            messages.success(request,'was added to cart for old orders')
        else:
            messages.success(request,'Run new order')
            new_order = Order()
            new_order.user = request.user
            new_order.created_at = timezone.now()
            new_order.is_finished = False
            new_order.save()
            orderdetails = OrderDetails.objects.create(product=product,order=new_order,price=product.price,quantity=quantity)
            messages.success(request,'added to new order')
        return redirect('/products/' + request.GET['product_id'])
    else:
        if 'product_id' in request.GET:
            messages.error(request,'You must login in')
            return redirect('/products/' + request.GET[product_id])
        else:
            return redirect('signin')

    

def cart(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        if Order.objects.filter(user=request.user, is_finished=False):
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.filter(order=order)
            total = 0
            for sub in orderdetails:
                total += sub.price * sub.quantity
            context = {
                'order': order,
                'orderdetails': orderdetails,
                'total': total,
            }
    return render(request, 'orders/cart.html', context)

def removecart(request,id):
    if request.user.is_authenticated and not request.user.is_anonymous and id:
        orderdetails = OrderDetails.objects.get(id=id)
        if orderdetails.order.user.id==request.user.id:
            orderdetails.delete()
    return redirect('cart')

def add_qty(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous and id:
        orderdetails = OrderDetails.objects.get(id=id)
        if orderdetails.order.user.id==request.user.id:
            orderdetails.quantity += 1  # corrected the syntax here
            orderdetails.save()
    return redirect('cart')


def sub_qty(request, id):
    if request.user.is_authenticated and not request.user.is_anonymous and id:
        orderdetails = OrderDetails.objects.get(id=id)
        if orderdetails.order.user.id==request.user.id:
            if orderdetails.quantity > 1:
                orderdetails.quantity -= 1
                orderdetails.save()
    return redirect('cart')


def payment(request):
    return render(request,'orders/payment.html')