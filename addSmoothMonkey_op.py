import bpy

class OBJECT_OT_add_smooth_monkey(bpy.types.Operator):
    """Adds a smooth monkey to the 3D view"""
    bl_label = "Add smooth monkey"
    bl_idname = "mesh.add_smooth_monkey"
    bl_options = {'REGISTER', 'UNDO'}
    
    smoothness = bpy.props.IntProperty(
        name = "Smoothness",
        default = 2,
        description = "Subsurf level"
        )
    size = bpy.props.FloatProperty(
        name = "Size",
        default = 1,
        description = "Size of monkey added"
        )
    name = bpy.props.StringProperty(
        name = "Name",
        default = "Eddy",
        description = "Name of added monkey"
        )
        
    
    def execute(self, context):
        
        bpy.ops.mesh.primitive_monkey_add(size=self.size)
        bpy.ops.object.shade_smooth()
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = self.smoothness
        bpy.context.object.name = self.name
        
        return {'FINISHED'}