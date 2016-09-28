from life import Player, Team

team = Team()

for player in range(9):
    name = input("Batter's Name:\n>")
    practice = int(input("How much time dedicated to practice on a scale from 0-100:\n>"))
    downtime = 100 - practice

    player = Player(name, practice, downtime)
    player.performance()

    team.add_batters(player)

print("Batters:")
for player in team.bat_team:
    print(player + "\n")

for player in range(3):
    name = input("Pitcher's Name:\n>")
    practice = int(input("How much time dedicated to practice on a scale from 0-100:\n>"))
    downtime = 100 - practice

    player = Player(name, practice, downtime)
    player.performance()

    team.add_pitchers(player)

print("Pitchers:")
for player in team.pitchers:
    print(player)

team.at_bat()
