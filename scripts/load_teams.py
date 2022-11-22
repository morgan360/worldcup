from stats.models import Team, Match
import csv


def run():
    with open('stats/teams.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Team.objects.all().delete()
        Match.objects.all().delete()

        for row in reader:
            print(row)
            # team, _ = Teams.objects.get_or_create(name=row[-2])

            teamx = Team(group=row[1],
                         name=row[0])
            teamx.save()
