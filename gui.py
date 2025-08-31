from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<int:randomnumber>")
def random_number_page(randomnumber):
        return "<h1>You found me!</h1>" \
        "<img src='https://media.giphy.com/media/AAmhvrZzLCz1m/giphy.gif?cid=790b76110nmxzs79jk4hmb91w04kbpq1wlvsasirpe3hduiu&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"


if __name__ == "__main__":
    app.run()