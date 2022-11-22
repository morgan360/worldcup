from django.contrib import admin
from .models import Team, Match, History, Fantasy

# admin.site.register(Teams)
# admin.site.register(Matches)
admin.site.register(History)


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "group",)
    readonly_fields = ["name", "group"]


class MatchAdmin(admin.ModelAdmin):
    list_display = ("team1", "team2", "date", "phase", "team1_score", "team2_score", "winner")
    ordering = ('date',)
    readonly_fields = ["team1", "team2", "date", "phase"]

    def __str__(self):
        return f'{self.team1} vs {self.team2}'


class FantasyAdmin(admin.ModelAdmin):
    list_display = ('student', 'match', 'score1', 'score2')
    # ordering = ('date',)
    # readonly_fields = ["team1", "team2", "date", "phase"]

    def __str__(self):
        return f'{self.team1} vs {self.team2}'


admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Fantasy, FantasyAdmin)
