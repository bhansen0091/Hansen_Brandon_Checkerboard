from flask import Flask, render_template
app = Flask(__name__)

import math

# @app.route("/")
# @app.route("/<int:num_x>")
# @app.route("/<int:num_x>/<int:num_y>")
# def play_x_times(num_x = 8, num_y = 8):
#     order = []
#     for x in range(0,int(num_y)):
#         order.append(x)
#     return render_template("index.html", times = int(num_x), sequence = order)

@app.route("/")
@app.route("/<int:num_x>")
@app.route("/<int:num_x>/<int:num_y>")
def play_x_times(num_x = 8, num_y = 8):
    return render_template("index.html", times = int(num_x), sequence = num_y)

if __name__=="__main__":
    app.run(debug=True)