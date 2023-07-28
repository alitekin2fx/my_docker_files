"""
    @package
    Generate a csv BOM list.
    Components are sorted by ref and grouped by value
    Fields are (if exist)
    Quantity, References, Value, Footprint, Brand, Part Number
"""
# python "/media/ali-teke/KiCad-Sources/kicad-scripts/bom3.py" "%I" "%O"

from __future__ import print_function

import re
import sys
import csv
sys.path.append("/media/ali-tekin/KiCadSources/kicad-sources/eeschema/plugins/python_scripts/")
import kicad_netlist_reader

def isEqualComp(self, other):
    result = True
    if getRealValue(self, self.getField("Brand")) != getRealValue(other, other.getField("Brand")):
        result = False
    elif getRealValue(self, self.getField("Part Number")) != getRealValue(other, other.getField("Part Number")):
        result = False

    return result

def getRealValue(component, value):
    obj = re.search('\${(.*?)}', value)
    if obj is None:
        return value

    properties = component.element.getChildren('property')
    for property in properties:
        if (property.attributes['name'] == obj.group(1)):
            return property.attributes['value']
            
    return value

csvFile = open(sys.argv[2] + '.csv', 'w')
csvWriter = csv.writer(csvFile, lineterminator='\n', delimiter='\t', quotechar='\"', quoting=csv.QUOTE_ALL )
csvWriter.writerow(['Quantity', 'References', 'Value', 'Footprint', 'Brand', 'Part Number'])

kicad_netlist_reader.comp.__eq__ = isEqualComp
net = kicad_netlist_reader.netlist(sys.argv[1])
for group in net.groupComponents(net.getInterestingComponents()):
    refs = []
    values = []
    for component in group:
        refs.append(component.getRef())
        value = getRealValue(component, component.getValue())
        if (value not in values):
            values.append(value)

    brand = getRealValue(component, component.getField("Brand"))
    partNumber = getRealValue(component, component.getField("Part Number"))
    if (brand != '' or partNumber != ""):
        columns = []
        columns.append(len(group))
        columns.append(", ".join(refs));
        columns.append(", ".join(values))
        columns.append(net.getGroupFootprint(group))
        columns.append(brand)
        columns.append(partNumber)
        csvWriter.writerow(columns)

csvFile.close()

