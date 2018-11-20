from flask import *
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>',methods=['GET','POST'])
def profile_page(id):
	if request.method == 'GET':
		name = get_name(id)
		return render_template("cat.html",n = id,name=name)
	else:
		vote=get_vote(id)
		return redirect('/')

@app.route('/cats/createcat', methods=['GET','POST'])
def create_cats():
	if request.method == 'GET':
		return render_template("form.html")
	else:
		name=request.form['firstname']
		create_cat(name, 0)
		return redirect('/')


	


if __name__ == '__main__':
   app.run(debug = True)
