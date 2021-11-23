from fastapi import FastAPI
from typing import Optional
import os
import json
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.100.62"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"GraphsCount": "3", "Widgets": ["SYNC_CHART", "PIE_GRAPH_MAP", "DONUT_3D_GRAPH"]}


@app.get("/api/dashboard")
def read_item(name: str):
    if(name == "PROFITABLE_AND_UNPROFITABLE_SITES"):
        with open('./dashboard/configData_drillDown_donut.json') as json_file:
            data = json.load(json_file)
            return data
    elif(name == "RENTABILITY_GIS_DASHBOARD"):
        with open('./dashboard/configData_drillDown_Gis.json') as json_file:
            data = json.load(json_file)
            return data
    elif("PROFITABLE_MARKETS_REGION_" in name):
        with open('./dashboard/configData_drillDown_buble.json') as json_file:
            data = json.load(json_file)
            return data
    elif(name == "DRILLDOWN_TABLE_MARKETS_INCOMES"):
        with open('./dashboard/configData_drillDown_column.json') as json_file:
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
    elif(sourceData == "QUALITY_RENTABILITY_BY_DATE_2"):
        with open('./data/pieGraphsMap_2.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "PROFITABLE_MARKETS_BYREGIONS"):
        with open('./data/buble.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "ESTIMATED_INCOME"):
        with open('./data/heatmap.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "RENTABILITY_BY_MARKET"):
        with open('./data/gis_image.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "RENTABILITY_MARKET_GIS_DATA"):
        with open('./data/gis.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "MOST_PROFITABLE_MARKETS_BY_REVENUE_BY_REGION"):
        with open('./data/table2.json') as json_file:
            data = json.load(json_file)
            return data
    elif(sourceData == "TOP_50_MARKETS"):
        with open('./data/column.json') as json_file:
            data = json.load(json_file)
            return data
    else:
        return {"Error": "Data not found"}
