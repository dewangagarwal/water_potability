from flask import Flask, render_template, request,jsonify
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model = pickle.load(open('water_quality_model.pkl', 'rb'))


@app.route("/", methods=['GET']) 


def Home():
    return render_template('sample.html')



@app.route("/predict", methods=['POST'])

def predict():
    
    if request.method == 'POST':
        ph = float(request.form['ph'])
        Hardness=float(request.form['Hardness'])
        Solids=float(request.form['Solids'])
        Chloramines=float(request.form['Chloramines'])
        Sulfate=float(request.form['Sulfate'])
        Conductivity=float(request.form['Conductivity'])
        Organic_carbon=float(request.form['Organic_carbon'])
        # Trihalomethanes=float(request.form['Trihalomethanes'])
        # Turbidity=float(request.form['Turbidity'])
        data = np.array([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,63,4]])
        my_prediction=model.predict(data)
        return render_template('sample.html',prediction=my_prediction[0])
    else:
        return render_template('sample.html')




if __name__=="__main__":
    app.run(debug=True)
