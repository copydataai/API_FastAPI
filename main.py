"""Define principal use"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'Python', 'none': 'hello'}
