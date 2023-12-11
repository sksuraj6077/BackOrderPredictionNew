import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor1.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor1=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor1.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(  self,
        national_inv: int,
        lead_time: int,
        in_transit_qty,
        forecast_3_month: str,
        forecast_6_month: str,
        forecast_9_month: int,
        sales_1_month: int,
        sales_3_month,
        sales_6_month,
        sales_9_month,
        min_bank,
        potential_issue,
        pieces_past_due,
        perf_6_month_avg,
        perf_12_month_avg,
        local_bo_qty,
        deck_risk,
        oe_constraint,
        ppap_risk,
        stop_auto_buy,
        rev_stop
        ):

        self.national_inv = national_inv

        self.lead_time = lead_time

        self. in_transit_qty =  in_transit_qty

        self.forecast_3_month = forecast_3_month 

        self.forecast_6_month = forecast_6_month

        self.forecast_9_month = forecast_9_month

        self.sales_1_month = sales_1_month

        self.sales_3_month = sales_3_month

        self.sales_6_month = sales_6_month

        self.sales_9_month = sales_9_month

        self.min_bank = min_bank

        self.potential_issue = potential_issue

        self.pieces_past_due = pieces_past_due

        self. perf_6_month_avg =  perf_6_month_avg

        self.perf_12_month_avg = perf_12_month_avg

        self.local_bo_qty = local_bo_qty

        self.deck_risk = deck_risk

        self.oe_constraint = oe_constraint

        self.ppap_risk = ppap_risk

        self.stop_auto_buy = stop_auto_buy

        self.rev_stop = rev_stop


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "national_inv": [self.national_inv],
                "lead_time": [self.lead_time],
                "in_transit_qty": [self.in_transit_qty],
                "forecast_3_month": [self.forecast_3_month],
                "forecast_6_month": [self.forecast_6_month],
                "forecast_9_month": [self.forecast_9_month],
                "sales_1_month": [self.sales_1_month],
                "sales_3_month":[self.sales_3_month],
                "sales_6_month":[self.sales_6_month],
                "sales_9_month":[self.sales_9_month],
                "min_bank":[self.min_bank],
                "potential_issue":[self.potential_issue],
                "pieces_past_due":[self.pieces_past_due],
                "perf_6_month_avg":[self.perf_6_month_avg],
                "perf_12_month_avg":[self.perf_6_month_avg],
                "local_bo_qty":[self.local_bo_qty],
                "deck_risk":[self.deck_risk],
                "oe_constraint":[self.oe_constraint],
                "ppap_risk":[self.ppap_risk],
                "stop_auto_buy":[self.stop_auto_buy],
                "rev_stop":[self.rev_stop]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)