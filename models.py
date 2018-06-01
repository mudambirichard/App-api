from app.all_requests import all_requests


class Request:

    def __init__(self, name, email, password):
         self.name = name
         self.password = password
         self.email = email

    def save(self):
        self.id = all_requests[-1]['id']+1
        all_requests.append(self.get_details())


    def get_details(self):
        return{
        'id' : self.id,
        'name' : self.name,
        'password' : self.password,
        'email' : self.email

    }














  














