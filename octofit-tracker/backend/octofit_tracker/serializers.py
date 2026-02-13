from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'age', 'goals', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True},
            '_id': {'read_only': True}
        }
    
    def create(self, validated_data):
        # Hash password before saving (in production, use proper hashing)
        user = User(**validated_data)
        user.save()
        return user


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_by', 'members', 'created_at']
        extra_kwargs = {
            '_id': {'read_only': True}
        }


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'notes', 'date', 'created_at']
        extra_kwargs = {
            '_id': {'read_only': True}
        }


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'username', 'total_activities', 'total_duration', 'total_distance', 
                  'total_calories', 'points', 'rank', 'last_updated']
        extra_kwargs = {
            '_id': {'read_only': True}
        }


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'activity_type', 'difficulty_level', 'duration', 
                  'exercises', 'target_muscle_groups', 'equipment_needed', 'created_at']
        extra_kwargs = {
            '_id': {'read_only': True}
        }
