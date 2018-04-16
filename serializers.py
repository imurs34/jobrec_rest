from rest_framework import serializers
from models import Job, Ints, User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job
		fields =('title','link','category')

'''
class UserSerializer(serializers.ModelSerializer):
	pass
		'''
		model = User
		fields =('FirstName','LastName','Email','interests')
		'''
