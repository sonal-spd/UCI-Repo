from pydantic import BaseModel
from typing import Optional

class Disease(BaseModel):
    age : int
    sex : int
    chest_pain_type : int
    resting_bp : int
    chol : int
    fbs : int
    resting_electrocardio_results : int
    max_heart_rate : int
    exang : int
    ST_depression : float
    slope : int
    ca : int 
    thal : int

class DiseaseResponse(BaseModel):
    target : int
    