from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/Promotions/')
def list_promotions():
    user = {}
    user = request.args

    if not validate_user(user):
        return "Bad Input", 401

    requested_user = User(float(request.args['Years']), float(request.args['Balance']), float(request.args['Rating']),
                          float(request.args['Age']), request.args['AccountType'])

    return jsonify(determine_promotions(requested_user))


def validate_user(user):
    try:
        float(user['Balance'])
        if not (float(user['Years']) > 0 and float(user['Rating']) > 0 and float(user['Age']) > 0):
            return False
    except ValueError:
        return False

    if user['AccountType'] not in {'Blue', 'Gold', 'Platinum'}:
        return False

    return True


def determine_promotions(user):
    user_results = Results()

    if rule_millennial(user):
        user_results.Promotions.append("Millennial Madness")

    if rule_oldies(user):
        user_results.Promotions.append("Golden Oldies")

    if rule_loyalty(user):
        user_results.Promotions.append("Loyalty Bonus")

    if rule_valued(user):
        user_results.Promotions.append("Valued Customer")

    if len(user_results.Promotions) == 0:
        user_results.Promotions.append("No Promotions!")

    return user_results.Promotions


def rule_millennial(user):
    if 21 <= user.Age <= 35:
        if user.Rating >= 600 or user.Balance > 10000:
            return True
    return False


def rule_oldies(user):
    if user.Age >= 65:
        if user.Rating >= 500 or user.Balance > 5000:
            if user.Years >= 10 or (user.AccountType in {'Gold', 'Platinum'}):
                return True
    return False


def rule_loyalty(user):
    if user.Years > 5:
        return True
    return False


def rule_valued(user):
    if rule_good_standing(user) and not (rule_millennial(user) or rule_oldies(user) or rule_loyalty(user)):
        return True
    return False


def rule_good_standing(user):
    if user.AccountType == 'Platinum':
        return True
    if user.Rating > 500 or user.Balance >= 0:
        return True
    return False


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
    app.run(processes=6)
