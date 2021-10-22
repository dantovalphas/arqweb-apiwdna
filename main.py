from fastapi import FastAPI
from typing import Optional
import os
import json


app = FastAPI()


@app.get("/")
def read_root():
    return {"GraphsCount": "3", "Widgets": ["SYNC_CHART", "PIE_GRAPH_MAP", "DONUT_3D_GRAPH"]}


@app.get("/api/dashboard")
def read_item(name: str):
    if(name == "PROFITABLE_AND_UNPROFITABLE_SITES"):
        with open('./dashboard/configData_drillDown_donut.json') as json_file:
            data = json.load(json_file)
            return data
    else:
        with open('./dashboard/configData.json') as json_file:
            data = json.load(json_file)
            return data


@app.get("/api/data")
def read_item(sourceData: str):
    if(sourceData == "QUALITY_RENTABILITY_DATA"):
        with open('./data/syncChart.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "QUALITY_RENTABILITY_BY_DATE"):
        with open('./data/pieGraphsMap.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "RENTABILITY_COMPARATION"):
        with open('./data/donut_3d.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "PROFITABLE_AND_UNPROFITABLE_SITES_DATA"):
        with open('./data/sunburst.json') as json_file:
            data = json.load(json_file)
            return data
    else:
        return {"Error": "Data not found"}
