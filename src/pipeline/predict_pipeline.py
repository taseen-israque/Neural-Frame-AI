import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        property_type: str,
        Section: str,
        
        Bedrooms: float,
        Bathrooms: float,
        Floor_area: float,
        Floor_no: float):

        self.property_type = property_type

        self.Section = Section

        self.Bedrooms = Bedrooms

        self.Bathrooms = Bathrooms

        self.Floor_area = Floor_area

        self.Floor_no = Floor_no

        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "property_type": [self.property_type],
                "Section": [self.Section],
                "Bedrooms": [self.Bedrooms],
                "Bathrooms": [self.Bathrooms],
                "Floor_area": [self.Floor_area],
                "Floor_no": [self.Floor_no]
               
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)