#This serializer converts model data to json objects. we can also convert in other format such as xml.
#Serializer convert data from complex types such as queryset to python native types which can easily be converted to JSON,xml etc.

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		#all fields
		fields = '__all__'
		#get specific fields
		#fields = ('title', 'url', 'description', 'publish_date')
		
