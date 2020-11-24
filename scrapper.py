from flask import Flask, render_template, url_for
import bs_data
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie')
def movie():
    info = bs_data.all_the_movies
    for i in range(len(info)):
        context = random.choice(info)
    return render_template('movie.html',context=context)

@app.route('/all_movies')
def all_movies():
    context = bs_data.all_the_movies
    return render_template('all_movies.html',context=context)



if __name__ == "__main__":
    app.run(debug=True)