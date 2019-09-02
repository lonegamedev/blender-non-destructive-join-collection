bl_info = {
    "name": "Collection Join",
    "author": "lonegamedev",
    "description": "Joins collection into single mesh, without destroying existing objects.",
    "category": "Object",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "wiki_url": "https://lonegamedev.com/blender/object_collection_join"
}

if "bpy" in locals():
    import importlib
    importlib.reload(utils)
else:
    from . import utils

import bpy

class menu_collection_join_objects(bpy.types.Operator):
    bl_idname = "collection.join_objects"
    bl_label = "Join"
    def execute(self, context):
        utils.join_collection(context, False)
        return {'FINISHED'}

class menu_collection_join_objects_recursive(bpy.types.Operator):
    bl_idname = "collection.join_objects_recursive"
    bl_label = "Join Recursive"
    def execute(self, context):
        utils.join_collection(context, True)
        return {'FINISHED'}

def menu_draw(self, context):
    self.layout.separator()
    self.layout.operator(menu_collection_join_objects.bl_idname)
    self.layout.operator(menu_collection_join_objects_recursive.bl_idname)

def register():
    bpy.utils.register_class(menu_collection_join_objects)
    bpy.utils.register_class(menu_collection_join_objects_recursive)
    bpy.types.OUTLINER_MT_collection.append(menu_draw)

def unregister():
    bpy.utils.unregister_class(menu_collection_join_objects)
    bpy.utils.unregister_class(menu_collection_join_objects_recursive)
    bpy.types.OUTLINER_MT_collection.remove(menu_draw)