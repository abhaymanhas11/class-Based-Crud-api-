from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import s_serializer
from.models import student
from rest_framework.response import Response

class studentapi(APIView):
    def  get(self,request,id=None,fomat=None):
        id=id
        if id is not None:
            stu=student.objects.get(id=id)
            s=s_serializer(stu)
            return Response(s.data)
        stu = student.objects.all()
        s = s_serializer(stu,many=True)
        return Response(s.data)

    def post(self,request,format=None):
        s=s_serializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response({'msg':'Data inserted'})
        return Response(s.errors)

    def put(self,request,id=None,format=None):
        id=id
        stu=student.objects.get(id=id)
        s=s_serializer(stu,data=request.data)
        if s.is_valid():
            s.save()
            return Response({'msg':'updated successfully'})
        return Response(s.errors)

    def patch(self,request,id=None,format=None):
        id=id
        stu=student.objects.get(id=id)
        s=s_serializer(stu,data=request.data,partial=True)
        if s.is_valid():
            s.save()
            return Response({'msg':'updated successfully'})
        return Response(s.errors)

    def delete(self,request,id=None,format=None):
        id=id
        stu=student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'deleted successfully'})



