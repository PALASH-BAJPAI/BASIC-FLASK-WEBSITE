from flask import Flask,render_template
ourapp=Flask(__name__)
@ourapp.route("/")
def home():
    return render_template("home.html")

@ourapp.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    ourapp.run(debug=True)
