
from django.db import models
from django.contrib.auth.models import User 

class Customer(models.Model):
	fullname = models.CharField(max_length=50)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=15, unique=True)
	address = models.TextField(blank=True)
	pincode = models.CharField(max_length=6)
	def __str__(self):
		return self.fullname

class Membership(models.Model):
	membership_name = models.CharField(max_length=60, unique=True)
	membership_category = models.CharField(max_length=30,
		choices = (
			('Membership', 'Membership'),
			('Personal Training', 'Personal Training'),
			('Nutrition Consultation', 'Nutrition Consultation'),
			),
		default = ('Membership'),
		)
	membership_price =  models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return self.membership_name


# class Order(models.Model):
# 	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
# 	product = models.ForeignKey(Membership, on_delete=models.CASCADE)
# 	dop = models.DateTimeField(auto_now_add=True, verbose_name="Date of Purchase")
# 	quantity = models.PositiveSmallIntegerField(default=0)
# 	discount = models.PositiveSmallIntegerField(default=0)
# 	comment = models.TextField(blank=True)
# 	def __str__(self):
# 		return "%s - %s" % (self.customer.fullname, self.product.membership_name)

class Payment(models.Model):
    #order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product = models.ForeignKey(Membership, on_delete=models.CASCADE)
	mode = models.CharField(max_length=30,
		choices = (
			('Cash', 'Cash'),
			('UPI', 'UPI'),
			('Debit/Credit Card', 'Debit/Credit Card'),
			),
		default = ('Cash'),
		)
	date_of_payment = models.DateTimeField(auto_now_add=True)
	discount = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return "%s - %s" % (self.customer_name.fullname, self.product.membership_category,self.product.membership_price)

