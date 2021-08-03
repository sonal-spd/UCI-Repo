import pandas as pd
from fastapi import FastAPI
from schemas import Disease,DiseaseResponse
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"detail":"please make a post request to /predict"}


@app.post('/predict/',response_model=DiseaseResponse)
def predict(request : Disease):
    
    data = dict(request)
    
    age = request.age
    sex = request.sex
    chest_pain_type = request.chest_pain_type
    resting_bp = request.resting_bp
    chol = request.chol
    fbs = request.fbs
    resting_electrocardio_results = request.resting_electrocardio_results
    max_heart_rate = request.max_heart_rate
    exang = request.exang
    ST_depression = request.ST_depression
    slope = request.slope
    ca = request.ca
    thal = request.thal
    scale = pd.read_pickle('model/scale.pkl')
    temp = []
    columns = ['age', 'resting_bp', 'chol', 'max_heart_rate', 'ST_depression']
    for i in columns:
        temp.append(data[i])
    var = [temp]
    new_data = scale.transform (var)

    age = new_data[0][0]
    resting_bp = new_data[0][1]
    chol = new_data[0][2]
    max_heart_rate = new_data[0][3]
    ST_depression = new_data[0][4]
    # for python 3.8
    model = pd.read_pickle('model/model.pkl')
    
    target = model.predict([[age,sex,chest_pain_type,resting_bp,chol,fbs,resting_electrocardio_results,max_heart_rate,exang,ST_depression,slope,ca,thal]])
    classification = target[0]
    data['target'] = classification
    return data
    # return data


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)