from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import *
import random
import time

class DataInsertView(APIView):
    permission_classes = (AllowAny, )

    def get(self, requests):
        name_list = ['Lee Mack', 'Louis Bell', 'Emma Harris', 'Keith Burton', 'Ricardo Cunningham', 'Vicky Daniel',
                     'Shawna Baldwin', 'Lela Davidson', 'Guadalupe Spencer', 'Anna Jacobs']
        mail_list = ['merges@hotmail.com', 'eidac@verizon.net', 'tarreau@hotmail.com' 'jipsen@icloud.com',
                     'conteb@icloud.com', 'crypt@verizon.net', 'kosact@att.net', 'subir@msn.com', 'tubesteak@aol.com',
                     'bastian@mac.com']
        age_list = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
        i = 0
        while i < 1000001:
            form_response = {
                'name': random.choice(name_list),
                'email': random.choice(mail_list),
                'age': random.choice(age_list)
            }
            data_model = DataModel()
            data_model.form_id = 1
            data_model.form_response = form_response
            data_model.save()
            i = i + 1
        return Response(True, status=status.HTTP_200_OK)