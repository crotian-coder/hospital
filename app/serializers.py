from rest_framework import serializers
from .models import Patient,Doctor,Appointment,Test
from django.contrib.auth.models import User
from .models import APPOINTMENT_STATUS

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','last_name','password','username')




class PatientSerializer(serializers.ModelSerializer):

	user = UserSerializer()

	class Meta:
		model = Patient
		fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Doctor
		fields = '__all__'

	def create(self,validated_data):
		user_data = validated_data.pop("user")
		user_obj = UserSerializer(data=user_data)
		if user_obj.is_valid():
			get_user = User.objects.create(**user_data)
			get_user.set_password(user_data["password"])
			get_user.save()
			instance = Doctor.objects.create(user =get_user, **validated_data)
		return instance

class TestSerializer(serializers.ModelSerializer):

	class Meta:
		model = Test 
		fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
	status = serializers.ChoiceField(choices=APPOINTMENT_STATUS, read_only=True)
	patient = PatientSerializer(read_only=True)
	class Meta:
		model = Appointment
		fields = '__all__'



