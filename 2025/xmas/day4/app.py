from factory import LeFlagSynthesisRoom
from flask import Flask, render_template, redirect, url_for
from threading import Lock

mutex = Lock()
app = Flask(__name__)

REQUIRED_WORK = 1337133713371337133713371337133713371337
work_counter = 0
flag_room = LeFlagSynthesisRoom()

@app.route('/')
def index():
    with mutex:
        counter = work_counter
        if counter == REQUIRED_WORK:
            gift_state = 'Gift complete: ' + int(''.join(str(b) for b in flag_room.gift_state), 2).to_bytes(24, 'little').decode()
        else:
            gift_state = 'Work In Progress'
    return render_template('index.j2',
                           work_counter=counter,
                           required_work=REQUIRED_WORK,
                           gift_state=gift_state)

@app.route('/help_santa', methods=['POST'])
def help_santa():
    global work_counter
    with mutex:
        if work_counter < REQUIRED_WORK:
            flag_room.work()
            work_counter += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
