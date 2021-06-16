from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField 
from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy
from django.db.models.fields.related import ManyToManyField 



class Exercise(Model): 
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=500, default="https://www.atehno.md/theme/images/no_image.png")
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name 

#Many:Many A workout can have many exercises. An exercise can relate to many workouts. 
class Workout(Model):
    name = models.CharField(max_length=20)
    exercises = ManyToManyField(Exercise)


    def __str__(self):
        return self.name 

# 1 profile to 1 user 
#A user can have access to many workouts. Many workouts may be accomplished by many users. 
class Profile(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usersProfile")
    workouts = models.ManyToManyField(Workout)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    weight_lbs = models.CharField(max_length=5, null=True)
    img = models.CharField(max_length=1000, default="https://lh3.googleusercontent.com/proxy/6X3eRz-kEjYAZqTAJ1Ae_kywd-NSXFYJ8DfCzgbHU1v_t6lnBrZmISVCb5f3lcboXPQgYRCclrH1Zqr_qXAMHPMU-ghr2jBm8WS80adIvovHl19DdhozFYVsw60HSw")
    age = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.user.username 

#1 Tracker to many entries 
#1 tracker to one profile 
class Tracker(Model): 
    date = models.DateTimeField(auto_now_add=True)
    date.editable = True 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.date.strftime("%B-%d-%Y")

    class Meta:
        # ordering = ["-date"]
         ordering = ["date"]


#1 entry per 1 exercise . 1 tracker to many entries 
class Entry(Model): 
    date = models.DateTimeField(auto_now_add=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set1 = models.CharField(max_length=2, default=0)
    set2 = models.CharField(max_length=3, default=0)
    set3 = models.CharField(max_length=3, default=0)
    set4 = models.CharField(max_length=3, default=0)
    set5 = models.CharField(max_length=3, default=0)
    notes = models.TextField(max_length=500, default="none")
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE, related_name="entries")

    def __str__(self):
        return f'{self.tracker.date.strftime("%B-%d-%Y")} - {self.exercise.name}'










