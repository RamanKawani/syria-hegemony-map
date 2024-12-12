from flask import Blueprint
from controllers.mapController import get_region_influence

map_routes = Blueprint('map_routes', __name__)

@map_routes.route('/api/region/<region_name>')
def region_influence(region_name):
    return get_region_influence(region_name)
