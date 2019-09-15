from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer
from rest_framework import status



#========================FUNCTION BASED API VIEW===========================================



@api_view(['GET','POST'])
def products_list(request):
#=====================================GET method====================================
	if request.method == 'GET':
		#fetch all objects from model/database. Here we are using sqlite db.
		obj = Product.objects.all()
		#serializing the fetched data. Many='True' means there can be multiple objects.
		serializer = ProductSerializer(obj, many='True')
		return Response(serializer.data)


#=====================================POST method====================================

	#It will be called only after giving data and pressing POST button or calling POST method from somewhere else
	elif request.method == 'POST':
		#Here the details of new product which we have typed at url is moved to serializer variable.
		#We first need to click POST button then this method will be call. So that before clicking POST we have data.
		#This data will be moved to serializer.
		serializer = ProductSerializer(data=request.data)
		#print("ok",serializer)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)





#===============================GET, Update and DELETE Specific Product==============================
@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, prod_id):
	obj = get_object_or_404(Product, pk = prod_id)
	
	if request.method == 'GET':
		serializer = ProductSerializer(obj)
		return Response(serializer.data)


	elif request.method == "PUT":
		#At this line we are requesting new typed data for update using request.data.
		serializer = ProductSerializer(obj, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.error)

	elif request.method == "DELETE":
		serializer = ProductSerializer(obj)
		obj.delete()
		return Response({"message" : "Deleted"+str(serializer.data)})