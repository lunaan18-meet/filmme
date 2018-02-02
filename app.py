from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    comments = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/new')
def new():
	return render_template('new.html')

@app.route('/review', methods=['POST', 'GET'])
def review():
	if request.method == 'GET':
		return render_template('review.html')
	else:
		print("HI")
		new_review = Review(first_name=request.form['first_name'], 
							last_name=request.form['last_name'],
							email=request.form['email'],
							comments=request.form['comments'])
		db.session.add(new_review)
		db.session.commit()
		return redirect(url_for('index'))

@app.route('/categories')
def categories():
	return render_template('categories.html')


if __name__ == '__main__':
	app.run(debug=True)	