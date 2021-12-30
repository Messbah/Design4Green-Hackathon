from flask import Flask, render_template, request,redirect, Response
import os
import sys
import pymongo

from time import sleep


db_object=0
db_select=0

app = Flask(__name__)
#homepage
@app.route('/')
def index():
	title="Home"
	return render_template('index.html', title=title)


@app.route('/select_criteria')
def select_criteria():
    global db_object
    client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.orrpa.mongodb.net/New_INR?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
    db = client.New_INR
    coll = db.New_INR
    data_selected=coll.find({"Unmissable": 1})
    db_object=data_selected
    data=coll.find({"Unmissable": 0})
    client.close()
    return render_template('demo.html', criterias=data_selected,select_criterias=data)

@app.route('/view_cart',methods = ['GET','POST'])
def view_cart():
    global db_select
    if request.method == 'POST':
      checkbox = request.form.getlist("selected")
      #mandatory=coll.find({"Unmissable": 1})
      #mandatory=db_object
      client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.orrpa.mongodb.net/New_INR?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
      db = client.New_INR
      coll = db.New_INR
      mandatory=coll.find({"Unmissable": 1})
      checked=coll.find({"ID":{"$in":[x for x in checkbox] }} )
      db_select=checked
      client.close()
      #db_object3=checkbox
      return render_template('view_cart.html',mandatory=mandatory, selected=checked)

@app.route('/show_status',methods = ['POST'])
def show_status():
    sort_dict={}
    client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.orrpa.mongodb.net/New_INR?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
    db = client.New_INR
    coll = db.New_INR
    #pr1=[]
    checked_criteria=db_select #coll.find({"ID":{"$in":[x for x in db_object3]}})
    db_object11=coll.find({"Unmissable":1})
    #db_object11=db_object
    phases=["Acquisition","Conception","Realization","Deployment","Administration","Utilisation","Design","Usage","Maintenance","End of Life","Revaluation"]
    for element in db_object11:
        if element["Phases"] in phases:
        #pr1.append(element["Parent"])
            #sort_dict[element["Parent"]].append(element["ID"])
            sort_dict[element["Phases"]]=element["ID"]
    for element in sys.getsizeof(checked_criteria):
        if element["Phases"] in phases:
            sort_dict[element["Phases"]]=element["ID"]
    checked_criteria.rewind()
    db_object11.rewind()
    return render_template('show_status.html',phase_dict=sort_dict.keys(), selected_criteria=checked_criteria,mandatory_criteria=db_object11)




if __name__ == '__main__':
   app.run(debug=True)