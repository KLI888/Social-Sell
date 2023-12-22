from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.conf import settings
import razorpay

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def home(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        feedback_email = request.POST.get('feedback_email')
        feedback_msg = request.POST.get('feedback_msg')

        feedback = Feedback.objects.create(full_name=full_name, feedback_email=feedback_email, feedback_msg=feedback_msg)
        feedback.save()

    instaAcc = InstaAccounts.objects.all()
    context = {
        'instaAcc': instaAcc
    }
    return render(request, 'index.html', context)



def followerPage(request):
    followers = Followers.objects.all()
    context = {
        'followers': followers
    }
    return render(request, 'followerType.html', context)

def followerType(request, id):
    instaAcc = InstaAccounts.objects.filter(ac_follow=id)
    context = {
        'instaAcc': instaAcc
    }
    return render(request, 'followerTypePage.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/loginPage')

def registerPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            return render(request, 'signup.html')
        except:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/loginPage')

        

    return render(request, 'signup.html')

def aboutusPage(request):
    return render(request, 'aboutus.html')

def sellPage(request):
    if request.method == "POST":
        ac_name = request.POST.get('ac_name')
        ac_category = request.POST.get('ac_category')
        ac_followers = request.POST.get('ac_followers')
        ac_age = request.POST.get('ac_age')
        ac_fullname = request.POST.get('ac_name')
        ac_email = request.POST.get('ac_email')

        sellAcc = SellAcc(ac_name=ac_name, ac_category=ac_category, ac_followers=ac_followers, ac_age=ac_age, ac_fullname=ac_fullname, ac_email=ac_email)

        sellAcc.save()
        return redirect('/')
    
    category = Category.objects.all()
    context = {
        'category': category
    }

    return render(request, 'sell.html', context)

def deliveryPage(request):
    instaAcc = InstaAccounts.objects.all()
    context = {
        'instaAcc': instaAcc
    }
    return render(request, 'delivery.html', context)

def contactPage(request):
    return render(request, 'contact.html')

def categoryPage(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys
    }
    return render(request, 'category.html', context)



def productViewPage(request, ac_name):
    if not request.user.is_authenticated:
        return redirect('loginPage') 
    try:
        insta_acc = get_object_or_404(InstaAccounts, ac_name=ac_name)
        
        client = razorpay.Client(auth=(settings.KEY, settings.SECRET))

        payment = client.order.create({
            'amount': int(insta_acc.ac_price) * 100,
            'currency': 'INR',
            'payment_capture': 1
        })
        cart_obj = Cart.objects.create(
            user=request.user,
            razor_pay_order_id=payment['id'],
            sell_ac=insta_acc
        )

        context = {
            'instaAcc': insta_acc,
            'payment': payment
        }

        return render(request, 'productView.html', context)

    except InstaAccounts.DoesNotExist:
        raise Http404("Instagram account does not exist")

    except Exception as e:
        # Handle exceptions appropriately, log them, and inform the user
        return render(request, 'error.html', {'error_message': str(e)})

def categoryType(request, id):
    instaAcc = InstaAccounts.objects.filter(ac_category=id)
    context = {
        'instaAcc': instaAcc
    }
    return render(request, 'categoryType.html', context)

def success(request):
    order_id = request.GET.get('order_id')
    cart = Cart.objects.get(razor_pay_order_id=order_id)
    cart.is_paid = True
    cart.save()
    return HttpResponse("Payment Successfully")
    # return redirect('home')