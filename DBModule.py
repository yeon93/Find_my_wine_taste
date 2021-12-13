"""
와인에 대한 정보를 담은 csv 파일 3개에서 중복되지 않는 데이터들을 sqlite db에 저장합니다.
"""
    
import pandas as pd
import sqlite3

class DBModule:
    def __init__(self):  
        data1 = pd.read_csv('wine1.csv').iloc[:, 1:].drop(['description'], axis=1)
        data2 = pd.read_csv('wine2.csv').iloc[:, 1:].drop(['description'], axis=1)
        data3 = pd.read_csv('new_wine.csv').drop(['description'], axis=1)
        data = pd.concat([data1, data2[data1.columns], data3[data1.columns]]).drop_duplicates().reset_index().iloc[:, 1:]
        
        conn = sqlite3.connect('wine.db')
    
        data.to_sql('data', conn, if_exists='replace', index=False)
        conn.commit()
        conn.close()
 