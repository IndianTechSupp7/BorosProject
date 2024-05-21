import json

class Auth():
    def __init__(self, *, usrers_path = "users.json"):
        self.users_path = usrers_path
        self.user = None

    @staticmethod
    def load_json(path):
        with open(path, "r") as f:
            data = json.load(f)
        return data


    def validate(self, useranme, password):
        user = {
            "username" : useranme,
            "password" : password,
        }
        data = self.load_json(self.users_path)
        if user in data["users"]:
            self.user = user
            return True
        return False

    def add_user(self, useranme, password):
        user = {
            "username": useranme,
            "password": password,
        }
        data = self.load_json(self.users_path)
        validate = [True for i in data["users"] if i["username"] == user["username"]]
        if validate:
            return "Használt felhasználónév!"
        with open(self.users_path, "w") as file:
            data["users"].append(user)
            json.dump(data, file)

if __name__ == '__main__':
    auth = Auth(usrers_path="../users.json")
    print(auth.add_user("asdasd", "1234"))

