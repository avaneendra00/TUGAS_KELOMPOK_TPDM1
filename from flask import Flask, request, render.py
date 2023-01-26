from flask import Flask, request, render_template
import pickle
import numpy

app = Flask(__name__)

model_file = open('gold.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', Price=0)

@app.route('/predict', methods=['POST'])
def predict():

    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
   
    Kehadiran, Kedisiplinan, Attitude = [x for x in request.form.values()]






    data = []

    data.append(float(Kehadiran))
    data.append(float(Kedisiplinan))
    data.append(float(Attitude))




    prediction = model.predict([data])
    output = round(float(prediction[0]),2)
    
    return render_template('index.html', Jumlah=output, Kehadiran=Kehadiran, Kedisiplinan=Kedisiplinan, Attitude=Attitude)

if __name__ == '__main__':
    app.run(debug=True)