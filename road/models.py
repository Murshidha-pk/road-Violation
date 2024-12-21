from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=12,unique=True)


class RoadViolation(models.Model):

    name=models.CharField(max_length=100)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    description=models.TextField()

    VIOLATION_TYPES=(
        ("speeding","Speeding"),
        ("distracted_driving","Distracted driving"),
        ("seatbelt","Not Wearing Seatbelt"),
        ("parking","Illegal parking"),
        ("reckless","Reckless Driving"),
        ("traffic_signals","Ignoring Traffic Signals"),
        ("phone","Driving time phone usage"),
        ("register","Unregisterd Vehicle"),
        ("helmet","Riding Without Helmet"),
        ("Other","Other")
    )

    violation_type=models.CharField(max_length=100,choices=VIOLATION_TYPES,default="Speeding")

    fine_amount=models.PositiveIntegerField()

    location=models.CharField(max_length=100)

    image=models.ImageField(upload_to="violation_images",null=True,blank=True)

    timestamp=models.DateTimeField(null=True)


    def __str__(self):
        return self.name