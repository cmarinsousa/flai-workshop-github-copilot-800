from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        self.stdout.write(self.style.SUCCESS('Connected to MongoDB'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email field
        db.users.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))

        # Insert Teams
        self.stdout.write('Inserting teams...')
        teams = [
            {
                '_id': 1,
                'name': 'Team Marvel',
                'description': 'Avengers assemble! Heroes fighting for justice.',
                'created_at': datetime.now()
            },
            {
                '_id': 2,
                'name': 'Team DC',
                'description': 'Justice League united! Protectors of Earth.',
                'created_at': datetime.now()
            }
        ]
        db.teams.insert_many(teams)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(teams)} teams'))

        # Insert Users
        self.stdout.write('Inserting users...')
        users = [
            # Team Marvel
            {
                '_id': 1,
                'username': 'ironman',
                'email': 'tony@stark.com',
                'first_name': 'Tony',
                'last_name': 'Stark',
                'team_id': 1,
                'total_points': 1250,
                'created_at': datetime.now()
            },
            {
                '_id': 2,
                'username': 'captainamerica',
                'email': 'steve@rogers.com',
                'first_name': 'Steve',
                'last_name': 'Rogers',
                'team_id': 1,
                'total_points': 1180,
                'created_at': datetime.now()
            },
            {
                '_id': 3,
                'username': 'blackwidow',
                'email': 'natasha@romanoff.com',
                'first_name': 'Natasha',
                'last_name': 'Romanoff',
                'team_id': 1,
                'total_points': 1100,
                'created_at': datetime.now()
            },
            {
                '_id': 4,
                'username': 'thor',
                'email': 'thor@asgard.com',
                'first_name': 'Thor',
                'last_name': 'Odinson',
                'team_id': 1,
                'total_points': 1320,
                'created_at': datetime.now()
            },
            {
                '_id': 5,
                'username': 'hulk',
                'email': 'bruce@banner.com',
                'first_name': 'Bruce',
                'last_name': 'Banner',
                'team_id': 1,
                'total_points': 1050,
                'created_at': datetime.now()
            },
            # Team DC
            {
                '_id': 6,
                'username': 'superman',
                'email': 'clark@kent.com',
                'first_name': 'Clark',
                'last_name': 'Kent',
                'team_id': 2,
                'total_points': 1400,
                'created_at': datetime.now()
            },
            {
                '_id': 7,
                'username': 'batman',
                'email': 'bruce@wayne.com',
                'first_name': 'Bruce',
                'last_name': 'Wayne',
                'team_id': 2,
                'total_points': 1350,
                'created_at': datetime.now()
            },
            {
                '_id': 8,
                'username': 'wonderwoman',
                'email': 'diana@prince.com',
                'first_name': 'Diana',
                'last_name': 'Prince',
                'team_id': 2,
                'total_points': 1280,
                'created_at': datetime.now()
            },
            {
                '_id': 9,
                'username': 'flash',
                'email': 'barry@allen.com',
                'first_name': 'Barry',
                'last_name': 'Allen',
                'team_id': 2,
                'total_points': 1150,
                'created_at': datetime.now()
            },
            {
                '_id': 10,
                'username': 'aquaman',
                'email': 'arthur@curry.com',
                'first_name': 'Arthur',
                'last_name': 'Curry',
                'team_id': 2,
                'total_points': 1020,
                'created_at': datetime.now()
            }
        ]
        db.users.insert_many(users)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(users)} users'))

        # Insert Activities
        self.stdout.write('Inserting activities...')
        activities = []
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing']
        activity_id = 1
        
        for user in users:
            # Each user has 3-5 activities
            num_activities = random.randint(3, 5)
            for i in range(num_activities):
                days_ago = random.randint(0, 30)
                activities.append({
                    '_id': activity_id,
                    'user_id': user['_id'],
                    'activity_type': random.choice(activity_types),
                    'duration': random.randint(20, 90),
                    'distance': round(random.uniform(2, 15), 2),
                    'calories': random.randint(150, 800),
                    'date': datetime.now() - timedelta(days=days_ago),
                    'notes': f'Training session for {user["first_name"]}'
                })
                activity_id += 1
        
        db.activities.insert_many(activities)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(activities)} activities'))

        # Insert Workouts
        self.stdout.write('Inserting workouts...')
        workouts = [
            {
                '_id': '1',
                'name': 'Hero Training Basics',
                'description': 'Start your hero journey with basic exercises',
                'difficulty_level': 'Beginner',
                'duration': 30,
                'activity_type': 'Strength',
                'exercises': [
                    {'name': 'Push-ups', 'sets': 3, 'reps': 10},
                    {'name': 'Squats', 'sets': 3, 'reps': 15},
                    {'name': 'Plank', 'sets': 3, 'duration': '30 seconds'}
                ],
                'target_muscle_groups': ['chest', 'legs', 'core'],
                'equipment_needed': ['none'],
                'created_at': datetime.now()
            },
            {
                '_id': '2',
                'name': 'Speed Force Training',
                'description': 'Increase your speed and agility like The Flash',
                'difficulty_level': 'Intermediate',
                'duration': 45,
                'activity_type': 'Cardio',
                'exercises': [
                    {'name': 'Sprint Intervals', 'sets': 5, 'duration': '30 seconds'},
                    {'name': 'Ladder Drills', 'sets': 4, 'reps': 10},
                    {'name': 'Box Jumps', 'sets': 3, 'reps': 12}
                ],
                'target_muscle_groups': ['legs', 'cardio'],
                'equipment_needed': ['ladder', 'box'],
                'created_at': datetime.now()
            },
            {
                '_id': '3',
                'name': 'Super Strength Builder',
                'description': 'Build superhuman strength with this advanced workout',
                'difficulty_level': 'Advanced',
                'duration': 60,
                'activity_type': 'Strength',
                'exercises': [
                    {'name': 'Deadlifts', 'sets': 4, 'reps': 8},
                    {'name': 'Bench Press', 'sets': 4, 'reps': 8},
                    {'name': 'Pull-ups', 'sets': 4, 'reps': 10}
                ],
                'target_muscle_groups': ['back', 'chest', 'arms'],
                'equipment_needed': ['barbell', 'bench', 'pull-up bar'],
                'created_at': datetime.now()
            },
            {
                '_id': '4',
                'name': 'Amazonian Warrior Workout',
                'description': 'Train like Wonder Woman with this warrior routine',
                'difficulty_level': 'Intermediate',
                'duration': 50,
                'activity_type': 'Combat',
                'exercises': [
                    {'name': 'Sword Swings (with weight)', 'sets': 3, 'reps': 15},
                    {'name': 'Shield Pushes (resistance)', 'sets': 3, 'reps': 12},
                    {'name': 'Battle Rope Waves', 'sets': 4, 'duration': '45 seconds'}
                ],
                'target_muscle_groups': ['arms', 'shoulders', 'core'],
                'equipment_needed': ['weighted bar', 'battle rope'],
                'created_at': datetime.now()
            },
            {
                '_id': '5',
                'name': 'Asgardian Endurance',
                'description': 'Build godly endurance with Thor-inspired exercises',
                'difficulty_level': 'Advanced',
                'duration': 55,
                'activity_type': 'Strength',
                'exercises': [
                    {'name': 'Hammer Curls', 'sets': 4, 'reps': 12},
                    {'name': 'Battle Rope Slams', 'sets': 4, 'duration': '40 seconds'},
                    {'name': 'Farmer Walks', 'sets': 3, 'distance': '50 meters'}
                ],
                'target_muscle_groups': ['arms', 'grip', 'core'],
                'equipment_needed': ['dumbbells', 'battle rope', 'kettlebells'],
                'created_at': datetime.now()
            }
        ]
        db.workouts.insert_many(workouts)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(workouts)} workouts'))

        # Insert Leaderboard
        self.stdout.write('Inserting leaderboard...')
        leaderboard = []
        sorted_users = sorted(users, key=lambda x: x['total_points'], reverse=True)
        
        for rank, user in enumerate(sorted_users, start=1):
            user_activities = [a for a in activities if a['user_id'] == user['_id']]
            total_duration = sum(a['duration'] for a in user_activities)
            total_distance = sum(a['distance'] for a in user_activities)
            total_calories = sum(a['calories'] for a in user_activities)
            
            leaderboard.append({
                '_id': rank,
                'rank': rank,
                'user_id': user['_id'],
                'username': user['username'],
                'total_activities': len(user_activities),
                'total_duration': total_duration,
                'total_distance': round(total_distance, 2),
                'total_calories': total_calories,
                'points': user['total_points'],
                'last_updated': datetime.now()
            })
        
        db.leaderboard.insert_many(leaderboard)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(leaderboard)} leaderboard entries'))

        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database Population Complete!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'Teams: {db.teams.count_documents({})}')
        self.stdout.write(f'Users: {db.users.count_documents({})}')
        self.stdout.write(f'Activities: {db.activities.count_documents({})}')
        self.stdout.write(f'Workouts: {db.workouts.count_documents({})}')
        self.stdout.write(f'Leaderboard: {db.leaderboard.count_documents({})}')
        self.stdout.write(self.style.SUCCESS('='*50))

        client.close()
