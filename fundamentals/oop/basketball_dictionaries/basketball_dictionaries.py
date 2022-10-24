# Challenge 1: Update the Constructor
class Player:
    def __init__(self, playerInfo):
        self.name = playerInfo['name']
        self.age = playerInfo['age']
        self.position = playerInfo['position']
        self.team = playerInfo['team']

    # NINJA BONUS: Add a get_team(cls, team_list) @classmethod
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for person in team_list:
            new_team.append(Player(person))
        return new_team



# Challenge 2. Create instances using individual player dictionaries
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


# Challenge 3. Make a list of Player instances from a list of dictionaries
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for person in players:
    new_team.append(Player(person))

# TEST
# for player in new_team:
#     print(player.name)


# NINJA BONUS: Add a get_team(cls, team_list) @classmethod

# TEST
#  team_list = Player.get_team(players)
# for player in team_list:
#     print(player.name)



