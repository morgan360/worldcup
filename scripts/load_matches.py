from stats.models import Team, Match
import csv


def run():
    with open('stats/matches.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        # Teams.objects.all().delete()
        Match.objects.all().delete()

        for row in reader:
            print(row)

            team1, _ = Team.objects.get_or_create(name=row[-3])
            team2, _ = Team.objects.get_or_create(name=row[-2])

            match = Match(date=row[1],
                          phase=row[4],
                          team1=team1,
                          team2=team2)
            match.save()
