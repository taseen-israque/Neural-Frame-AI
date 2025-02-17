from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page



@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('something.html')
    else:
        data=CustomData(
            property_type=request.form.get('property_type'),
            Section=request.form.get('place'),
            Bedrooms=float(request.form.get('bedrooms')),
            Bathrooms=float(request.form.get('bathrooms')),
            Floor_area=float(request.form.get('area')),
            Floor_no=float(request.form.get('floor')),
            

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('something.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")  