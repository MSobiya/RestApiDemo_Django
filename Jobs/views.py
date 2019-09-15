from django.shortcuts import render,get_object_or_404
from .models import Job
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import JobSerializer
from rest_framework import status
#from django.http import HttpResponse


#======================Get and Post Jobs================================================
class JobView(APIView):
	def get(self, request):
		all_jobs = Job.objects.all()
		serializer = JobSerializer(all_jobs, many = True)
		return Response(serializer.data)

	def post(self, request):
		serializer = JobSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#==============================Get, Update, Delete Specific Job=================================

class UpdateJob(APIView):
	def get(self, request, j_id):
		obj = get_object_or_404(Job, pk = j_id)
		serializer = JobSerializer(obj)
		return Response(serializer.data)

	def put(self, request, j_id):
		obj = get_object_or_404(Job, pk = j_id)
		serializer = JobSerializer(obj, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.error)

	def delete(self, request, j_id):
		obj = get_object_or_404(Job, pk = j_id)
		obj.delete()
		return Response({"Message": "Deleted"})