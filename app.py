# Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create instance of Flask app
app = Flask(__name__)

# Set up a Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# create route that renders index.html template
@app.route("/")
def home():
    news_data = mongo.db.news_data.find_one()
    return render_template("index.html", text="Mission to Mars", news_data=news_data)

@app.route("/scrape")
def scrape():
    news_data = mongo.db.news_data
    news_scrape_data = scrape_mars.scrape()
    news_data.update({}, news_scrape_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)