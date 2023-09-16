from django.db import models

# Create your models here.
class Person(models.Model):
    CHOICES = (
        ('male',"Male"),('female',"Female")
    )
    first_name = models.CharField(max_length=20, null=False, blank=False)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=False, blank = False)
    gender = models.CharField(max_length=6,default="male",choices=CHOICES)
    address = models.TextField()

    class Meta:
        verbose_name="Person"
        verbose_name_plural="Person"

    def __str__(self):
        return f"{self.first_name}{self.middle_name}{self.last_name}"