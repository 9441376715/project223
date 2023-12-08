from django.db import models

# Create your models here.

class Department(models.Model):
    deptno=models.PositiveIntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    def __str__(self):
        return self.dname

class Employee(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    deptno=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename
