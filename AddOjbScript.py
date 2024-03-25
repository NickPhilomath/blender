import bpy

vertices_coordinates = [
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (1, 1, 0)
]

# Create a new mesh object for the vertices
mesh = bpy.data.meshes.new(name="VerticesMesh")
obj = bpy.data.objects.new(name="VerticesObject", object_data=mesh)
bpy.context.collection.objects.link(obj)

# Create the mesh data for the vertices
mesh.from_pydata(vertices_coordinates, [], [])

# Update the mesh geometry
mesh.update()