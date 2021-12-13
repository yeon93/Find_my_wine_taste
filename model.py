"""
db에서 데이터를 가져와서, 와인의 평점을 예측하는 머신러닝 모델을 만듭니다.
"""

import DBModule
import sqlite3
import pandas as pd
import category_encoders as ce
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
import pickle

db = DBModule.DBModule()
print('db생성 완료')

def pull_data(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    query = """SELECT * FROM data"""
    cur.execute(query)
    
    result = cur.fetchall()
    
    data = []
    for i in result:
        data.append(i)
    
    conn.close()
    
    return pd.DataFrame(data, columns=['country', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery'])

data = pull_data('wine.db')
print('db에서 데이터 불러오기 완료')

#결측치 제거
data = data[data.country.notnull()]
data = data[data.price.notnull()]
data = data[data.variety.notnull()]
data = data.reset_index().iloc[:, 1:]

#타겟, 특성 분리
target = data.points
features = data.drop('points', axis=1)

#값이 숫자가 아닌 특성들을 encoding
string = ['country', 'designation', 'province', 'region_1', 'region_2', 'variety', 'winery']
encoder = ce.target_encoder.TargetEncoder(cols=string)
encoder.fit(features, target)
features = encoder.transform(features)

#숫자로 변환된 값들을 standardize
standardizer = StandardScaler()
features = standardizer.fit_transform(features)

#모델생성&학습
model = XGBRegressor(learning_rate= 0.1, max_depth= 5, n_estimators= 1000)

model.fit(features, target)

with open('model.pkl','wb') as file:
    pickle.dump(model, file)