from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/Promotions/')
def list_promotions():
    RequestedUser = User(float(request.args['Years']), float(request.args['Balance']), float(request.args['Rating']),
                         float(request.args['Age']), request.args['AccountType'])

    if not validate_user(RequestedUser):
        return "Bad Input", 400

    return jsonify(determine_promotions(RequestedUser))


def validate_user(User):
    try:
        float(User.Balance)
        if not (float(User.Years) > 0 and float(User.Rating) > 0 and float(User.Age) > 0):
            return False
    except ValueError:
        return False

    if User.AccountType not in {'Blue', 'Gold', 'Platinum'}:
        return False

    return True


def determine_promotions(User):
    MyResults = Results()

    def rule1(User):
        if 21 <= User.Age <= 35:
            if User.Rating >= 600 or User.Balance > 10000:
                return True
        return False

    def rule2(User):
        if User.Age >= 65:
            if User.Rating >= 500 or User.Balance > 5000:
                if User.Years >= 10 or (User.AccountType in {'Gold', 'Platinum'}):
                    return True
        return False

    def rule3(User):
        if User.Years > 5 and GoodStanding(User):
            return True
        return False

    def rule4(User):
        if GoodStanding(User) and not (rule1(User) or rule2(User) or rule3(User)):
            return True
        return False

    def GoodStanding(User):
        if User.AccountType == 'Platinum':
            return True
        if User.Rating > 500 and User.Balance >= 0:
            return True
        return False

    if rule1(User):
        MyResults.Promotions.append("Millennial Madness")

    if rule2(User):
        MyResults.Promotions.append("Golden Oldies")

    if rule3(User):
        MyResults.Promotions.append("Loyalty Bonus")

    if rule4(User):
        MyResults.Promotions.append("Valued Customer")

    if len(MyResults.Promotions) == 0:
        MyResults.Promotions.append("No Promotions!")

    return MyResults.Promotions


class Results:
    def __init__(self):
        self.Promotions = []


class User:
    def __init__(self, Years, Balance, Rating, Age, AccountType):
        self.Years = Years
        self.Balance = Balance
        self.Rating = Rating
        self.Age = Age
        self.AccountType = AccountType


if __name__ == '__main__':
    app.run()
