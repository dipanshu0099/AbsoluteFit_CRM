
from django.contrib import admin

from myapp.models import Customer,Membership, Payment

admin.site.site_title = "AbsoluteFit"

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone',]
    list_filter = ['address', 'pincode',]
    #list_display_links = ['id']
    list_per_page = 20 
    

class MembershipAdmin(admin.ModelAdmin):
     list_display = ['membership_name' , 'membership_category','membership_price',]
    # list_display_links = ['id']
     list_filter = ['membership_category']
     list_per_page = 20 


class PaymentAdmin(admin.ModelAdmin):
    list_display=['customer_name','product','mode','discount','date_of_payment']
    #list_display_links = ['id']
    #list_editable = ['mode','discount']
    list_per_page = 20 


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Membership,MembershipAdmin)
admin.site.register(Payment,PaymentAdmin)