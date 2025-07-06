from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector as MDS
import kryotos
import customer as cust
import room
import transactions as tran

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

# Database connection
def get_db_connection():
    connection = MDS.connect(
        host="localhost",
        user="root",
        passwd="Rakshit",
        database="hotel"
    )
    return connection

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('main_menu'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    fobj = open("userdat.txt","r")
    l1=fobj.readlines()
    for i in l1:
        a = i.partition("/")
        if a[0] == username:
            tpass = kryotos.kryptos(password)
            if a[2] == tpass:
                session['username'] = username
                return redirect(url_for('main_menu'))
    return 'Invalid username or password'

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with open("userdat.txt", "w") as fobj:
            data = username + "/" + kryotos.kryptos(password)
            fobj.write(data)
        return redirect(url_for('index'))
    return render_template('new_user.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/main_menu')
def main_menu():
    if 'username' in session:
        return render_template('main_menu.html')
    return redirect(url_for('index'))

@app.route('/customer')
def customer():
    if 'username' in session:
        return render_template('customer.html')
    return redirect(url_for('index'))

@app.route('/customer/new', methods=['GET', 'POST'])
def new_customer():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        cID = request.form['cID']
        name = request.form['name']
        conn = get_db_connection()
        cust.new_cust(conn, cID, name)
        conn.close()
        return redirect(url_for('customer'))
    return render_template('new_customer.html')

@app.route('/customer/update', methods=['GET', 'POST'])
def update_customer():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        tID = request.form['tID']
        cID = request.form['cID']
        name = request.form['name']
        conn = get_db_connection()
        cust.update_cust(conn, tID, cID, name)
        conn.close()
        return redirect(url_for('customer'))
    return render_template('update_customer.html')

@app.route('/customer/delete', methods=['GET', 'POST'])
def delete_customer():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        cID = request.form['cID']
        conn = get_db_connection()
        cust.delete_cust(conn, cID)
        conn.close()
        return redirect(url_for('customer'))
    return render_template('delete_customer.html')

@app.route('/customer/report')
def customer_report():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    records = cust.report_cust(conn)
    conn.close()
    return render_template('customer_report.html', records=records)

@app.route('/room')
def room_management():
    if 'username' in session:
        return render_template('room.html')
    return redirect(url_for('index'))

@app.route('/room/new', methods=['GET', 'POST'])
def new_room():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        roomno = request.form['roomno']
        roontype = request.form['roontype']
        roompri = request.form['roompri']
        conn = get_db_connection()
        room.add_room(conn, roomno, roontype, roompri)
        conn.close()
        return redirect(url_for('room_management'))
    return render_template('new_room.html')

@app.route('/room/update', methods=['GET', 'POST'])
def update_room():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        uroom = request.form['uroom']
        roomno = request.form['roomno']
        roontype = request.form['roontype']
        roompri = request.form['roompri']
        conn = get_db_connection()
        room.update_rooom(conn, uroom, roomno, roontype, roompri)
        conn.close()
        return redirect(url_for('room_management'))
    return render_template('update_room.html')

@app.route('/room/delete', methods=['GET', 'POST'])
def delete_room():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        roomno = request.form['roomno']
        conn = get_db_connection()
        room.delete_room(conn, roomno)
        conn.close()
        return redirect(url_for('room_management'))
    return render_template('delete_room.html')

@app.route('/room/report')
def room_report():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    records = room.report_room(conn)
    conn.close()
    return render_template('room_report.html', records=records)

@app.route('/transaction')
def transaction():
    if 'username' in session:
        return render_template('transaction.html')
    return redirect(url_for('index'))

@app.route('/transaction/checkin', methods=['GET', 'POST'])
def checkin():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        id = request.form['id']
        no = request.form['no']
        conn = get_db_connection()
        tran.check_in(conn, id, no)
        conn.close()
        return redirect(url_for('transaction'))
    return render_template('checkin.html')

@app.route('/transaction/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        id = request.form['id']
        no = request.form['no']
        conn = get_db_connection()
        tran.check_out(conn, id, no)
        conn.close()
        return redirect(url_for('transaction'))
    return render_template('checkout.html')

@app.route('/transaction/report')
def transaction_report():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    records = tran.report_tran(conn)
    conn.close()
    return render_template('transaction_report.html', records=records)

@app.route('/report')
def report_menu():
    if 'username' in session:
        return render_template('report.html')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
