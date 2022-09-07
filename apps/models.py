from django.db import models


# Create your models here.
class StudentMaster(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    year = models.DateField()
    cnic = models.CharField(max_length=200,)

    def __str__(self):
        return self.name


class StudentDetail(models.Model):
    student_master = models.ForeignKey(
        StudentMaster, on_delete=models.CASCADE, blank=True, null=True
    )
    subject_name = models.CharField(max_length=20)
    subject_description = models.CharField(max_length=20)

    def __str__(self):
        return self.subject_name
