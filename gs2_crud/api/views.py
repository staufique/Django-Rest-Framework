from django.shortcuts import render
from io import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


#this is function based logic to perform CRUD Opertaion
@csrf_exempt
def student_api(request):

    # creating logic for get data from database
    if request.method=='GET':
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream) 
        id = pythondata.get('id', None)
        if id is not None:
            stu  = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    
    # Createing logic to create data to database
    if request.method=='POST':
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data inserted'}
            json_data=JSONRenderer().render(res['msg'])
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    

    # creating logic for update data to database
    if request.method=="PUT":
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data = pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data upadted'}
            json_data = JSONRenderer().render(res['msg'])
            return HttpResponse(json_data, content_type='application/type')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/type')
    
    # creating logic to delete data from database
    if request.method=='DELETE':
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted'}

        # json_data=JSONRenderer().render(res['msg'])
        # return HttpResponse(json_data,content_type='application/json')

        return JsonResponse(res['msg'],safe=False)