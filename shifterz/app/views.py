from django.conf.urls import url
from django.contrib.auth.models import User
from django.http import HttpResponse
# from django.shortcuts import render_to_response
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import (Customer,Product,Cart,OrderPlaced,Wishlist)
from shifterz import settings
from django.contrib.sites.shortcuts import get_current_site
from json import dump, dumps

def home(request):
    brakes=Product.objects.filter(category='BR')
    seat=Product.objects.filter(category='SE')
    lights=Product.objects.filter(category='LI')
    underglow=Product.objects.filter(category='UN')
    spoilers=Product.objects.filter(category='SP')
    usr=request.user 
    ab=[]
    for p in Product.objects.all():
        temp=[p.title, p.id]
        ab.append(temp)
    ab=dumps(ab)
    print(ab)
    return render(request,'index.html',{'brakes':brakes,
    'seat':seat,'lights':lights,'underglow':underglow,
    'spoilers':spoilers,'list':ab})


def getaddress(request):

    if request.method=='GET':
        usr=request.user
        address=Customer.objects.filter(user=usr)
        ab=[]
        for a in address:
            temp={'id':a.id,'name':a.name,'locality':a.locality,'city':a.city,'zipcode':a.zipcode,'state':a.state}
            ab.append(temp)
        # print(ab)
        return JsonResponse(ab,safe=False)
        
def deleteaddress(request,n):
    if request.method=='GET':
        usr=request.user
        Customer.objects.filter(user=usr,id=n).delete()
        return JsonResponse('ab',safe=False)

def add_address(request):
    if request.method=='POST':
        usr=request.user
        n=request.POST['name']
        l=request.POST['locality']
        c=request.POST['city']
        s=request.POST['state']
        z=request.POST['zipcode']
        Customer(user=usr,name=n,locality=l,city=c,state=s,zipcode=z).save()
        address=Customer.objects.filter(user=usr)
        ab=[]
        for a in address:
            temp={'id':a.id,'name':a.name,'locality':a.locality,'city':a.city,'zipcode':a.zipcode,'state':a.state}
            ab.append(temp)
        return JsonResponse(ab,safe=False)


def getwishlist(request):
    if request.method=='GET':
        usr=request.user
        wishlist=Wishlist.objects.filter(user=usr)
        ab=[]
        for p in wishlist:
            temp={'id':p.product.id,'image':p.product.product_image.url,'title':p.product.title,'price':p.product.discounted_price}
            ab.append(temp)
        return JsonResponse(ab,safe=False)

def removewishlist(request,n):
     if request.method=='GET':
        usr=request.user
        Wishlist.objects.filter(user=usr , product=n).delete()
        wishlist=Wishlist.objects.filter(user=usr)
        ab=[]
        for p in wishlist:
            temp={'id':p.id,'image':p.product.product_image.url,'title':p.product.title,'price':p.product.discounted_price}
            ab.append(temp)
        return JsonResponse(ab,safe=False)

def addwishlist(request,n):
    if request.method=='GET':
        usr=request.user
        # product_id=request.GET.get('prod_id')
        product=Product.objects.get(id=n)
        Wishlist(user=usr,product=product,wish=True).save()
        return JsonResponse('ab',safe=False)


def getorders(request):
     if request.method=='GET':
        usr=request.user
        order=OrderPlaced.objects.filter(user=usr)
        ab=[]
        for p in order:
            date=str(p.ordered_date).split()[0]
            temp={'order_id':p.order_id,'amount':p.amount,'date':date,'locality':p.customer.locality,'city':p.customer.city,'status':p.status}
            ab.append(temp)
        return JsonResponse(ab,safe=False)

def product_page(request,n):
    product=Product.objects.get(id=n)
    usr=request.user 
    try:
        wish=Wishlist.objects.filter(user=usr).filter(product=n).first()
        return render(request,'product.html',{'product':product,'wish':wish})
    except:
        return render(request,'product.html',{'product':product,})




def cart(request):
    usr=request.user 
    try:
        cart=Cart.objects.filter(user=usr)
        # for c in cart:print(usr,w.wish) 
        shipping=5.0
        total=0.0
        for p in cart:
                tempamount=(p.quantity*p.product.discounted_price)
                total+=tempamount
        return render(request,'cart.html',{'cart':cart,'total':total,'total2':total+shipping,'shipping':shipping})
    except:
        return render(request,'cart.html')

def add_to_cart(request,n):
    usr=request.user
    product=Product.objects.get(id=n)
    Cart(user=usr,product=product).save()
    return JsonResponse('ab',safe=False)

def remove_from_cart(request,n):
    usr=request.user
    Cart.objects.filter(user=usr,product=n).delete()

    cart=Cart.objects.filter(user=usr)
    shipping=5.0
    total=0.0
    for p in cart:
            tempamount=(p.quantity*p.product.discounted_price)
            total+=tempamount
    ab=[{'total':total,'total2':total+shipping,'shipping':shipping}]
    return JsonResponse(ab,safe=False)

def minus_cart(request,n):
    usr=request.user
    c=Cart.objects.get(user=usr,product=n)
    if c.quantity!=1:
        c.quantity-=1
        c.save()
    cart=Cart.objects.filter(user=usr)
    shipping=5.0
    total=0.0
    for p in cart:
            tempamount=(p.quantity*p.product.discounted_price)
            total+=tempamount
    ab=[{'total':total,'total2':total+shipping,'shipping':shipping,'that_quantity':c.quantity}]
    return JsonResponse(ab,safe=False)

def plus_cart(request,n):
    usr=request.user
    c=Cart.objects.get(user=usr,product=n)
    c.quantity+=1
    c.save()
    cart=Cart.objects.filter(user=usr)
    shipping=5.0
    total=0.0
    for p in cart:
            tempamount=(p.quantity*p.product.discounted_price)
            total+=tempamount
    ab=[{'total':total,'total2':total+shipping,'shipping':shipping,'that_quantity':c.quantity}]
    return JsonResponse(ab,safe=False)

def del_user(request):
    usr=request.user
    User.objects.get(username=usr).delete()
    return JsonResponse("ab",safe=False)



# Adding Payment Gateway
import razorpay
razorpay_client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_account_id))

def checkout(request):
    usr=request.user
    address=Customer.objects.filter(user=usr)
    cart=Cart.objects.filter(user=usr)
    # for c in cart:print(usr,w.wish) 
    shipping=5.0
    total=0.0
    for p in cart:
            tempamount=(p.quantity*p.product.discounted_price)
            total+=tempamount

    order_currency = 'AUD'
    callback_url = str(get_current_site(request))+"handlerequest/"
    # print(callback_url)
    notes = {'order-type': "basic order from the website", 'key':'value'}
    razorpay_order = razorpay_client.order.create(dict(amount=(total+shipping)*100, currency=order_currency, notes = notes, payment_capture='0'))
    # print(razorpay_order['id'])
    return render(request,'checkout.html',{'address':address,'cart':cart,'total':total,'total2':total+shipping,'shipping':shipping,'order_id': razorpay_order['id'],'callback_url':callback_url})

def success(request,n):
    usr=request.user
    c=Customer.objects.get(id=n)
    OrderPlaced(user=usr,customer=c,order_id="pending",amount="0").save()


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id','')
            signature = request.POST.get('razorpay_signature','')
            params_dict = { 
            'razorpay_order_id': order_id, 
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result==None:
                # amount = order_db.total_amount * 100   #we have to pass in paisa
                usr=request.user
                cart=Cart.objects.filter(user=usr)
                shipping=5.0
                total=0.0
                for p in cart:
                        tempamount=(p.quantity*p.product.discounted_price)
                        total+=tempamount
                try:
                    print("doing it 1")
                    amount=int(total+shipping)*100
                    razorpay_client.payment.capture(payment_id,amount) 
                    print("doing it 2") 
                    # usr=request.user
                    # OrderPlaced(user=usr,order_id=order_id,amount=(amount/100)).save()
                    order=OrderPlaced.objects.get(order_id="pending")
                    order.order_id=order_id
                    order.amount=amount/100
                    order.save()
                    Cart.objects.filter(user=usr).delete()
                    return render(request, 'payment-success.html')
                except:
                    # print("lol")
                    order=OrderPlaced.objects.get(order_id="pending")
                    order.delete()
                    return render(request, 'payment-failed.html')
            else:
                # print("nyc")
                return render(request, 'payment-failed.html')
        except:
            return HttpResponse("505 not found")


def handler404(request, exception,*args, **kwargs):
    return render(request,'404.html') 

def handler400(request, exception,*args, **kwargs):
    return render(request,'400.html')

def handler500(request, exception,*args, **kwargs):
    return render(request,'500.html')


def privacy(request):
    return render(request,'privacy.html')

def terms(request):
    return render(request,'terms.html')

def returnpolicy(request):
    return render(request,'return-policy.html')

def shippingpolicy(request):
    return render(request,'shipping-policy.html')