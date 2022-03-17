from flask import Flask, request

from udasa import udasa 
from split_csv import split_csv
from datetime import date
from os import path
from flask_restful import reqparse
import boto3

app = Flask(__name__)
app.secret_key = "TDSmartAgri"

today = str(date.today())
t_return = 0 

# parser = reqparse.RequestParser()

# parser.add_argument('')

def get_csv_from_s3():
    session = boto3.Session(
        aws_access_key_id= "AKIAQCHZOOIP3O44VPUY",
        aws_secret_access_key= "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",
    )
    s3 = session.resource('s3')
    s3.Bucket('tdsolution').download_file('dataset_25-11-2021.csv', './dataset_25-11-2021.csv')


@app.route('/get_tsampling', methods = ['GET'])
def get_tsampling():
    return str(t_return)

@app.route('/adaptive_sampling', methods = ['POST'])
def cal_T():
    global t_return

    if path.exists('dataset_25-11-2021.csv') != True: 
        get_csv_from_s3() 
    
    if path.exists('pres_'+ today + '.csv') != True:
        a = split_csv()
        a.create_sensor_csv('dataset_25-11-2021.csv')

    requested_data = request.get_json()
    
    N = requested_data['N']
    i = requested_data['i']
    n = requested_data['n']    

    X = udasa.read_value_from_csv('pres_'+ today + '.csv')
    wN = udasa.initialize_window(N, i, n, X)
    avg_med = udasa.cal_avg_med(wN)
    D = udasa.cal_D(avg_med, wN, n)
    next_T = udasa.cal_next_T(n, D, 7)
    next_T = round(next_T)
    t_return = next_T*1000

    return str(t_return)

if __name__ == '__main__': 
    app.run()