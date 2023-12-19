from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.logger import logging
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    data=CustomData (
        national_inv=(request.form.get('national_inv')),
        lead_time=(request.form.get('lead_time')),
        in_transit_qty=(request.form.get('in_transit_qty')),
        forecast_3_month=(request.form.get('forecast_3_month')),
        forecast_6_month=(request.form.get('forecast_6_month')),
        forecast_9_month=(request.form.get('forecast_9_month')),
        sales_1_month=(request.form.get('sales_1_month')),
        sales_3_month=(request.form.get('sales_3_month')),
        sales_6_month=(request.form.get('sales_6_month')),
        sales_9_month=(request.form.get('sales_9_month')),
        min_bank=(request.form.get('min_bank')),
        potential_issue=(request.form.get('potential_issue')),
        pieces_past_due=(request.form.get('pieces_past_due')),
        perf_6_month_avg=(request.form.get('perf_6_month_avg')),
        perf_12_month_avg=(request.form.get('perf_12_month_avg')),
        local_bo_qty=(request.form.get('local_bo_qty')),
        deck_risk=(request.form.get('deck_risk')),
        oe_constraint=(request.form.get('oe_constraint')),
        ppap_risk=(request.form.get('ppap_risk')),
        stop_auto_buy=(request.form.get('stop_auto_buy')),
        rev_stop=(request.form.get('rev_stop'))        
    )   
    print(data)
    pred_df=data.get_data_as_data_frame()
    #print(CustomData.national_inv)

    logging.info("User Data\n {}".format(pred_df))
    predict_pipeline=PredictPipeline()
    logging.info("Prediction Started")
    results=predict_pipeline.predict(pred_df)
    #print("after Prediction")
    def output(result):
        if result[0]==0:
            logging.info("Output : No")
            return "No"
        else:
            logging.info("Output : Yes")
            return "Yes"
    logging.info("Prediction Completed")
    return render_template('result.html',results=output(results))

    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)        

        
        
        