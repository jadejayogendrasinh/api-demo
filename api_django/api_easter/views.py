import json
from traceback import print_tb
from urllib import request
from django.shortcuts import render
from .models import CardItem, GIFsItem, QuotesItem
from .serializer import CardSerializer, GIFSerializer, QuotesSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
# Create your views here.

class CardView(APIView):
    queryset = CardItem.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            all_users = CardItem.objects.all()
            # all_users = CardItem.objects.all().values('cards')
            serializer = CardSerializer(all_users, context={"request": request}, many=True)
            # newdata = {"cards":[]}
            # {newdata["cards"].append(i["cards"]) for i in serializer.data}

            return Response({"Response": True, "ReturnCode": 1, "Result":serializer.data, "Message": "Success"}, status=200)
        else:
            return Response({"Response": False, "ReturnCode": 1, "Result": [], "Message": "Fail"}, status=200)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and 'cards' in request.data and request.data['cards']:
            # converts querydict to original dict
            images = dict((request.data).lists())['cards']
            flag = 0
            for img_name in images:
                try:
                    CardItem.objects.create(cards=img_name)
                    flag = 1
                except Exception as e:
                    flag = 0
                    raise e
            if flag == 1:
                return Response({'message': "Uploaded"}, status=200)
            else:
                return Response({'message': "Upload Unsuccessfull"}, status=404)
        else:
            return Response({'message': "Request type get or not proper card data"}, status=404)

class CardsDetail(APIView):
    def get_object(self, pk):
        try:
            return CardItem.objects.get(pk=pk)
        except CardItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CardSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CardSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Response": True, "ReturnCode": 1, "Result": [], "Message": "Deleted Successfully"}, status=200)

# @api_view(['GET'])
# def getData(request):
#     if request.method == 'GET':
#         all_users = CardItem.objects.all()
#         # all_users = CardItem.objects.all().values('cards')
#         serializer = CardSerializer(all_users, context={"request": request}, many=True)
#         newdata = {"cards":[]}
#         {newdata["cards"].append(i["cards"]) for i in serializer.data}

#         return Response({"Response": True, "ReturnCode": 1, "Result": newdata, "Message": "Success"}, status=200)
#     else:
#         return Response({"Response": False, "ReturnCode": 1, "Result": [], "Message": "Fail"}, status=200)
    # return Response(person)

class GIFView(APIView):
    queryset = GIFsItem.objects.all()
    serializer_class = GIFSerializer

    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and 'gifs' in request.data and request.data['gifs']:
            # converts querydict to original dict
            images = dict((request.data).lists())['gifs']
            flag = 0
            for img_name in images:
                try:
                    GIFsItem.objects.create(gifs=img_name)
                    flag = 1
                except Exception as e:
                    flag = 0
                    raise e
            if flag == 1:
                return Response({'message': "Uploaded"}, status=200)
            else:
                return Response({'message': "Upload Unsuccessfull"}, status=404)
        else:
            return Response({'message': "Upload Unsuccessfull"}, status=404)
    
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            all_users = GIFsItem.objects.all()
            serializer = GIFSerializer(
                all_users, context={"request": request}, many=True)
            # newdata = {"gifs":[]}
            # {newdata["gifs"].append(i["gifs"]) for i in serializer.data}
            return Response({"Response": True, "ReturnCode": 1, "Result": serializer.data, "Message": "Success"}, status=200)
        else:
            return Response({"Response": False, "ReturnCode": 1, "Result": [], "Message": "Fail"}, status=200)

class GIFsDetail(APIView):
    def get_object(self, pk):
        try:
            return GIFsItem.objects.get(pk=pk)
        except GIFsItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GIFSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GIFSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Response": True, "ReturnCode": 1, "Result": [], "Message": "Deleted Successfully"}, status=200)

class QuotesView(APIView):
    queryset = QuotesItem.objects.all()
    serializer_class = QuotesSerializer

    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and 'quotes' in request.data and request.data['quotes']:
            # converts querydict to original dict
            flag = 1
            try:
                QuotesItem.objects.create(quotes=request.data['quotes'])
                flag = 1
            except Exception as e:
                flag = 0
                raise e
            if flag == 1:
                return Response({'message': "Success"}, status=200)
            else:
                return Response({'message': "Failed"}, status=404)
        else:
            return Response({'message': "Failed"}, status=404)
    
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            all_users = QuotesItem.objects.all()
            serializer = QuotesSerializer(
                all_users, context={"request": request}, many=True)
            newdata = {"quotes":[]}
            {newdata["quotes"].append(i["quotes"]) for i in serializer.data}
            return Response({"Response": True, "ReturnCode": 1, "Result": newdata, "Message": "Success"}, status=200)
        else:
            return Response({"Response": False, "ReturnCode": 1, "Result": [], "Message": "Fail"}, status=200)