from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'created_at')
    list_filter = ('created_at', 'age')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('_id', 'created_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('User Information', {
            'fields': ('_id', 'username', 'email', 'password')
        }),
        ('Personal Details', {
            'fields': ('first_name', 'last_name', 'age', 'goals')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin configuration for Team model"""
    list_display = ('name', 'created_by', 'member_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('_id', 'created_at')
    ordering = ('-created_at',)
    
    def member_count(self, obj):
        """Display the number of members in the team"""
        return len(obj.members) if obj.members else 0
    member_count.short_description = 'Members'
    
    fieldsets = (
        ('Team Information', {
            'fields': ('_id', 'name', 'description')
        }),
        ('Team Management', {
            'fields': ('created_by', 'members')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for Activity model"""
    list_display = ('activity_type', 'user_id', 'duration', 'distance', 'calories', 'date', 'created_at')
    list_filter = ('activity_type', 'date', 'created_at')
    search_fields = ('user_id', 'activity_type', 'notes')
    readonly_fields = ('_id', 'created_at')
    ordering = ('-date',)
    
    fieldsets = (
        ('Activity Information', {
            'fields': ('_id', 'user_id', 'activity_type', 'date')
        }),
        ('Activity Details', {
            'fields': ('duration', 'distance', 'calories', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin configuration for Leaderboard model"""
    list_display = ('username', 'rank', 'points', 'total_activities', 'total_duration', 'total_distance', 'last_updated')
    list_filter = ('last_updated',)
    search_fields = ('username', 'user_id')
    readonly_fields = ('_id', 'last_updated')
    ordering = ('-points',)
    
    fieldsets = (
        ('User Information', {
            'fields': ('_id', 'user_id', 'username')
        }),
        ('Statistics', {
            'fields': ('total_activities', 'total_duration', 'total_distance', 'total_calories')
        }),
        ('Ranking', {
            'fields': ('points', 'rank')
        }),
        ('Timestamps', {
            'fields': ('last_updated',)
        }),
    )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin configuration for Workout model"""
    list_display = ('name', 'activity_type', 'difficulty_level', 'duration', 'created_at')
    list_filter = ('activity_type', 'difficulty_level', 'created_at')
    search_fields = ('name', 'description', 'activity_type')
    readonly_fields = ('_id', 'created_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Workout Information', {
            'fields': ('_id', 'name', 'description')
        }),
        ('Workout Details', {
            'fields': ('activity_type', 'difficulty_level', 'duration')
        }),
        ('Exercise Information', {
            'fields': ('exercises', 'target_muscle_groups', 'equipment_needed')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )
