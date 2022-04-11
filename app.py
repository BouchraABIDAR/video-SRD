from flask import Flask, render_template, request, redirect, url_for, flash
from model import *
import time
import uuid
import random
import os

app = Flask(__name__)

path = os.path.abspath( os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(path , 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(SECRET_KEY=os.urandom(24))

db.init_app(app)
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

@app.before_first_request
def create_table():
    db.create_all()
    
@app.route('/')
def index():
    all_data = Video.query.all()
    pages = Page.query.all()
    return render_template("index.html", all_data = all_data, pages = pages)

@app.route('/create_page', methods = ['POST'])
def create_page():
    if request.method == 'POST':
        name = request.form['name']
        created_at = str(time.time())
        id = uuid.uuid4()
        my_page = Page(created_at, id, name)
        db.session.add(my_page)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        title = request.form['title']
        page_id = request.referrer
        created_at = time.time()
        id = uuid.uuid4()
        id_insight = next(uniqueid())
        likes = request.form['likes']
        views = request.form['views']
        
        my_data = Video(created_at, id, id_insight, title, page_id, likes, views)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('index'))
    
    
@app.route('/update', methods = ['POST'])
def update():
    if request.method == "POST":
        my_date = Video.query.get(request.form.get('id'))
        my_date.title = request.form['title']
        #my_date.page_id = request.form['page id']
        my_date.page_id = request.referrer
        my_date.likes = request.form['likes']
        my_date.views = request.form['views']
        db.session.commit()
        return redirect(url_for('index'))
    
@app.route('/delete_page/<id>/')
def delete_page(id):
    my_page = Page.query.get(id)
    db.session.delete(my_page)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>/')
def delete(id):
    my_data = Video.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True, host = 5000)
