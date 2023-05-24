from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'test', views.TestViewSet)


urlpatterns = [
	path("",views.HomeView.as_view()),
	path("patient/create/",views.PatientCreateView.as_view()),
	path("patient/profile/",views.PatientProfileView.as_view()),
	# path("login/",views.)
	path("doctor/",views.DoctorListView.as_view()),
	path("doctor/all",views.DoctorListView.as_view()),
	path("doctor/<int:pk>/",views.DoctorRetrieveView.as_view()),
	path("doctor/create/",views.DoctorCreateView.as_view()),
	path("doctor/profile/",views.DoctorProfileView.as_view()),
	path("patient/appointment/create/",views.AppointmentCreateView.as_view()),
	path("patient/appointment/",views.PatientAppointmentView.as_view()),
	path("doctor/appointment/",views.DoctorAppointmentView.as_view()),

]+router.urls
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)