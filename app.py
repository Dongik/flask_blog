from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient # Database Connector
from bson.objectid import ObjectId

client = MongoClient('39.162.99.200', 27017)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/User/mySpace/flask_blog/blog.db'

db = SQLAlchemy(app)

class Blogpost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
 	title = db.Column(db.String(50))
 	subtitle = db.Column(db.String(50))
 	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime)
	content = db.Column(db.Text)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username



@app.route('/')
def index():
	return render_template('index_webgl.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/post')
def post():
	return render_template('post.html')

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

	return '<h1>Title: {} Subtitle: {} Author: {} Content: {}</h1>'.format(title, subtitle, author, content)


if __name__ == '__main__':
	app.run(debug=True)
