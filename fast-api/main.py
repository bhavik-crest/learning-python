from typing import Union

from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()

conn = MongoClient("mongodb+srv://bhavikt:hs8sayh7vOyXzTkB@cluster0.8hoyu.mongodb.net")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}