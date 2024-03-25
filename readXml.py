import xml.etree.ElementTree as ET

# Path to your XML file
xml_file_path = "data/map-small.osm"

# Parse the XML file
tree = ET.parse(xml_file_path)

# Get the root element
root = tree.getroot()

# Iterate over each node element
for node in root.findall('node'):
    # Extract attributes
    node_id = node.get('id')
    lat = node.get('lat')
    lon = node.get('lon')
    
    # Print or process the attributes as needed
    print("Node ID:", node_id)
    print("Latitude:", lat)
    print("Longitude:", lon)
    print()