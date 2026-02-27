from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, date=date(2024,1,1))
        Activity.objects.create(user=steve, type='swim', duration=45, date=date(2024,1,2))
        Activity.objects.create(user=bruce, type='cycle', duration=60, date=date(2024,1,3))
        Activity.objects.create(user=clark, type='run', duration=50, date=date(2024,1,4))

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='all')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='all')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
