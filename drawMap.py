import bpy
import xml.etree.ElementTree as ET


# load data from file
xml_file_path = "data/map-small.osm"
tree = ET.parse(xml_file_path)
root = tree.getroot()

bounds = root.findall('bounds')[0]
minlat = float(bounds.get('minlat'))
minlon = float(bounds.get('minlon'))


# Iterate over each node element
vertices_data = []
for node in root.findall('node'):
    node_id = node.get('id')
    lat = float(node.get('lat')) - minlat
    lon = float(node.get('lon')) - minlon
    
    vertices_data.append({"id": int(node_id), "lat": float(lat), "lon": float(lon)})

# create vertices coordinates for blender
vertices_coordinates = []
for vertex in vertices_data:
    vertices_coordinates.append((vertex['lat'], vertex['lon'], 0))


# Create a dictionary to map IDs to indices
id_to_index = {obj["id"]: index for index, obj in enumerate(vertices_data)}


# Iterate over each way element
ways_data = []
for way in root.findall('way'):
    # check if this way is a hightway
    if not any(tag.attrib.get('k') == 'highway' for tag in way.findall('tag')):
        continue

    last_node = None
    next_node = None
    for nd in way.findall('nd'):
        next_node = int(nd.get('ref'))
        if last_node:
            ways_data.append((id_to_index.get(last_node), id_to_index.get(next_node)))

        last_node = next_node
    #     print(nd.get('ref'))
    # print()


# load into blender
mesh = bpy.data.meshes.new(name="VerticesMesh")
obj = bpy.data.objects.new(name="VerticesObject", object_data=mesh)
bpy.context.collection.objects.link(obj)
mesh.from_pydata(vertices_coordinates, ways_data, [])
mesh.update()