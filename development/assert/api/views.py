from django.shortcuts import render
from rest_framework import status,renderers
from django.http import FileResponse
from rest_framework.decorators import action, schema
from rest_framework.schemas.openapi import AutoSchema
# Create your views here.
from rest_framework import generics, serializers
from rest_framework.response import Response
from .models import Student,FileUpload
from .serializer import StudentSerializer,FileSerializer
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class FileuploadViewset(viewsets.GenericViewSet):
    parser_classes = [MultiPartParser,FormParser]
    serializer_class=FileSerializer
    schema=AutoSchema(tags=['File'])
    queryset=FileUpload.objects.all()
    def create(self, request, *args, **kwargs):
        # file=request.FILES['uploadFile']
        serializer=FileSerializer(data=request.data)
        print(request.data['uploadFile'])
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'OK','message':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def list(self,request):
        serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(serializer.data)


class PassthroughRenderer(renderers.BaseRenderer):
    """
        Return data as-is. View should supply a Response.
    """
    media_type = ''
    format = ''
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

class ExampleViewSet(viewsets.GenericViewSet):
    serializer_class=FileSerializer
    queryset = FileUpload.objects.all()
    schema=AutoSchema(tags=['File'])    
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()
        # send file
        response = FileResponse(file_handle, content_type='application/multipart')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response


import requests
url='http://192.168.43.171:8081/library/book/delete_book/?id=2'
res=requests.delete(url)
print(res.text)



print(Student.objects.get(first_name__contains='ha'))

# a = 10
# b = 200
# a += 1   
# for i in range(a,b):
#     if(str(i) == str(i)[::-1]):
#         if(i>2):
#             for a in range(2,i):
#                 y = True
#                 if(i%a==0):
#                     y = False
#                     break
#             if y:
#                 print(i)
# print('\U0001F600')


a,b,c,d=[2,4,34,5,6],[34,6,3,67],[78,34,12,23],[34,23,45,9]
lst=[]
def find_max(arr):
    maximum=0
    for i in range(len(arr)):
        # print(arr[i-1] > maximum,a[i-1])
        if arr[i-1] > maximum:
            maximum=arr[i]
    return maximum
print(max([find_max(a),find_max(b),find_max(c),find_max(d)]))
        



    