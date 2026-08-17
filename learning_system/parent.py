class User:

    def __init__(self,name,email,userid):
        self.name = name;
        self.email = email;
        self.userid = userid;

    def display_user(self,name,email,userid):
        print(f"name : {name}")
        print(f"email: {email}")
        print(f"userid: {userid}")


