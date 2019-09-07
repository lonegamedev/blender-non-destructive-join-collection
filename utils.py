bl_info = {
    "version" : (0, 0, 1),
    "blender" : (2, 80, 0)
}

import bpy, bmesh

#check if object is mesh
def is_mesh(obj):
    if obj:
        if obj.type == "MESH" :
            return True
    return False

#get selected collection
def get_sel_collection(context):
    #do we have collection selected
    if context.collection.name in bpy.data.collections:
        #get meshes from selected collection
        depsgraph = context.evaluated_depsgraph_get()
        sel_collection = bpy.data.collections[context.collection.name]
        return sel_collection
    return None

#get meshes from collection
def get_collection_meshes(collection, recursive):
    result = [obj for obj in collection.objects if is_mesh(obj)]
    if recursive:
        for col in collection.children:
            result += get_collection_meshes(col, recursive)
    return result

#get bmeshes from collection
def get_collection_bmeshes(collection, depsgraph, recursive):
    meshes = get_collection_meshes(collection, recursive)
    result = []
    for me in meshes:
        bm = bmesh.new()
        bm.from_object(me,depsgraph,True)
        bm.transform(me.matrix_world)
        result.append(bm)
    return result

#join list of bmeshes
#from https://github.com/nortikin/sverchok (GPL3 license)
def bmesh_join(list_of_bmeshes, normal_update=False):

    bm = bmesh.new()
    add_vert = bm.verts.new
    add_face = bm.faces.new
    add_edge = bm.edges.new

    for bm_to_add in list_of_bmeshes:
        offset = len(bm.verts)

        for v in bm_to_add.verts:
            add_vert(v.co)

        bm.verts.index_update()
        bm.verts.ensure_lookup_table()

        if bm_to_add.faces:
            for face in bm_to_add.faces:
                add_face(tuple(bm.verts[i.index+offset] for i in face.verts))
            bm.faces.index_update()

        if bm_to_add.edges:
            for edge in bm_to_add.edges:
                edge_seq = tuple(bm.verts[i.index+offset] for i in edge.verts)
                try:
                    add_edge(edge_seq)
                except ValueError:
                    # edge exists!
                    pass
            bm.edges.index_update()

    if normal_update:
        bm.normal_update()

    return bm

def join_collection(context, recursive):

    sel_collection = get_sel_collection(context)
    if sel_collection == None:
        return False

    depsgraph = context.evaluated_depsgraph_get()
    bmesh_list = get_collection_bmeshes(sel_collection, depsgraph, recursive)

    if len(bmesh_list) < 1 :
        return False

    final_mesh_name = "Joined_"+sel_collection.name+"_Mesh"
    final_object_name = "Joined_"+sel_collection.name
    if recursive:
        final_mesh_name += "_Recursive"
        final_object_name += "_Recursive"

    mesh_data = bpy.data.meshes.new(final_mesh_name)
    final_bmesh = bmesh_join(bmesh_list, True)
    final_bmesh.to_mesh(mesh_data)

    final_obj = bpy.data.objects.new(final_object_name, mesh_data)
    sel_collection.objects.link(final_obj)

    #delect all and select constructed object
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
    final_obj.select_set(True)
    bpy.context.view_layer.objects.active = final_obj
    #set origin to cursor
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    return True