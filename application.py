import sys
from flask import Flask,render_template,request,url_for

from src.logger import logging
from src.exception import CustomException_ANIL

from src.utils import CustomData
from src.pipeline.prediction_pipeline import Predict


application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('welcome.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        logging.info(f"app.py::datapoint:{pred_df}")
        results=Predict().predict(pred_df)
        logging.info(f"app.py::output:{results}")
        
        return render_template('home.html',results=results)
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port="8080")        
