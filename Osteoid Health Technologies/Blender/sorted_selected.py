#########################################################################
#                                                                       #
#   The selected vertices in a 3d shape in Blender sort as an output.   #
#                                                                       #
#########################################################################


import bpy
import bmesh   #Needs additional import
import csv

result = []

obj = bpy.context.active_object

bpy.ops.object.mode_set(mode='EDIT')  #Processing must be done in EDIT mode
bm = bmesh.from_edit_mesh(obj.data)

#Blender version is 2.Required when 73 or above
if bpy.app.version[0] >= 2 and bpy.app.version[1] >= 73:
    bm.verts.ensure_lookup_table()

#Show the selection order of vertices
count = 0
for e in bm.select_history:
    if isinstance(e, bmesh.types.BMVert) and e.select:
        result.append(obj.data.vertices[e.index].co)
        count += 1
        
print(result)
print(count)

path = 'C:/Users/Yunus Kardaş/Desktop/csv_files/'        
name = 'obj_'

number = '71'

endName = '_land.csv'
outputFile = path + name + number + endName

with open(outputFile, 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(result)

