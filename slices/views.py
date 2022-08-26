from rest_framework import generics
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Articles, Payment, UserManage
from .serializers import ArticlesSerializer
from apples.time_logic import *
from apples.payment_terms import due_when

from django.urls import reverse

####ALLOW PREMIUM MEMBERS TO POST VIDEO REVIEWs

#####Django Rest


#RestLandingPage

# def home(request):
    
#     
#     getter = UserManage.objects.get(id=1)
#     created = Articles.objects.update_or_create(
#     author=getter, title="loop" , body=hello,
#     )



def home(request):
    """Returns dynamic message based on time of the week.
    V3. Offers coupon code for certain days of the week if signed in
    """
    
    
    
    heading = f"Welcome to the {headline_stringer()}" # custom message based on time of day

    coupon = "Thanks For Visiting"

    return render(request, "slices/index.html", context={"heading": heading, "coupon":coupon})




def payment_view(request, pk):
    """form processes payment if and applies the following logic if SUCCESSFUL"""
    #TODO: v3 add stripe and apply logic to db only on successful payment, Add get object or 404


    user = UserManage.objects.get(id=pk)

    #note - creates payment instance and ,unpack the returning tuple
    payment_record, _ = Payment.objects.get_or_create(username_id=pk)

 
    
    #TODO: Wrap logic below in form. ###ON POST
    """Method within_range() calculates dates between payments. Returns True if payment is due."""
    if Payment.within_range(payment_record, pk) == True:
        record_paying_ = Payment.pay_up(payment_record, pk)
    else: 
        print("payment not made")

    #TODO: if instance.paid == True and More that 10 days no button to pay shows. 
    #datetimefield stamp
    return render(request, 'slices/payment.html', context={"payer":payment_record,"user":user})


#articles list
class MemberListAPI(generics.ListAPIView):
    
 

    model = Articles
    serializer_class =ArticlesSerializer

    queryset = Articles.objects.all()

                    # https://stackoverflow.com/questions/48427475/class-based-view-and-call-function-to-script

                        #  def dispatch(self,request,*args,**kwargs):
                        #     lobby_object = self.get_object()
                        #     user_object = request.user
                        #     # do stuff with lobby_object & user_object
                        #     return super().dispatch(request,*args, **kwargs) 
                        #     # can also return an http request

    


#MemberDetailAPI
    #with last login
    #with articles writen
    #with total "OPENS of link as reads"



#CreateNewArticleView
    #TimeStamp
    #allow comments


#CompareAutherScoresView
    #1 author ID, vs Another auther Id. Returning total stars. 
    #returning total reads. 


#ReviewOthersArticleView
    #self review not allow. Guest review not allowed. 
    #author 1 to many with Articles. KEY
    #memmbers 1 to many with comment. KEY
    #Article 1 to One to many with Comment KEY


#DonateToAuthorView
    #guest or signed in can go to pay page
    #house takes .25 of every dollar. 



#PayMemberShipView
    #accept payment
    #email "coupon right now", v1 once a week in production


#CancelmembershipView



#####ADD CSV Exporting
# https://stackoverflow.com/questions/18685223/how-to-export-django-model-data-into-csv-file
    