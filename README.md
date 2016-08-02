# HL Data Warehouse Updates

### Getting Started
Before you can begin, make sure you have [pip](https://pip.pypa.io/en/stable/installing/).

You can also run the included <strong>get-pip.py</strong> file:
```shell
python get-pip.py
```

With pip confirmed, install the only dependency: BeautifulSoup

```shell
pip install bs4
```

Now you're ready to go!

### Instructions


To use this tool:
  1. Download the appropriate 'GeographicAreas' KML file from the [HRSA Warehouse](https://datawarehouse.hrsa.gov/data/datadownload.aspx). --> One of 3: 'HPSA - Dental Health', 'HPSA - Mental Health', or 'HPSA - Primary Care'
  2. Import the DataUpdate.tbx toolbox into ArcMap or ArcCatalog
  3. Right click on the Parse_Popups script, and select 'Properties'. Go to the 'Source' tab, and point the script file's source to the 'parse.py' file in this repo.
  4. Run the Parse_Popups Script, passing in the KML file as your input data and naming an appropriate output feature class.

###### If Arc Desktop isn't your thing, you can also:

Run the python script (watch for schema locks!), and inspect the resulting Feature Class for the new fields and values.

```shell
python parse.py <pathToYourKML> <pathToANewFeatureClass>
```

example:

```shell
python parse.py HPSA_Dental_Health.kmz C:/Users/lcotner/Documents/ArcGIS/Default.gdb/HPSA_Dental_Health_parse1
```

*Make sure that feature class param lives in a real .gdb, we are deleting our intermediate data and gdb at the end of the script.

To-Do:
  >1. Unittests: for missing data, for range out of bounds, for different user parameters
  >2. Dynamicize the soup's findAll functions. It won't always be the same td elements we grab...I don't think.
