from rest_framework import serializers
from .models import Student,FileUpload


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','first_name', 'last_name', 'grade', 'age')

class FileSerializer(serializers.ModelSerializer):
    uploadFile=serializers.FileField(source='file')
    class Meta:
        model=FileUpload
        fields=('id','uploadFile','des')


