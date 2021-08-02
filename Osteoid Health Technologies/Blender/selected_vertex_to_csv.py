#########################################################################
#                                                                       #
#   The selected vertices in a 3d shape in Blender as an output.   #
#                                                                       #
#########################################################################


import bpy
import bmesh
import csv


# Get the active mesh
obj = bpy.context.edit_object
me = obj.data


# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

bm.faces.active = None

# Modify the BMesh, can do anything here...
result = []
count = 0
for v in bm.verts:
    if v.select:
        print(tuple(v.co))
        result.append(v.co)
        count += 1

print(count)
path = 'C:/Users/Yunus Kardaş/Desktop/csv_files/'        
name = 'obj_'

number = '89'

endName = '_land.csv'
outputFile = path + name + number + endName

with open(outputFile, 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(result)

