from email import message
from logging import exception
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import api_view,throttle_classes
import requests
from .form import Search_form

class UserMinThrottle(UserRateThrottle):
             scope = 'user_min'


class UserDayThrottle(UserRateThrottle):
             scope = 'user_day'


@api_view(['GET'])
@throttle_classes([UserMinThrottle,UserDayThrottle])
def home(request):
    try:
        response = requests.get(f'https://api.stackexchange.com/2.3/search/advanced?{request.META["QUERY_STRING"]}&site=stackoverflow')
        search_data = response.json()
        paginator = Paginator(search_data["items"], 6) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if request.method=="GET":
            from1=Search_form()
        
    except Exception as ex:
        raise Exception(ex)

    return render(request, 'home.html',{'search_data' :page_obj,"Search_form":from1 })