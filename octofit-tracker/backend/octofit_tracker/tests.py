from mongoengine import connect, disconnect
from mongoengine.connection import get_db
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        disconnect(alias='default')  # Disconnect any existing connections
        connect(db="test_octofit_db", host="localhost", port=27017)

    def tearDown(self):
        # Drop the test database after each test to avoid duplicate key errors
        db = get_db()
        db.client.drop_database(db.name)

    def test_create_user(self):
        user = User(username="testuser", email="test@example.com", password="password123")
        user.save()
        self.assertEqual(user.username, "testuser")

    # Add a test case to ensure unique constraints are handled properly.
    def test_unique_email_constraint(self):
        user1 = User(email="unique@example.com")
        user1.save()
        user2 = User(email="unique@example.com")
        with self.assertRaises(NotUniqueError):
            user2.save()

class TeamModelTest(TestCase):
    def setUp(self):
        disconnect(alias='default')  # Disconnect any existing connections
        connect(db="test_octofit_db", host="localhost", port=27017)

    def tearDown(self):
        # Drop the test database after each test to avoid duplicate key errors
        db = get_db()
        db.client.drop_database(db.name)

    def test_create_team(self):
        user = User(username="member1", email="member1@example.com", password="password123")
        user.save()
        team = Team(name="Team A", members=[user])
        team.save()
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def setUp(self):
        disconnect(alias='default')  # Disconnect any existing connections
        connect(db="test_octofit_db", host="localhost", port=27017)

    def tearDown(self):
        # Drop the test database after each test to avoid duplicate key errors
        db = get_db()
        db.client.drop_database(db.name)

    def test_create_activity(self):
        user = User(username="testuser", email="test@example.com", password="password123")
        user.save()
        activity = Activity(user=user, activity_type="Running", duration=3600)
        activity.save()
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        disconnect(alias='default')  # Disconnect any existing connections
        connect(db="test_octofit_db", host="localhost", port=27017)

    def tearDown(self):
        # Drop the test database after each test to avoid duplicate key errors
        db = get_db()
        db.client.drop_database(db.name)

    def test_create_leaderboard(self):
        user = User(username="testuser", email="test@example.com", password="password123")
        user.save()
        leaderboard = Leaderboard(user=user, score=100)
        leaderboard.save()
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        disconnect(alias='default')  # Disconnect any existing connections
        connect(db="test_octofit_db", host="localhost", port=27017)

    def tearDown(self):
        # Drop the test database after each test to avoid duplicate key errors
        db = get_db()
        db.client.drop_database(db.name)

    def test_create_workout(self):
        workout = Workout(name="Workout A", description="Test workout")
        workout.save()
        self.assertEqual(workout.name, "Workout A")