from pydantic import BaseModel

class PredictionModel(BaseModel):
    age: float
    trtbps: float
    chol: float
    thalachh: float
    oldpeak: float
    sex_1: bool
    exng_1: bool
    caa_1: bool
    caa_2: bool
    caa_3: bool
    caa_4: bool
    cp_1: bool
    cp_2: bool
    cp_3: bool
    fbs_1: bool
    restecg_1: bool
    restecg_2: bool
    slp_1: bool
    slp_2: bool
    thall_1: bool
    thall_2: bool
    thall_3: bool
