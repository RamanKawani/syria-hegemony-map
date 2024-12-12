from flask import jsonify
from models.regionModel import get_region_data

def get_region_influence(region_name):
    region_data = get_region_data(region_name)
    return jsonify(region_data)
