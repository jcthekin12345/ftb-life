import xml.etree.ElementTree as ET

tree = ET.parse("player_data.xml")
root_element = tree.getroot()

with open("player_data.xml") as f:
    tree = ET.parse(f)
    root_element = tree.getroot()

for age in root_element.iter("age"):

    print(age.text)
