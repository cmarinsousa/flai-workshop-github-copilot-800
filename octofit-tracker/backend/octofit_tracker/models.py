from django.db import models
from bson import ObjectId


class User(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=str(ObjectId()))
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    goals = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username


class Team(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=str(ObjectId()))
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.CharField(max_length=24)
    members = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=str(ObjectId()))
    user_id = models.CharField(max_length=24)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in kilometers
    calories = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.activity_type} - {self.date}"


class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=str(ObjectId()))
    user_id = models.CharField(max_length=24)
    username = models.CharField(max_length=100)
    total_activities = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # in minutes
    total_distance = models.FloatField(default=0.0)  # in kilometers
    total_calories = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['-points']
    
    def __str__(self):
        return f"{self.username} - {self.points} points"


class Workout(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=str(ObjectId()))
    name = models.CharField(max_length=100)
    description = models.TextField()
    activity_type = models.CharField(max_length=50)
    difficulty_level = models.CharField(max_length=20)  # beginner, intermediate, advanced
    duration = models.IntegerField()  # in minutes
    exercises = models.JSONField(default=list)
    target_muscle_groups = models.JSONField(default=list)
    equipment_needed = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return f"{self.name} - {self.difficulty_level}"
