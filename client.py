import grpc
# import the generated classes
from flask import Flask, render_template, request
import pandas as pd
import service_pb2_grpc
import service_pb2
import json, csv
from io import StringIO
#import platform
from google.protobuf.json_format import MessageToJson,MessageToDict

app = Flask(__name__)

@app.route('/',methods=['GET'])
def data():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    # Parse from argparse
    # create a stub (client)
    stub = service_pb2_grpc.CreateDataStub(channel)

    #Extracting the csv file 
    Time =[]
    Meterusage =[]        
    with open('meterusage.csv', 'r') as data:
        reader = csv.reader(data)
        next(reader, None)
        for stamp,meter in reader:
       #Looping through extracted csv file 
            requestData = service_pb2.GetData(
                time=stamp, meterusage= float(meter))
                 # create a valid request message
            responseData= stub.Loadtimeseries(requestData)
            Time.append(responseData.time)  
            Meterusage.append(responseData.meterusage)
            output = dict(zip(Time,Meterusage))
            #the API output for the frontend
            payload = render_template('data.html', 
                            data=output)
        return payload
        
        
if __name__ == "__main__":
    app.run(debug=True)
  