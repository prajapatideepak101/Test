from django.db import models
from account.models import CustomUser
from Project.models import Projects

# Create your models here.
class Clients(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    projects_list = models.ManyToManyField(Projects, related_name='projects_list', verbose_name='List of Projects')
    active_project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Active Project')
    done_projects = models.ManyToManyField(Projects, related_name='project_dones', verbose_name='Done Projects')
    def __str__(self):
        return self.user.full_name