from flask import Flask, render_template
import scrape_mars
import pymongo

# Flask
app = Flask(__name__)
conn = 'mongodb://localhost:27017/misson_to_mars'
client = pymongo.MongoClient(conn)

@app.route("/")
def index():
    mars = client.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data)
    

if __name__ == "__main__":
    app.run(debug=True)