import bpy

class smooth_monkey_panel(bpy.types.Panel):
    """The smooth monkey add panel"""
    bl_label = "Smooth Monkey"
    bl_idname = "OBJECT_PT_smooth_monkey"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Test Addon"
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Add smooth monkey named:")
        col.prop( context.scene, "smooth_monkey_name", text="", icon="MESH_MONKEY")
        p = col.operator('mesh.add_smooth_monkey')
        p.name = context.scene.smooth_monkey_name
