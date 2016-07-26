# HL Data Warehouse Updates

### Getting Started
Before you can begin, make sure you have [pip](https://pip.pypa.io/en/stable/installing/).

Install all the only dependencies: BeautifulSoup

```shell
pip install bs4
```

Now you're ready to go!

### Instructions
Download the appropriate 'GeographicAreas' KML file from the [HRSA Warehouse](https://datawarehouse.hrsa.gov/data/datadownload.aspx).
###### One of 3: HPSA - Dental Health, HPSA - Mental Health, or HPSA - Primary Care

Create an ArcGIS Feature Geodatabase in This Folder: 'data.gdb'

Add the KML into the gdb:
  1. Import the KML (or KMZ) file into the ArcGIS ecosystem via the [KML To Layer](http://pro.arcgis.com/en/pro-app/tool-reference/conversion/kml-to-layer.htm) GP tool, found in the Conversion Tools Toolbox.
  2. Copy the resulting Feature Class into the database, renaming it appropriately (see what the 'fc' variable is pointing to in the correct script).
  3. Ensure that your environmental variables are pointing to the proper paths and feature class names: Workspace, fc, updated_fc.

Run the appropriate python tool (watch for schema locks!), and inspect the resulting Feature Class for the new fields and values.

```shell
python parse.py
```

To-Do:
  >1. Add the KMZ into the script; user specifies 1 input and 1 output FC name
  >2. Combine 3 scripts into 1, change hardcoded paths
  >3. Turn this script into a Arc Desktop tool, paramatize the input and outputs
  >4. Unittests: for missing data, for range out of bounds, for different user parameters
  >5. Dynamicize the soup's findAll functions. It won't always be the same td elements we grab...I don't think.
