class user:
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
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already enrolled")
    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("Not enough points!")

emmet = user("emmet", "allen", "ea@gmail", 24)
sophia = user("sophia", "ws", "sws@gmail", 26)
lucy = user("lucy", "ws", "lws@gmail", 23 )


emmet.enroll().spend_points(50).enroll().display_info()
sophia.enroll().spend_points(80).display_info()
lucy.spend_points(40).display_info()
