from flask import Flask, render_template, url_for, request, session, redirect  ;
import re, sqlite3
app = Flask(__name__)

  
  
app.secret_key = 'xyzsdfg'
  

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



@app.route('/login', methods =['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully !'
            return render_template('index.html', message = message)
        else:
            message = 'Please enter correct email / password !'
    return render_template('login.html', message = message)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('name', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE email = ?', (email,))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address !'
        elif not userName or not password or not email:
            message = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (?, ?, ?)', (userName, email, password))
            conn.commit()
            message = 'You have successfully registered !'
    elif request.method == 'POST':
        message = 'Please fill out the form !'
    return render_template('register.html', message = message)

@app.route("/exclusives")
def Exclusive():
    if 'loggedin' not in session:
        return render_template('unregistered.html')
    else:
        return render_template('exclusives.html')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/single-blog')
def singleblog():
    return render_template('single-blog.html')
@app.route('/list')
def list():
    return render_template('list.html')


@app.route("/sololeveling", methods=['POST', 'GET'])
def sololeveling():
    volno = request.form.get("chapter")
    return render_template('sololeveling.html', volno=volno)

@app.route("/oyasumipunpun", methods=['POST', 'GET'])
def oyasumipunpun():
    volno = request.form.get("chapter")
    return render_template('oyasumipunpun.html', volno=volno)

@app.route("/spyxfamily", methods=['POST', 'GET'])
def spyxfamily():
    volno = request.form.get("chapter")
    return render_template('spyxfamily.html', volno=volno)

@app.route("/bleach", methods=['POST', 'GET'])
def bleach():
    volno = request.form.get("chapter")
    return render_template('bleach.html', volno=volno)

@app.route("/tokyoghoul", methods=['POST', 'GET'])
def tokyoghoul():
    volno = request.form.get("chapter")
    return render_template('tokyoghoul.html', volno=volno)



if __name__ == '__main__':
    app.run(debug=True)