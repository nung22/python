class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
    
    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print("Insufficient points.")
        else:
            self.gold_card_points -= amount


user_1 = User("Michael","Scott","mscott@dundermifflin.com",50)
user_1.display_info()
user_1.enroll()
user_2 = User("Jim","Halpert","jhalpert@dundermifflin.com",42)
user_3 = User("Pam","Beesly","pbeesly@dundermifflin.com",42)
user_1.spend_points(50)
user_2.enroll()
user_2.spend_points(80)
for user in [user_1, user_2, user_3]:
    user.display_info()
    print("")
user_1.enroll()
user_3.spend_points(40)