#using python & flask to create website
    
from flask import Flask, request
from flask import render_template
import os

app = Flask(__name__)

previous_searches = set()

fake_news = ["A banana is a better president than an orange", 
             "Fruit Declares War", 
             "Meat Running Scared"]

@app.route("/")
def show_search_page():
    return render_template("search.html")


@app.route("/search")
def do_search():
    q = request.args.get('query')
    previous_searches.add(q)
    return render_template("result.html", searched_for=q, items = fake_news)

@app.route("/previous")
def show_previous():
    return render_template("previous.html", search_terms = previous_searches)









@app.route("/searchinurl/<query>")
def do_url_search(query):
    return "You searched for {0}".format(query)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
