import os, csv
try:
    from mapnik import Projection, Coord
except ImportError:
    print "See https://github.com/mapnik/mapnik/wiki/Mapnik-Installation"
    print "for instructions on installing mapnik"
    raise

BRITISH_PROJECTION = Projection('+init=epsg:27700')
LAT_KEY, LNG_KEY = 'Latitude', 'Longitude'
_CSV_FOLDER_PATH = 'Data/CSV'
_COLUMN_HEADERS_PATH = 'Doc/Code-Point_Open_Column_Headers.csv'

def file_generator(sub_dir):
    for root, _, files in os.walk(sub_dir):
        for f in files:
            full_path = os.path.join(root, f)
            yield full_path

def eastings_northings_to_lat_lng(eastings, northings):
    c = Coord(eastings, northings)
    c = BRITISH_PROJECTION.inverse(c)
    return c.y, c.x

def post_code_data_generator(code_point_download_location):
    """Generate a dictionary of location data for each post code
    in the United Kingdom, based on the Code-Point Open download from
    https://www.ordnancesurvey.co.uk/opendatadownload/products.html.

    The dictionary will be keyed on the column headers specified in
    the Code-Point Open documentation. In addition, the dictionary
    will have 'Latitude' and 'Longitude' keys for a WGS-84 equivalent
    to the Eastings and Northings supplied by the Ordnance Survey.

    Pass a string representing the absolute path of the unzipped
    Code-Point Open download.
    """
    path = code_point_download_location
    with open(os.path.join(path, _COLUMN_HEADERS_PATH), 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            column_headers = line

    for filename in file_generator(os.path.join(path, _CSV_FOLDER_PATH)):
        with open(filename, 'rb') as f:
            reader = csv.DictReader(f, fieldnames=column_headers)
            for post_code_data in reader:
                eastings = float(post_code_data['Eastings'])
                northings = float(post_code_data['Northings'])
                lat, lng = eastings_northings_to_lat_lng(eastings, northings)
                post_code_data[LAT_KEY] = lat
                post_code_data[LNG_KEY] = lng

                yield post_code_data

