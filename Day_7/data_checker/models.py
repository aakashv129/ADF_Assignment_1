"""Table Creation"""
from django.db import models

# Create your models here.
#pylint: disable=invalid-name


class Request_info(models.Model):
    """Request_info table"""
    f_name = models.CharField(max_length=45)
    m_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    nation = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    pin_code = models.IntegerField()
    qualification = models.CharField(max_length=45)
    salary = models.IntegerField()
    pan_number = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)


class Response_info(models.Model):
    """Response_info table"""
    response = models.CharField(max_length=10)
    reason = models.CharField(max_length=45)
