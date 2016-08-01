# HL Data Warehouse Updates

### Getting Started
Before you can begin, make sure you have [pip](https://pip.pypa.io/en/stable/installing/).

Install the only dependency: BeautifulSoup

```shell
pip install bs4
```

Now you're ready to go!

### Instructions


To use this tool:
  1. Download the appropriate 'GeographicAreas' KML file from the [HRSA Warehouse](https://datawarehouse.hrsa.gov/data/datadownload.aspx). --> One of 3: 'HPSA - Dental Health', 'HPSA - Mental Health', or 'HPSA - Primary Care'
  2. Import the DataUpdate.tbx toolbox into ArcMap or ArcCatalog
  3. Run the Parse_Popups Script, passing in the KML file as your input data and naming an appropriate output feature class.

###### If Arc Desktop isn't your thing, you can also:

Run the python script (watch for schema locks!), and inspect the resulting Feature Class for the new fields and values.

```shell
python parse.py <pathToYourKML> <pathToANewFeatureClass>
```

*Make sure that feature class param lives in a real .gdb, we are deleting our intermediate data and gdb at the end of the script.

To-Do:
  >1. Unittests: for missing data, for range out of bounds, for different user parameters
  >2. Dynamicize the soup's findAll functions. It won't always be the same td elements we grab...I don't think.
