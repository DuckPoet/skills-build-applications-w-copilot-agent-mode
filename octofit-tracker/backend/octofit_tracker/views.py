from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout

class UserListView(APIView):
    # This function retrieves a list of all users.
    def get(self, request):
        users = User.objects.all()
        user_data = [{"username": user.username, "email": user.email} for user in users]
        return Response(user_data)

class TeamListView(APIView):
    # This function retrieves a list of all teams.
    def get(self, request):
        teams = Team.objects.all()
        team_data = [{"name": team.name, "members": [member.username for member in team.members]} for team in teams]
        return Response(team_data)

class ActivityListView(APIView):
    # This function retrieves a list of all activities.
    def get(self, request):
        activities = Activity.objects.all()
        activity_data = [{"user": activity.user.username, "activity_type": activity.activity_type, "duration": activity.duration} for activity in activities]
        return Response(activity_data)

class LeaderboardListView(APIView):
    # This function retrieves the leaderboard data.
    def get(self, request):
        leaderboard = Leaderboard.objects.all()
        leaderboard_data = [{"user": entry.user.username, "score": entry.score} for entry in leaderboard]
        return Response(leaderboard_data)

class WorkoutListView(APIView):
    # This function retrieves a list of all workouts.
    def get(self, request):
        workouts = Workout.objects.all()
        workout_data = [{"name": workout.name, "description": workout.description} for workout in workouts]
        return Response(workout_data)