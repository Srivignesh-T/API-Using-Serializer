from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .models import Employee
from .serializer import EmployeeSerializer
# from django.db.models import Q

class EmployeeDetails(APIView):

    def get(self, request):
        data = Employee.objects.all()
        serial = EmployeeSerializer(data, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    def post(self, request):
        serial = EmployeeSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)


class EmployeeInfo(APIView):
    def get(self, request, id):
        try:
            data = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            raise Http404

        serial = EmployeeSerializer(data)
        return Response(serial.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            data = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            raise Http404
        serial = EmployeeSerializer(data, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            data = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            raise Http404
        serial = EmployeeSerializer(data, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            data = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404
        data.delete()
        return Response({"msg":"Record Deleted"}, status=status.HTTP_204_NO_CONTENT)

