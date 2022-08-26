

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date, datetime

#Django abstract user
class UserManage(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(blank=True, max_length=25)
    last_name = models.CharField(blank=True,  max_length=25)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] #phone number

    #with lastlogin field in admin
    #wtih lastlogin field in model

    related_name='abs_user',
    verbose_name=_('abs_user'),

    def __str__(self):
        return f"{self.username} {self.id}"  #self.last_login



class Articles(models.Model):
    author = models.ForeignKey('UserManage', on_delete=models.CASCADE) #forignkey member
    title = models.CharField(max_length=75, blank = False)
     #date
    body = models.TextField(blank = False)

    def __str__(self):
        return f"{self.author.username} {self.title}"  #self.last_login


    


class Comments(models.Model):
    author = models.ForeignKey('UserManage', on_delete=models.CASCADE)
    article = models.ForeignKey('Articles', on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    
    #date
#     #comment body
#     #acceptable default true

#     def like_comment_toggler(self):


#     def flag_inapproriate(self):
#         self.acceptable = false

#     def eval_accepatable(self):
#         #if count of unique unacceptable 3+ hide comment. 

# ####Viewable but not writtable. Only viewable for self. 
# class Payment_Status(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE )
#     paid = models.BooleanField(default=False) #production default FALSE


    

#Is one to many to keep record of membership lenghth 1 payer many months paid
class Payment(models.Model):
    username = models.OneToOneField('UserManage', primary_key=True,on_delete=models.CASCADE)
    charges = models.FloatField(default=99.99)
    payment_amount = models.FloatField(default=0)
    auto_pay =models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    coupon = models.CharField(max_length=75, null=True, blank=True)
    #join_date
    #consequetive_months_paid
    last_payment = models.DateField
    #payment_due_date
    # last_payment_date
    


    def __str__(self):
        return f"{self.username.username} has paid: {self.paid}"
    

    def within_range(self,*args, **Kwargs):
        """Boolean returning function 10 days or less between today and last payment
        also take another step and blank if within range no true"""
        #place holder for now
        #if last_payment_date - datetime.today < 10 :

        ######or solution can be due date + a certain amount if days
        ###### and while here due date field is due date .save()
        ######if today is greater than or = due date payment due = true

        #else
        from datetime import date
        print("today is :",datetime.now())
        d0 = date(2017, 8, 18)
        d1 = date(2017, 10, 26)
        print(d1)
    
        delta = d1 - d0
        print(delta.days)
        
        #Placeholder to keep code from breaking 
        return False


    
    def pay_up(self, *args, **Kwargs):
        self.paid = True
        self.save()
       
    

  
  
        #place holder = (Payment, pk = id)
    
    
    #def on success charge card 99 and record amount collected as 99
        #if coupon == charges field x .05
    #next_paymentdate = 30 days after payment date. 

    #TODO create method that turns paid to true
    #TODO add auto pay to form, coupon field in form


    
    


    # def time_stamp(self, pk):
    #     self.last_payment_date
   
    #if less than 10 days in month ask for payment

    


#https://learndjango.com/tutorials/django-slug-tutorial


#TODO: Try different styles of flipping this value
    # def subscription_payer(self):
    #     """Allows user to submit a payment. In test phase
    #     simple button click denotes payment. """
       
    #     self.paid = True
    #     self.save()
        
    
       
        

#TODO: v1.1 one to many with author
# class Articles(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50)
#     # subtitle not required
