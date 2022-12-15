import time
import threading
import sqlite3
from Soda import Soda
from SodaMachine import SodaMachine
from db import DB

soda1 = Soda(10, 20, "Дюшес", 20)
soda2 = Soda(3, 0, "Мохито", 30)

machine = SodaMachine(300, 300)

machine.AddNewSoda(soda1)
machine.AddNewSoda(soda2)

machine.AddCoin(50)

machine.SelectSoda(0)


def test():
    while True:
        print("-----------------------------------")
        print("Water:", machine.water)
        print("Syrup:", machine.syrup)
        print("Money:", machine.money)
        print("coinAcceptor", machine.coinAcceptor)
        print("progressWater", machine.progressWater)
        print("progressSyrup", machine.progressSyrup)
        print("-----------------------------------")
        time.sleep(1)

def get_db_connection():
    conn = sqlite3.connect('DB.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    return post


t_elevator = threading.Thread(target=test)
t_elevator.start()

t_elevator1 = threading.Thread(target=machine.Activation)
t_elevator1.start()

