from flask import Flask, render_template, jsonify, request
import sqlite3
import threading
import time

app = Flask(__name__)

@app.route('/') # setting the main connection between this server and index.html
def index():
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    accounts = c.fetchall()
    conn.close()
    return render_template('index.html')

@app.route('/accounts')
def get_accounts():
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    accounts = c.fetchall()
    conn.close()
    return jsonify(accounts)


countTime = 0 #This is to adjust to the bug that update_time() executes twice every hour
def update_time():
    global countTime
    if countTime == 0:
        with app.app_context():
            conn = sqlite3.connect('accounts.db')
            c = conn.cursor()
            c.execute('SELECT * FROM accounts')

            for row in c.fetchall():
                oldVal = row[8] #row[8] -> time
                newVal = oldVal - 1
                c.execute("UPDATE accounts SET time = ? WHERE id = ?", (newVal, row[0])) #row[0] -> id
                conn.commit()
            print('timeMain')
            conn.close()
        countTime = 1
    else:
        countTime = 0
    return 0

def run_update_time():
    while True:
        time.sleep(2) #2/2 = 1 sec (idk why)
        update_time()



if __name__ == '__main__':
    update_thread_time = threading.Thread(target=run_update_time)
    update_thread_time.start()
    app.run(debug=True)