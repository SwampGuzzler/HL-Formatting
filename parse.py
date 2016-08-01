from bs4 import BeautifulSoup
import arcpy
import sys
import os

# Set environment settings
# Workspace = r"D:\apps\HL-formatter"
# arcpy.env.workspace = Workspace
# arcpy.env.scratchWorkspace = r"D:\apps\HL-formatter\InputData.gdb"
arcpy.env.overwriteOutput = True

middle_layer = 'Polygons'

temp_gdb = 'Polygons.gdb'

input_data = os.path.join(arcpy.env.workspace, sys.argv[1])

directory = 'kmz_output'

if not os.path.exists(directory):
    os.makedirs(directory)

arcpy.AddMessage(input_data)
arcpy.AddMessage(directory)


arcpy.KMLToLayer_conversion(input_data, directory, middle_layer)

temp_path = os.path.join(os.getcwd(), directory)

arcpy.AddMessage(temp_path)


print 'Copying features to new Feature Class...'

updated_fc = sys.argv[2]

arcpy.AddMessage(updated_fc)
new_gdb = os.path.join(temp_path, 'Polygons.gdb')

arcpy.AddMessage(os.path.join(new_gdb, 'Polygons'))
arcpy.CopyFeatures_management(os.path.join(new_gdb, 'Polygons'), updated_fc)

if arcpy.Exists(middle_layer):
   arcpy.Delete_management(middle_layer)
   arcpy.AddMessage("Deleting middle_layer")

import shutil

shutil.rmtree(directory)


# Set local variables
inFeatures = updated_fc
fieldName1 = "hpsa_id"
fieldAlias1 = "HPSA ID"
fieldType1 = "TEXT"

fieldName2 = "hpsa_score"
fieldAlias2 = "HPSA Score"
fieldType2 = "LONG"

fieldName3 = "design_type"
fieldAlias3 = "Designation Type"
fieldType3 = "TEXT"

fieldName4 = "hpsa_disc"
fieldAlias4 = "HPSA Discipline"
fieldType4 = "TEXT"

fieldName5 = "date"
fieldAlias5 = "Data As Of"
fieldType5 = "TEXT"

print 'Adding new fields to the Feature Class...'
arcpy.AddMessage("Adding new fields to the Feature Class...")
arcpy.AddField_management(updated_fc, fieldName1, fieldType1,
                          field_alias=fieldAlias1, field_is_nullable="NULLABLE")

arcpy.AddField_management(updated_fc, fieldName2, fieldType2,
                          field_alias=fieldAlias2, field_is_nullable="NULLABLE")

arcpy.AddField_management(updated_fc, fieldName3, fieldType3,
                          field_alias=fieldAlias3, field_is_nullable="NULLABLE")

arcpy.AddField_management(updated_fc, fieldName4, fieldType4,
                          field_alias=fieldAlias4, field_is_nullable="NULLABLE")

arcpy.AddField_management(updated_fc, fieldName5, fieldType5,
                          field_alias=fieldAlias5, field_is_nullable="NULLABLE")


print 'Updating every row and their new field with our Popupinfo value...'
arcpy.AddMessage('Updating every row and their new field with our Popupinfo value...')
xml_field = "Popupinfo"
cursor = arcpy.UpdateCursor(updated_fc)
for row in cursor:
   xml_as_text = row.getValue(xml_field)
   soup = BeautifulSoup(xml_as_text, "html.parser")

   table_data = soup.find_all("td")

   hpsa_id_value = soup.findAll('td')[3:4]
   hpsa_score_value = soup.findAll('td')[5:6]
   design_type_value = soup.findAll('td')[7:8]
   hpsa_disc_value = soup.findAll('td')[9:10]
   date_value = soup.findAll('td')[11:12]
   
   row.setValue(fieldName1, hpsa_id_value[0].get_text())
   row.setValue(fieldName2, int(hpsa_score_value[0].get_text()))
   row.setValue(fieldName3, design_type_value[0].get_text())
   row.setValue(fieldName4, hpsa_disc_value[0].get_text())
   row.setValue(fieldName5, date_value[0].get_text())

   cursor.updateRow(row)


