from rest_framework.permissions import BasePermission
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Doctor,Patient


class IsDoctor(BasePermission):
	def has_permission(self, request,view):
		try:
			Doctor.objects.get(user=request.user)
		except Exception as e:
			print(e)
			return False

		return True


class IsPatient(BasePermission):
	def has_permission(self, request,view):
		try:
			Patient.objects.get(user=request.user)
		except Exception as e:
			print(e)
			return False

		return True

# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         account_approval = user.groups.filter(name='doctor').exists()
#         doctor = Doctor.objects.get
#         if request.user
#         # if user.status==False:
#         #     return Response(
#         #         {
#         #             'message': "Your account is not approved by admin yet!"
#         #         },
#         #         status=status.HTTP_403_FORBIDDEN
#         #     )
#         if account_approval==False:
#             return Response(
#                 {
#                     'message': "You are not authorised to login as a doctor"
#                 },
#                 status=status.HTTP_403_FORBIDDEN
#             )
#         else:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({
#                 'token': token.key
#             },status=status.HTTP_200_OK)