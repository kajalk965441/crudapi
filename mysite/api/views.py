from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import studentlist
from .serializers import studentdataserializers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import serializers
from rest_framework.status import HTTP_404_NOT_FOUND


@api_view(['GET'])
def index(request):
    students = studentlist.objects.all()
    serialstudents = studentdataserializers(students, many=True)
    return Response(serialstudents.data)


@api_view(["GET"])
def studentView(request, pk):
    student = studentlist.objects.get(id=pk)
    serialstudent = studentdataserializers(student,many=False)
    return Response(serialstudent.data)

@api_view(['POST'])
def studentAdd(request):
    serialstudent = studentdataserializers(data=request.data)
    # if serialstudent.objects.filtegetr(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')
  
    if serialstudent.is_valid():
        serialstudent.save()
        return Response(serialstudent.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def studentUpdate( request, pk):
    student = studentlist.objects.get(id = pk)
    serialstudent = studentdataserializers(instance=student, data=request.data)
     
    if serialstudent.is_valid():
        serialstudent.save()
    
    return Response(serialstudent.data)

@api_view(["DELETE"])
def studentdelete( request, pk):
    student = studentlist.objects.get(id=pk)
    student.delete()
    
    students= studentlist.objects.all()
    serialstudents = studentdataserializers(students, many=True)

    return Response(serialstudents.data)
