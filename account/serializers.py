from asyncore import write
from dataclasses import field, fields
import email
from pyexpat import model
from click import style
from client.models import clients
from Project.models import Projects
from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','name','password','password2','tc']
        extra_kwargs={'password':{'write_only':True}
        }
#validating password and confirm password while registeration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesn't match")
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']
        extra_kwargs={'password':{'write_only':True}
        }

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'about', 'date', 'user']
    user = UserLoginSerializer()

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ['user', 'projects_list', 'active_project', 'done_projects']
    user = UserLoginSerializer()
    active_project = ProjectSerializer()
    done_projects = ProjectSerializer()