import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template


app = Flask(__name__)
model = pickle.load(open(r'C:/Users/nacha/Downloads/ML2/mL2/onlineEd.pkl', 'rb'))
scale = pickle.load(open(r'C:/Users/nacha/Downloads/ML2/mL2/onlineEd.pkl','rb'))

@app.route('/') # rendering the html template
def home():
    return render_template('home.html')
@app.route('/predict',methods=["POST","GET"]) # rendering the html template
def predict() :
    return render_template("input.html")

@app.route('/submit',methods=["POST","GET"])# route to show the predictions in a web UI
def submit():
    #  reading the inputs given by the user
    input_feature=[int(x) for x in request.form.values() ]  
    input_feature=[np.array(input_feature)]
    print(input_feature)
    names = ['Gender', 'Education Level', 'Institution Type', 'IT Student', 'Financial Condition', 'Internet Type',
       'Network Type','Device']
    data = pandas.DataFrame(input_feature,columns=names)
    print(data)
     # predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
   
    if (prediction == 0):
        return render_template("output.html",result ="Adaptivity Level is High")
    elif (prediction == 1):
        return render_template("output.html",result ="Adaptivity Level is medium")
    else:
        return render_template("output.html",result = "Adaptivity Level is Low")
     # showing the prediction results in a UI
if __name__=="__main__":
    
    # app.run(host='0.0.0.0', port=8000,debug=True)    # running the app
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True)