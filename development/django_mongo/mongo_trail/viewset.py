from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas.openapi import AutoSchema

class MemberViewset(viewsets.GenericViewSet):
    schema=AutoSchema(tags=['Member Controller'],component_name='Menbers')
    serializer_class=serializer.MemberSerializer
    queryset=models.Members.objects.all()
    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_400_BAD_REQUEST})
    def list(self,request):
        serializer=self.get_serializer(self.get_queryset(),many=True)
        print(serializer.data)
        a=[]
        for i in serializer.data:
            print(i['name'])
            i.pop('created_date')
            a.append(i)
        return Response(a)
    
