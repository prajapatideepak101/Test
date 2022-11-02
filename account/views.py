from distutils.log import error
from itsdangerous import Serializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import UserLoginSerializer , UserRegistrationSerializer,ProjectSerializer,ClientSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework import generics
from Project.models import Projects
from client.models import clients
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# Create your views here.
class UserRegistrationView(APIView):
    renderer_classes =[UserRenderer]
    def post(self,request,format=None):
        serializer =UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'login success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)

class ProjectsView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = ()
    authentication_classes = ()
class clientView(generics.ListCreateAPIView):
    queryset = clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = ()
    authetication_classes = ()
