from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector as MDS
import kryotos
import customer as cust
import room
import transactions as tran

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

@app.before_request
def make_session_permanent():
    session.permanent = True

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

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return 'Invalid admin credentials'
    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin_logged_in' in session and session['admin_logged_in']:
        return render_template('admin_dashboard.html')
    return redirect(url_for('admin_login'))

def get_users():
    users = []
    try:
        with open("userdat.txt", "r") as fobj:
            for line in fobj:
                username, encrypted_password = line.strip().split('/', 1)
                users.append({'username': username, 'encrypted_password': encrypted_password})
    except FileNotFoundError:
        pass
    return users

@app.route('/admin/users')
def admin_users():
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin_login'))
    users = get_users()
    return render_template('admin_users.html', users=users)

    return render_template('admin_users.html', users=users)

@app.route('/admin/users/add', methods=['GET', 'POST'])
def admin_add_user():
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with open("userdat.txt", "a") as fobj:
            data = "\n" + username + "/" + kryotos.kryptos(password)
            fobj.write(data)
        return redirect(url_for('admin_users'))
    return render_template('admin_add_user.html')

    return render_template('admin_add_user.html')

@app.route('/admin/users/update/<username>', methods=['GET', 'POST'])
def admin_update_user(username):
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin_login'))

    users = get_users()
    user_to_update = next((user for user in users if user['username'] == username), None)

    if not user_to_update:
        return "User not found", 404

    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        updated_users = []
        for user in users:
            if user['username'] == username:
                updated_users.append({'username': new_username, 'encrypted_password': kryotos.kryptos(new_password)})
            else:
                updated_users.append(user)

        with open("userdat.txt", "w") as fobj:
            for user in updated_users:
                fobj.write(f"{user['username']}/{user['encrypted_password']}\n")
        return redirect(url_for('admin_users'))

    return render_template('admin_update_user.html', user=user_to_update)

    return render_template('admin_update_user.html', user=user_to_update)

@app.route('/admin/users/delete/<username>')
def admin_delete_user(username):
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin_login'))

    users = get_users()
    updated_users = [user for user in users if user['username'] != username]

    with open("userdat.txt", "w") as fobj:
        for user in updated_users:
            fobj.write(f"{user['username']}/{user['encrypted_password']}\n")
    return redirect(url_for('admin_users'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

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

@app.route('/customer/update')
def select_customer_to_update():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    customers = cust.report_cust(conn)
    conn.close()
    return render_template('select_customer_to_update.html', customers=customers)

@app.route('/customer/update/<cID>', methods=['GET', 'POST'])
def update_customer(cID):
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    if request.method == 'POST':
        tID = cID # The original ID is passed as cID in the URL
        new_cID = request.form['cID']
        name = request.form['name']
        cust.update_cust(conn, tID, new_cID, name)
        conn.close()
        return redirect(url_for('customer'))
    
    # Fetch the specific customer's data to pre-fill the form
    mycur = conn.cursor()
    mycur.execute("SELECT * FROM CUSTOMERS WHERE CustomerID = '{}'".format(cID))
    customer_data = mycur.fetchone()
    mycur.close()
    conn.close()

    if customer_data:
        return render_template('update_customer.html', customer=customer_data)
    else:
        return "Customer not found", 404

@app.route('/customer/delete', methods=['GET', 'POST'])
def delete_customer():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    if request.method == 'POST':
        cID = request.form['cID']
        cust.delete_cust(conn, cID)
        conn.close()
        return redirect(url_for('customer'))
    
    records = cust.report_cust(conn) # Reuse report_cust to get all customers
    conn.close()
    return render_template('delete_customer.html', customers=records)

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

@app.route('/room/update')
def select_room_to_update():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    rooms = room.report_room(conn)
    conn.close()
    return render_template('select_room_to_update.html', rooms=rooms)

@app.route('/room/update/<roomno>', methods=['GET', 'POST'])
def update_room(roomno):
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    if request.method == 'POST':
        uroom = roomno # The original roomno is passed in the URL
        new_roomno = request.form['roomno']
        roontype = request.form['roontype']
        roompri = request.form['roompri']
        room.update_rooom(conn, uroom, new_roomno, roontype, roompri)
        conn.close()
        return redirect(url_for('room_management'))
    
    # Fetch the specific room's data to pre-fill the form
    mycur = conn.cursor()
    mycur.execute("SELECT * FROM ROOMS WHERE Roomno = '{}'".format(roomno))
    room_data = mycur.fetchone()
    mycur.close()
    conn.close()

    if room_data:
        return render_template('update_room.html', room=room_data)
    else:
        return "Room not found", 404

@app.route('/room/delete', methods=['GET', 'POST'])
def delete_room():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    if request.method == 'POST':
        roomno = request.form['roomno']
        room.delete_room(conn, roomno)
        conn.close()
        return redirect(url_for('room_management'))
    
    records = room.report_room(conn) # Reuse report_room to get all rooms
    conn.close()
    return render_template('delete_room.html', rooms=records)

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

    conn = get_db_connection()
    if request.method == 'POST':
        id = request.form['id']
        no = request.form['no']
        tran.check_in(conn, id, no)
        conn.close()
        return redirect(url_for('transaction'))
    
    customers = cust.report_cust(conn)
    all_rooms = room.report_room(conn)

    # Get occupied rooms from the CUSTOMERS table
    mycur = conn.cursor()
    mycur.execute("SELECT Room FROM CUSTOMERS WHERE Room != '000'")
    occupied_rooms_data = mycur.fetchall()
    mycur.close()
    occupied_room_numbers = [r[0] for r in occupied_rooms_data]

    available_rooms = [r for r in all_rooms if r[0] not in occupied_room_numbers]

    conn.close()
    return render_template('checkin.html', customers=customers, available_rooms=available_rooms)

@app.route('/transaction/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' not in session:
        return redirect(url_for('index'))

    conn = get_db_connection()
    if request.method == 'POST':
        id = request.form['id']
        no = request.form['no']
        tran.check_out(conn, id, no)
        conn.close()
        return redirect(url_for('transaction'))
    
    # Fetch customers who are currently occupying a room
    mycur = conn.cursor()
    mycur.execute("SELECT CustomerID, Name, Room FROM CUSTOMERS WHERE Room != '000'")
    occupied_customers = mycur.fetchall()
    mycur.close()
    conn.close()

    return render_template('checkout.html', occupied_customers=occupied_customers)

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
