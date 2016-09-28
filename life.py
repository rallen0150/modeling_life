# This program is set up to simulate how well a pitcher does against a lineup.
# How it turns out will be determined on how each player practiced during the week
#   and how much downtime they spent which reduces their performance.

class Player:

    def __init__(self, name, practice, down_time):
        self.name = name
        self.practice = practice
        self.down_time = down_time

    def performance(self):
        self.performance = self.practice - self.down_time

    def __str__(self):
        return self.name

class Team:

    def __init__(self):
        self.bat_team = []
        self.pitchers = []

    def add_batters(self, batters):
        self.bat_team.append(batters)

    def add_pitchers(self, pitcher):
        self.pitchers.append(pitcher)


    def at_bat(self):
        for pitcher in self.pitchers:
            homerun = 0
            triple = 0
            double = 0
            single = 0
            out = 0
            for batter in self.bat_team:
                if batter.performance >= (pitcher.performance + 20):
                    homerun += 1
                elif batter.performance >= (pitcher.performance + 10):
                    triple += 1
                elif batter.performance >= (pitcher.performance + 5):
                    double += 1
                elif batter.performance >= pitcher.performance:
                    single += 1
                else:
                    out += 1
            print("Against Pitcher: {}".format(pitcher.name))
            print("Homerun: {}\nTriples: {}\nDoubles: {}\nSingle: {}\nOuts: {}".format(homerun, triple, double, single, out))

    def __str__(self):
        return self.bat_team.name
