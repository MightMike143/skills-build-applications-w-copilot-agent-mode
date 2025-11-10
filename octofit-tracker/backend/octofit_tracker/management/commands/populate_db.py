from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
	help = 'Populate the octofit_db database with test data'

	def handle(self, *args, **options):
		# Delete existing data
		User.objects.all().delete()
		Team.objects.all().delete()
		Activity.objects.all().delete()
		Leaderboard.objects.all().delete()
		Workout.objects.all().delete()

		# Create teams
		marvel = Team.objects.create(name='Marvel')
		dc = Team.objects.create(name='DC')

		# Create users
		users = [
			User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
			User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
			User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
			User.objects.create(name='Batman', email='batman@dc.com', team=dc),
		]

		# Create workouts
		workouts = [
			Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard'),
			Workout.objects.create(name='Agility Boost', description='Agility and flexibility exercises', difficulty='Medium'),
		]

		# Create activities
		Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=timezone.now().date())
		Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date=timezone.now().date())
		Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date=timezone.now().date())
		Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date=timezone.now().date())

		# Create leaderboard
		Leaderboard.objects.create(team=marvel, points=750)
		Leaderboard.objects.create(team=dc, points=800)

		self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))