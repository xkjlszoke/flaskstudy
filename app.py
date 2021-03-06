from flask import Flask, render_template, request, redirect, url_for, session, flash, g, jsonify
from functools import wraps
import sqlite3

app = Flask(__name__)

app.secret_key = 'wrajj forever'
app.database = 'sample.db'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    print posts
    g.db.close()
    return render_template('index.html', posts = posts)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('you were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('you were just logged out!')
    return redirect(url_for('login'))


@app.route('/wxtest', methods=['GET'])
def wxtest():
    result = {
        'imgs':[
            {'src': 'http://wx3.sinaimg.cn/mw690/0069X71Lgy1fj7d54x9mkj30jz0drgnb.jpg'},
            {'src': 'http://wx1.sinaimg.cn/mw690/0069X71Lgy1fj7d55kopuj30hs0hsq3d.jpg'},
            {'src': 'http://wx1.sinaimg.cn/mw690/0069X71Lgy1fj7d55kopuj30hs0hsq3d.jpg'}
        ]
    }
    return jsonify(result)


@app.route('/wxtestpost', methods=['POST'])
def wxtestpost():
    name = request.form['name']
    id = request.form['id']
    print name,id
    result = {
        'name': name+' love jj',
        'id': id + ' is id'
    }
    return jsonify(result)


def connect_db():
    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True)
