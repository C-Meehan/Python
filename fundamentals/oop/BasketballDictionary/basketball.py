class Player:

    def __init__(self, player_dictionary):
        self.name = player_dictionary["name"]
        self.age = player_dictionary["age"]
        self.position = player_dictionary["position"]
        self.team = player_dictionary["team"]

    @classmethod
    def creating_team(cls, athletes):
        new_team = []
        for player in athletes:
            new_team.append(cls(player))
            print(player)
        print(new_team)
        return new_team

    def team_creator(self, athletes):
        new_team = []
        for player in athletes:
            new_team.append(Player(player))
            print(player)
        print(new_team)
        return new_team

    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}\n"
        return display


athletes = [
    {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},
    
    {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"},
    
    {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"},
    
    {"name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"},
    
    {"name": "Joel Embiid", "age":32, "position": "Power Foward", "team": "Philidelphia 76ers"},
    
    {"name": "", "age":16, "position": "P", "team": "en"}
]

Player.creating_team(athletes)

# print(new_team)


    # def display_info(self):
    #     display = f"{self.name}"
    #     return display

#     @classmethod
#     def get_team(cls, team_list):
#         for player in players:
#             Player.new_team.append(cls)
#             print(player)
#             Player(player)
#         print(cls.new_team)




# Player.team()

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# jason = {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"}

# kyrie = {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}

# # Create your Player instances here!
# player_jason = Player(jason)
player_kevin = Player(kevin)
# player_kyrie = Player(kyrie)
player_kevin.team_creator(athletes)
# print(player_jason.display_info())

    


#Bridgewater codeeeeeee
# class Players:
#     def __init__(self, player_info):
#         self.name = player_info['name']
#         self.age = player_info['age']
#         self.position = player_info['position']
#         self.team = player_info['team']


# ######  add players
#     @classmethod
#     def add_players(cls, player_info):
#         player_list = []
#         for dict in player_info:
#             player_list.append(cls(dict))
#         return player_list


#Josh W codeeeeee
# @classmethod
#     def get_team(cls, team_list):
#         generated_team = []
#         for player in team_list:
#             generated_team.append(Player(player))
#         return generated_team

