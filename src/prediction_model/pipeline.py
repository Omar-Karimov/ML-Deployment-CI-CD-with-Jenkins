from sklearn.pipeline import Pipeline
from prediction_model.config import config
import prediction_model.processing.preprocessing as pp 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

model_pipeline = Pipeline(
    [
        ("mean_imputation", pp.MeanImputation(variables=config.NUM_FEATURES)),  
        ("mode_imputation", pp.ModeImputation(variables=config.CAT_FEATURES)), 
        ("custom_processing", pp.CustomProcessing()),  
        ("drop_features", pp.ColumnDropper(variables_to_drop=config.COLUMNS_TO_DROP)),
        ("label_encoder", pp.CategoricalEncoder(variables=config.FEATURES_TO_ENCODE)),
        ("log_scaling", pp.LogScaler(variables=config.NUM_FEATURES, add_constant=True)),
        ("standard_scale", StandardScaler()), 
        ("logistic_classifier", LogisticRegression(random_state=0))  
    ]
)
