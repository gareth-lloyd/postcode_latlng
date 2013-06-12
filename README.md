# Postcode Lat-Lng

Parse the Ordnance Survey Code-Point Open postcode data download, and generate
latitudes and longitudes for each postcode.

# Why?

The Ordnance Survey provides a fantastic download of all UK postcodes along
with location and local authority information. However, it does not include
latitude and longitude data, but uses it's own grid reference system. This 
script will parse the OS download and convert these to more conventional
geographic references based on the WGS-84 coordinates system.

# Use

1. Download the Code-Point Open dataset https://www.ordnancesurvey.co.uk/opendatadownload/products.html
2. Unzip it to some directory.
3. Install Mapnik, including the Python bindings https://github.com/mapnik/mapnik/wiki/Mapnik-Installation
4. Pass the directory name from 2 to the `post_code_data_generator()` method.
5. Iterate over the resulting dictionaries and do what you want with the data.


