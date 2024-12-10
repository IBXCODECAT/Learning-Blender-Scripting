import bpy

bpy.ops.mesh.primitive_cube_add(size=2)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.subdivide(number_cuts=1)
bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 2
bpy.context.object.modifiers["Subdivision"].render_levels = 2

bpy.ops.object.shade_smooth()