import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features: pd.DataFrame):
        try:
   
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            defaults = {
                "gender": "male",
                "race_ethnicity": "group A",
                "parental_level_of_education": "high school",
                "lunch": "standard",
                "test_preparation_course": "none"
            }

            for col in categorical_columns:
                if features[col].isnull().any() or features[col].iloc[0] is None:
                    features[col] = features[col].fillna(defaults[col])

            # Transform features
            data_scaled = preprocessor.transform(features)

            # Predict
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        gender: str = None,
        race_ethnicity: str = None,
        parental_level_of_education: str = None,
        lunch: str = None,
        test_preparation_course: str = None,
        reading_score: int = 0,
        writing_score: int = 0
    ):
 
        self.gender = gender or "male"
        self.race_ethnicity = race_ethnicity or "group A"
        self.parental_level_of_education = parental_level_of_education or "high school"
        self.lunch = lunch or "standard"
        self.test_preparation_course = test_preparation_course or "none"
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
