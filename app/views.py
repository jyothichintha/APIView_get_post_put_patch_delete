from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response


class ProductCrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)

    def post(self,request,id):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'massage':'Product is created'})
        else:
            return Response({'Failed':'Product create is failed'})

    def put(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'massage':'Product is updated'})
        else:
            return Response({'Failed':'Product create is updated'})

    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PO.save()
        return Response({'msg':'Product is partially updated'})

    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'msg':'Product is deleted Successfully'})

