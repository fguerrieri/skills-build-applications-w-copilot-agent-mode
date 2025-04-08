from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_data
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = {}
        for user_data in test_data['users']:
            user = User.objects.create(**user_data)
            users[user_data['username']] = user

        # Create teams
        for team_data in test_data['teams']:
            team = Team.objects.create(name=team_data['name'])

        # Create activities
        for activity_data in test_data['activities']:
            user = users[activity_data.pop('username')]
            Activity.objects.create(user=user, **activity_data)

        # Create leaderboard entries
        for leaderboard_data in test_data['leaderboard']:
            user = users[leaderboard_data.pop('username')]
            Leaderboard.objects.create(user=user, **leaderboard_data)

        # Create workouts
        for workout_data in test_data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated successfully with test data.'))
