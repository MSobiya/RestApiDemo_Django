from rest_framework import serializers
from .models import Job

'''class JobSerializer(serializers.Serializer):
    j_title = serializers.CharField(max_length=255)
    j_desc = serializers.CharField(max_length)
	j_sal = serializers.IntegerField()
	j_location = serializers.CharField(max_length = 255)'''


class JobSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job
		fields = '__all__'