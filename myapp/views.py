from click import DateTime
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
import datetime
from .models import Membership
from django.http import HttpResponseRedirect
from django.http import JsonResponse
#from .models import Order
from .models import Customer
from .models import Payment



def dashboard(request):
    return render(request, 'dashboard.html',{})

def customer(request):
    context=Customer.objects.all()
    return render(request, 'customer.html',{"data":context})


def membership(request):
    context=Membership.objects.all()
    return render(request, 'membership.html', {"data":context})

def invoice(request):
	context=Payment.objects.all()
	return render(request,'invoice.html',{"data":context})

def bill(request):
    #selected_order = Order.objects.get(id=id)
    return render(request, 'bill.html', {})

# def order(request):
#     context=Order.objects.all()
#     return render(request, 'orders.html', {"data":context})
    
def signup(request):
	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name' or None]
		email = request.POST['email']
		password = request.POST['password']
		new_user= User.objects.create_user(
			first_name = first_name,
			last_name = last_name,
			email =  email,
			username = email,
			password = password,
			)
		new_user.save()
		return HttpResponse("""
			<h3>Signup Successful</h3>
			<p>
				<a href="/">Visit Homepage</a>
			</p>
			""")
	return render(request, 'signup.html', {})

