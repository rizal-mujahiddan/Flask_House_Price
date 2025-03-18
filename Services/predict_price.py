import joblib
import pandas as pd

model_ml = joblib.load('Model_ML/RFRegressor_pipeline.joblib')

def predict_ml(dict_x):
    data_ser = pd.Series(dict_x)
    data_df = data_ser.to_frame().T
    hasilnya = model_ml.predict(data_df)
    print(hasilnya)
    return hasilnya