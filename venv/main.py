import time
import threading
import sqlite3
from Soda import Soda
from SodaMachine import SodaMachine
from db import DB
from flask import Flask, render_template, request, make_response


soda1 = Soda(10, 20, "Кола", 20)
soda2 = Soda(5, 2, "Махито", 30)
soda3 = Soda(8, 6, "Дюшес", 10)

machine = SodaMachine(300, 300)

machine.AddNewSoda(soda1)
machine.AddNewSoda(soda2)
machine.AddNewSoda(soda3)


app = Flask(__name__, template_folder='templates')


def get_data():
    data = [
        machine.water,
        machine.syrup,
        machine.money,
        machine.coinAcceptor,
        machine.progressWaterUI,
        machine.progressSyrupUI,
        machine.error,
        machine.result
    ]

    return data


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/info', methods=['GET'])
def getInfo():
    y = get_data()
    message_server = ""

    for i in range(len(y)):
        message_server += str(y[i])
        if i != len(y) - 1:
            message_server += "/"

    res = make_response(message_server)
    res.headers['Content-Type'] = 'text'
    return res


@app.route('/button', methods=['POST'])
def postInfo():
    button = request.args.get('button')
    if button == 'Activation':
        machine.Activation()
    elif button == "AddCoin":
        machine.AddCoin(10)
    elif button == "TakeSoda":
        machine.TakeSoda()
    else:
        machine.SelectSoda(int(button))

    res = make_response()
    return res


if __name__ == '__main__':
    app.run(host='localhost', port=8200, debug=False, use_reloader=False)
