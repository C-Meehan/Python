class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name,'\n',self.last_name,'\n',self.email,'\n',self.age,'\n',self.is_rewards_member,'\n',self.gold_card_points)

    def enroll(self):
        if (self.is_rewards_member == True):
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            print(self.is_rewards_member)
            self.gold_card_points = 200
            print(self.gold_card_points)

    def spend_points(self,amount):
        if (amount > self.gold_card_points):
            print(f"Sorry, your current balance is {self.gold_card_points}. Insufficient funds")
        else:
            self.gold_card_points = self.gold_card_points - amount
            print(f"Remaining balance: {self.gold_card_points}")

#Create instance, call display method and enroll method
user_John = User("John", "Doe", "jd@aol.com", 30)
user_John.display_info()
user_John.enroll()

#Create two more instances
user_Renee = User("Renee", "Smith", "rsmith@gmail.com", 21)
user_Alex = User("Alex", "Burris", "aburr@hotmail.com", 40)

#User spends 50 points. Enroll second user and spend 80 points
user_John.spend_points(50)
user_Renee.enroll()
user_Renee.spend_points(80)

#Call display method on all users
user_John.display_info(), user_Renee.display_info(), user_Alex.display_info() 



