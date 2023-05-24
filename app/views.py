from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import QueryDict
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Patient,Doctor,Address,Appointment,Test
from rest_framework.response import Response  
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import PatientSerializer,UserSerializer,DoctorSerializer,TestSerializer,AppointmentSerializer
from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from .permissions import IsDoctor,IsPatient

class PatientCreateView(generics.CreateAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer

	def perform_create(self,serializer):
		user_data = self.request.data.get("user")
		user_serializer = UserSerializer(data = user_data)
		if user_serializer.is_valid():
			user = user_serializer.save()
			user.set_password(user_data.get("password"))
			user.save()
			return serializer.save(user = user)

class PatientProfileView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsPatient]

	def get(self,request,format=None):
		serializer = PatientSerializer(request.user.patient)
		return Response(serializer.data,status=200)



class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = []
    permission_classes = [IsAdminUser]



class DoctorProfileView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsDoctor]
	def get(self, request, format=None):
		serializer = PatientSerializer(request.user.doctor)
		return Response(serializer.data,status=200)


class AppointmentCreateView(generics.CreateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentSerializer
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsPatient]

	def perform_create(self,serializer):
		doctor = Doctor.objects.get(id=self.request.data.get("doctor"))
		print(self.request.user.patient)
		return serializer.save(patient=self.request.user.patient,doctor=doctor)

class PatientAppointmentView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsPatient]

	def get(self,request,format=None):
		appointments = Appointment.objects.filter(patient=request.user.patient)
		serializer = AppointmentSerializer(appointments,many=True)

		return Response(serializer.data,status=200)

class DoctorAppointmentView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsDoctor]

	def get(self,request,format=None):
		appointments = Appointment.objects.filter(doctor=request.user.doctor)
		serializer = AppointmentSerializer(appointments,many=True)

		return Response(serializer.data,status=200)


class DoctorRetrieveView(generics.RetrieveAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	lookup = 'pk'

class DoctorCreateView(generics.CreateAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer


class TestViewSet(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializer
	authentication_classes = [SessionAuthentication,TokenAuthentication]



class HomeView(APIView):
	def get(self, request, format=None):
		return Response({"message":"yep"},status=200)


# class DoctorAppointmentView(APIView):

# 	def get(self, request, format=None):




