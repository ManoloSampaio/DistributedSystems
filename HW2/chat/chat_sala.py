class ChatRoom():
    def __init__(self):
        self.user_vector = []
    def add_user(self,user_nickname):
        if user not in self.user_vector:
            self.user_vector.append(user_nickname)
    def remove_user(self,user_nickname,user_ip):
        self.user_vector.remove(user_nickname)
    def see_users(self,IP):
        return self.user_vector
        
            
