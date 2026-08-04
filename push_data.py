import os 
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca =certifi.where()#certificate autorities

import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e :
            raise NetworkSecurityException(e,sys)

    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = json.loads(data.to_json(orient="records"))
            return records


        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def InsertDataMongoDB(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)

            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return(len(self.records))


        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__=='__main__':
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE="DIPESH"
    Collection="NetworkData"

    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.InsertDataMongoDB(records,DATABASE,Collection)
    print(no_of_records)