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
    images_data = mongo.db.images_data.find_one()
    weather_data = mongo.db.weather_data.find_one()
    facts_data = mongo.db.facts_data.find_one()
    return render_template("index.html", text="Mission to Mars", news_data=news_data, images_data=images_data, weather_data=weather_data, facts_data=facts_data)

@app.route("/scrape")
def scrape():
    # Scrape for mars news data
    news_data = mongo.db.news_data
    news_scrape_data = scrape_mars.scrape_news()
    news_data.update({}, news_scrape_data, upsert=True)

    # Scrape for mars images data
    images_data = mongo.db.images_data
    images_scrape_data = scrape_mars.scrape_images()
    images_data.update({}, images_scrape_data, upsert=True)

    # Scrape for mars weather data
    weather_data = mongo.db.weather_data
    weather_scrape_data = scrape_mars.scrape_weather()
    weather_data.update({}, weather_scrape_data, upsert=True)

    # Scrape for mars facts data
    facts_data = mongo.db.facts_data
    facts_scrape_data = scrape_mars.scrape_facts()
    facts_data.update({}, facts_scrape_data, upsert=True)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)