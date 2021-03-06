from flask import Flask, render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient # Database Connector
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient('39.162.99.200', 27017)


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/home/dongik/mySpace/flask_blog/blog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////root/flask_blog/blog.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
 	title = db.Column(db.String(50))
 	subtitle = db.Column(db.String(50))
 	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime)
	content = db.Column(db.Text)

@app.route('/')
def index():
	return render_template('index_webgl.html')

@app.route('/posts')
def posts():
	postList = Blogpost.query.all()
	return render_template('index_old.html', posts=postList)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
	post = Blogpost.query.filter_by(id=post_id).one()
	date_posted = post.date_posted.strftime('%B %d, %Y')
	return render_template('post.html',post=post, date_posted=date_posted)

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
	title = request.form['title']
	subtitle = request.form['subtitle']
	author = request.form['author']
	content = request.form['content']

	post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

	db.session.add(post)
	db.session.commit()

	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
