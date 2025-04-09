from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Removed admin registration for mongoengine models as they are not compatible with Django's admin system.