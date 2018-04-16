from rest_framework import serializers
from .models import Job, User


class JobSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job
		fields =('title','link','category')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		#fields =('FirstName','LastName','Email')
		fields =('FirstName','LastName','Email','interests')
