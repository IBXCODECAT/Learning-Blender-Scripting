import bpy

# Define a custom Panel class
class TestPanel(bpy.types.Panel):
    # The label displayed at the top of the panel
    bl_label = "Hello Panel!"
    # A unique identifier for the panel
    bl_idname = "IBX_Hello_Panel"
    # Specifies the area where the panel will appear (3D View)
    bl_space_type = 'VIEW_3D'
    # Specifies the region where the panel will appear (Sidebar)
    bl_region_type = 'UI'
    # The title of the tab in the sidebar where the panel will be located
    bl_category = 'Hello Tab!'

    # Function to define the layout of the panel
    def draw(self, context):
        layout = self.layout  # Access the panel's layout object

        row = layout.row()  # Create a new row in the panel layout

        # Manipulate the row object with various UI elements
        row.label(text="Hello World!", icon='WORLD_DATA')
        row.label(text="Hello Blender!", icon='BLENDER')

# Register the custom panel class with Blender
def register():
    bpy.utils.register_class(TestPanel)

# Unregister the custom panel class to clean up
def unregister():
    bpy.utils.unregister_class(TestPanel)

# Ensure the script can be executed directly
if __name__ == "__main__":
    register()