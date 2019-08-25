import bpy

f add_object_button(self, context):
    self.layout.operator(
            OBJECT_OT_add_smooth_monkey.bl_idname,
            icon = "MESH_MONKEY"
            )