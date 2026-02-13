from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, 
    TeamSerializer, 
    ActivitySerializer, 
    LeaderboardSerializer, 
    WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a specific user"""
        user = self.get_object()
        activities = Activity.objects.filter(user_id=user._id)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        """Add a member to the team"""
        team = self.get_object()
        user_id = request.data.get('user_id')
        if user_id and user_id not in team.members:
            team.members.append(user_id)
            team.save()
            return Response({'status': 'member added'})
        return Response({'error': 'Invalid user_id or already a member'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def remove_member(self, request, pk=None):
        """Remove a member from the team"""
        team = self.get_object()
        user_id = request.data.get('user_id')
        if user_id in team.members:
            team.members.remove(user_id)
            team.save()
            return Response({'status': 'member removed'})
        return Response({'error': 'User is not a member'}, 
                       status=status.HTTP_400_BAD_REQUEST)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing activities
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get activities filtered by user_id"""
        user_id = request.query_params.get('user_id')
        if user_id:
            activities = Activity.objects.filter(user_id=user_id)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'user_id parameter required'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get activities filtered by activity_type"""
        activity_type = request.query_params.get('type')
        if activity_type:
            activities = Activity.objects.filter(activity_type=activity_type)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'type parameter required'}, 
                       status=status.HTTP_400_BAD_REQUEST)


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing leaderboard
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    
    @action(detail=False, methods=['get'])
    def top_users(self, request):
        """Get top N users from leaderboard"""
        limit = int(request.query_params.get('limit', 10))
        top_users = Leaderboard.objects.all().order_by('-points')[:limit]
        serializer = self.get_serializer(top_users, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def user_rank(self, request):
        """Get rank for a specific user"""
        user_id = request.query_params.get('user_id')
        if user_id:
            try:
                leaderboard_entry = Leaderboard.objects.get(user_id=user_id)
                serializer = self.get_serializer(leaderboard_entry)
                return Response(serializer.data)
            except Leaderboard.DoesNotExist:
                return Response({'error': 'User not found in leaderboard'}, 
                               status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'user_id parameter required'}, 
                       status=status.HTTP_400_BAD_REQUEST)


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing workouts
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts filtered by difficulty level"""
        difficulty = request.query_params.get('difficulty')
        if difficulty:
            workouts = Workout.objects.filter(difficulty_level=difficulty)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'difficulty parameter required'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get workouts filtered by activity type"""
        activity_type = request.query_params.get('type')
        if activity_type:
            workouts = Workout.objects.filter(activity_type=activity_type)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'type parameter required'}, 
                       status=status.HTTP_400_BAD_REQUEST)
