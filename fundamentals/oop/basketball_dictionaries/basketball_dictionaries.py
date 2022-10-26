
# TODO Challenge 1: Update the Constructor
class Player:
    def __init__(self, playerInfo):
        self.name = playerInfo['name']
        self.age = playerInfo['age']
        self.position = playerInfo['position']
        self.team = playerInfo['team']

    # TODO NINJA BONUS: Add a get_team(cls, team_list) @classmethod
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for person in team_list:
            new_team.append(cls(person))
        return new_team


# TODO Challenge 2. Create instances using individual player dictionaries
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

# !Test
# print(f"{player_jason}\n{player_kevin}\n{player_kyrie}")


# TODO Challenge 3. Make a list of Player instances from a list of dictionaries
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

# !TEST
# for player in new_team:
#     print(f"{player.name} - Age:{player.age} - {player.position.capitalize()} - {player.team.upper()}")


# TODO NINJA BONUS: Add a get_team(cls, team_list) @classmethod

teamList = Player.get_team(players)
print(teamList[0])

# !TEST
# for player in teamList:
#     print(f"{player.name} - Age:{player.age} - {player.position.capitalize()}")