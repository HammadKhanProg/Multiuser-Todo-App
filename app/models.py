from django.db import models
from django.contrib.auth.models import User
class TODO (models.Model):
    status_choices=[
        ("Completed","Complete"),
        ("Pending","Pending"),
    ]
    priority_choices=[
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    ]

    title=models.CharField(max_length=50)
    status=models.CharField(max_length=50, choices=status_choices)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=50, choices=priority_choices)


    def __str__(self):
        return self.title
# Create your models here.
