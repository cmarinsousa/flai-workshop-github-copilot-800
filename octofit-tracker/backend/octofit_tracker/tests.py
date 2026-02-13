from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import datetime


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            _id=str(ObjectId()),
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            age=25,
            goals='Get fit'
        )
    
    def test_user_creation(self):
        """Test user creation"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(str(self.user), 'testuser')


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            _id=str(ObjectId()),
            name='Test Team',
            description='A test team',
            created_by=str(ObjectId()),
            members=[]
        )
    
    def test_team_creation(self):
        """Test team creation"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            _id=str(ObjectId()),
            user_id=str(ObjectId()),
            activity_type='running',
            duration=30,
            distance=5.0,
            calories=300,
            notes='Morning run',
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        """Test activity creation"""
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.duration, 30)


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        self.leaderboard_entry = Leaderboard.objects.create(
            _id=str(ObjectId()),
            user_id=str(ObjectId()),
            username='testuser',
            total_activities=10,
            total_duration=300,
            total_distance=50.0,
            total_calories=3000,
            points=100
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry creation"""
        self.assertEqual(self.leaderboard_entry.username, 'testuser')
        self.assertEqual(self.leaderboard_entry.points, 100)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            _id=str(ObjectId()),
            name='Morning Cardio',
            description='A cardio workout',
            activity_type='cardio',
            difficulty_level='beginner',
            duration=30,
            exercises=['jumping jacks', 'burpees'],
            target_muscle_groups=['legs', 'core'],
            equipment_needed=[]
        )
    
    def test_workout_creation(self):
        """Test workout creation"""
        self.assertEqual(self.workout.name, 'Morning Cardio')
        self.assertEqual(self.workout.difficulty_level, 'beginner')


class UserAPITest(APITestCase):
    """API test cases for User viewset"""
    
    def test_create_user(self):
        """Test creating a user via API"""
        url = '/api/users/'
        data = {
            'username': 'apiuser',
            'email': 'api@example.com',
            'password': 'apipass123',
            'first_name': 'API',
            'last_name': 'User',
            'age': 28
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_users(self):
        """Test listing users via API"""
        url = '/api/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITest(APITestCase):
    """API test cases for Team viewset"""
    
    def test_create_team(self):
        """Test creating a team via API"""
        url = '/api/teams/'
        data = {
            'name': 'API Team',
            'description': 'Team created via API',
            'created_by': str(ObjectId()),
            'members': []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_teams(self):
        """Test listing teams via API"""
        url = '/api/teams/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """API test cases for Activity viewset"""
    
    def test_create_activity(self):
        """Test creating an activity via API"""
        url = '/api/activities/'
        data = {
            'user_id': str(ObjectId()),
            'activity_type': 'cycling',
            'duration': 45,
            'distance': 15.0,
            'calories': 450,
            'date': datetime.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_activities(self):
        """Test listing activities via API"""
        url = '/api/activities/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """API test cases for Leaderboard viewset"""
    
    def test_list_leaderboard(self):
        """Test listing leaderboard via API"""
        url = '/api/leaderboard/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """API test cases for Workout viewset"""
    
    def test_create_workout(self):
        """Test creating a workout via API"""
        url = '/api/workouts/'
        data = {
            'name': 'API Workout',
            'description': 'Workout created via API',
            'activity_type': 'strength',
            'difficulty_level': 'intermediate',
            'duration': 40,
            'exercises': ['push-ups', 'squats'],
            'target_muscle_groups': ['chest', 'legs'],
            'equipment_needed': ['dumbbells']
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_workouts(self):
        """Test listing workouts via API"""
        url = '/api/workouts/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
