from django.contrib import admin
from django.urls import path,include
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('users/projects/', ProjectsView.as_view(), name='projects'),
    path('users/clients/', clientView.as_view(), name='clients')
    
]
