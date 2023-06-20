# Databricks notebook source
# Databricks notebook source
import requests,json
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

api_response = requests.get('https://api.datamuse.com/words?ml=ringing+in+the+ears')
auth = HTTPBasicAuth('user', 'pass')
headers = {'Authorization': 'abcde12345'}
data = api_response.json()
df = spark.createDataFrame(data)
type(df)
df.printSchema()
df.write.saveAsTable("api_table")
