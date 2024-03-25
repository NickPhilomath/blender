import bpy
import xml.etree.ElementTree as ET

vertices_coordinates = []

# load data from file
xml_file_path = "data/map-small.osm"
tree = ET.parse(xml_file_path)
root = tree.getroot()

bounds = root.findall('bounds')[0]
minlat = float(bounds.get('minlat'))
minlon = float(bounds.get('minlon'))

# Iterate over each node element
for node in root.findall('node'):
    node_id = node.get('id')
    lat = float(node.get('lat')) - minlat
    lon = float(node.get('lon')) - minlon
    
    vertices_coordinates.append((float(lat), float(lon), 0))


# load into blender
mesh = bpy.data.meshes.new(name="VerticesMesh")
obj = bpy.data.objects.new(name="VerticesObject", object_data=mesh)
bpy.context.collection.objects.link(obj)
mesh.from_pydata(vertices_coordinates, [], [])
mesh.update()