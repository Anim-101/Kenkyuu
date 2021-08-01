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
    permission_classes = (AllowAny,)

    def get(self, requests):
        name_list = ['Lee Mack', 'Louis Bell', 'Emma Harris', 'Keith Burton', 'Ricardo Cunningham', 'Vicky Daniel', 'Shawna Baldwin', 'Lela Davidson', 'Guadalupe Spencer', 'Anna Jacobs']
        mail_list = ['merges@hotmail.com', 'eidac@verizon.net', 'tarreau@hotmail.com' 'jipsen@icloud.com', 'conteb@icloud.com', 'crypt@verizon.net', 'kosact@att.net', 'subir@msn.com', 'tubesteak@aol.com', 'bastian@mac.com']
        age_list = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
        i = 0
        while i < 1000001:
            form_response = {
                'name': random.choice(name_list),
                'email': random.choice(mail_list),
                'age': random.choice(age_list)
            }
            data_model = DataModel.objects.create(
                form_id=1,
                form_response=form_response
            )
            data_model.save()
            i = i + 1
        return Response(True, status=status.HTTP_200_OK)


class DataFetchView(APIView):
    permission_classes = (AllowAny,)

    def get(self, requests):
        filtered_data = DataModel.objects.filter(form_id=1)
        data_list = []
        for data in filtered_data:
            data_list.append(data.form_response)
        data_response = {
            'data': data_list
        }
        return Response(data_response, status=status.HTTP_200_OK)


class DataFetchChunkView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def filter_query(offset, limit):
        data = DataModel.objects.filter(form_id=1)[offset:limit]
        return data

    def get(self, requests):
        try:
            offset = int(self.request.query_params.get('offset'))
            limit = int(self.request.query_params.get('limit'))
            filtered_data = self.filter_query(offset, limit)
            data_list = []
            if offset >= limit:
                return Response({'error': 'Offset should be smaller than limit.'}, status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)
            if filtered_data is not None:
                for data in filtered_data:
                    data_list.append(data.form_response)
            data_response = {
                'data': data_list
            }
            return Response(data_response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Offset and limit should be of int type.'}, status=status.HTTP_400_BAD_REQUEST)

