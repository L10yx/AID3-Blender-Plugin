import bpy
import math
import time
import os
from mathutils import Vector, Euler

from AID3_addon.addons.AID3_addon.config import __addon_name__
from AID3_addon.addons.AID3_addon.preference.AddonPreferences import ExampleAddonPreferences

from bpy_extras.view3d_utils import region_2d_to_vector_3d, region_2d_to_location_3d

# This Example Operator will scale up the selected object
class ExampleOperator(bpy.types.Operator):
    '''ExampleAddon'''
    bl_idname = "object.example_ops"
    bl_label = "ExampleOperator"

    # 确保在操作之前备份数据，用户撤销操作时可以恢复
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)
        # use operator
        # bpy.ops.transform.resize(value=(2, 2, 2))

        # manipulate the scale directly
        context.active_object.scale *= addon_prefs.number
        # context.active_object.location.x += addon_prefs.number
        # print("hello world!\n")

        return {'FINISHED'}
class ResetOperator(bpy.types.Operator):
    '''Reset the model to its origin'''
    bl_idname = "object.reset_ops"
    bl_label = "Reset"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.location = [0,0,0]
        context.object.rotation_euler = [0,0,0]
        context.active_object.scale = [1,1,1]
        return {'FINISHED'}
class XAxisOperator(bpy.types.Operator):
    '''Move the model along X-axis'''
    bl_idname = "object.x_axis_ops"
    bl_label = "X_Axis_Operator"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.location.x += addon_prefs.number

        return {'FINISHED'}
class YAxisOperator(bpy.types.Operator):
    '''Move the model along Y-axis'''
    bl_idname = "object.y_axis_ops"
    bl_label = "Y_Axis_Operator"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.location.y += addon_prefs.number

        return {'FINISHED'}
class ZAxisOperator(bpy.types.Operator):
    '''Move the model along Z-axis'''
    bl_idname = "object.z_axis_ops"
    bl_label = "Z_Axis_Operator"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.location.z += addon_prefs.number

        return {'FINISHED'}
class XRotateOperator(bpy.types.Operator):
    '''Rotate the model along X-axis'''
    bl_idname = "object.x_rotate_ops"
    bl_label = "X_Rotate"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        # context.active_object.rotation_euler.x += addon_prefs.number * math.pi / 6
        for i in range(100):
            bpy.context.object.rotation_euler[0] += math.pi * 2 / 100
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            time.sleep(1 / 100)


        return {'FINISHED'}
class YRotateOperator(bpy.types.Operator):
    '''Rotate the model along Y-axis'''
    bl_idname = "object.y_rotate_ops"
    bl_label = "Y_Rotate"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        # context.active_object.rotation_euler.x += addon_prefs.number * math.pi / 6
        for i in range(100):
            bpy.context.object.rotation_euler[1] += math.pi * 2 / 100
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            time.sleep(1 / 100)


        return {'FINISHED'}
class ZRotateOperator(bpy.types.Operator):
    '''Rotate the model along Z-axis'''
    bl_idname = "object.z_rotate_ops"
    bl_label = "Z_Rotate"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        # context.active_object.rotation_euler.x += addon_prefs.number * math.pi / 6
        for i in range(100):
            bpy.context.object.rotation_euler[2] += math.pi * 2 / 100
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            time.sleep(1 / 100)


        return {'FINISHED'}
class XExpandOperator(bpy.types.Operator):
    '''Expand the model along X-axis'''
    bl_idname = "object.x_expand_ops"
    bl_label = "X_Expand"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.scale[0] *= addon_prefs.number
        return {'FINISHED'}
class YExpandOperator(bpy.types.Operator):
    '''Expand the model along Y-axis'''
    bl_idname = "object.y_expand_ops"
    bl_label = "Y_Expand"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.scale[1] *= addon_prefs.number
        return {'FINISHED'}
class ZExpandOperator(bpy.types.Operator):
    '''Expand the model along Z-axis'''
    bl_idname = "object.z_expand_ops"
    bl_label = "Z_Expand"

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.scale[2] *= addon_prefs.number
        return {'FINISHED'}
class GenerateOperator(bpy.types.Operator):
    '''Generate a model'''
    bl_idname = "object.generate_ops"
    bl_label = "Generate"

    bl_options = {'REGISTER', 'UNDO'}

    scale: bpy.props.FloatProperty(name="Scale", default=2, min=1, max=10)

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)

        context.active_object.scale *= self.scale
        return {'FINISHED'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        self.scale = 2
        # self.report({'INFO'}, f"mouse_X: {event.mouse_x}, mouse_y:{event.mouse_y}")
        return context.window_manager.invoke_props_dialog(self, width=400)

    # def modal(self, context: bpy.types.Context, event: bpy.types.Event):
class MovingOperator(bpy.types.Operator):
    '''Move the model'''
    bl_idname = "object.move_ops"
    bl_label = "Moving"

    bl_options = {'REGISTER', 'UNDO'}

    # scale: bpy.props.FloatProperty(name="Scale", default=2, min=1, max=10)
    initial_location = None
    mouse_x = 0
    mouse_y = 0

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        mouse_location = (self.mouse_x, self.mouse_y)
        vec = region_2d_to_vector_3d(context.region, context.space_data.region_3d, mouse_location)
        loc = region_2d_to_location_3d(context.region, context.space_data.region_3d, mouse_location, vec)
        context.active_object.location = loc
        return {'FINISHED'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        # self.report({'INFO'}, f"mouse_X: {event.mouse_x}, mouse_y:{event.mouse_y}")
        # return context.window_manager.invoke_props_dialog(self, width=400)
        self.initial_location = context.active_object.location.copy()
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    def modal(self, context: bpy.types.Context, event: bpy.types.Event):
        match event.type:
            case 'MOUSEMOVE':
                # Set the model to follow the mouse
                self.mouse_x = event.mouse_x
                self.mouse_y = event.mouse_y
                self.execute(context)
            case 'LEFTMOUSE':
                # Reach destination
                return {'FINISHED'}
            case 'RIGHTMOUSE' | 'ESC':
                # Cancel the Operation
                context.active_object.location = self.initial_location.copy()
                return {'CANCELLED'}
            case _:
                return {'PASS_THROUGH'}
        return {'RUNNING_MODAL'}
class DancingOperator(bpy.types.Operator):
    '''Dnace the model'''
    bl_idname = "object.dance_ops"
    bl_label = "Dancing"

    bl_options = {'REGISTER', 'UNDO'}

    _timer = None

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        return {'FINISHED'}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        context.window_manager.modal_handler_add(self)
        self._timer = context.window_manager.event_timer_add(0.05, window=context.window)
        return {'RUNNING_MODAL'}

    def modal(self, context: bpy.types.Context, event: bpy.types.Event):
        match event.type:
            case 'TIMER':
                context.active_object.rotation_euler[2] += math.pi * 2 / 100
                return {'RUNNING_MODAL'}
            case 'ESC':
                # Cancel the Operation
                context.window_manager.event_timer_remove(self._timer)
                return {'CANCELLED'}
        return {'PASS_THROUGH'}

class ImportFixedOBJOperator(bpy.types.Operator):
    '''Import a specific .obj file'''
    bl_idname = "object.import_fixed_obj_file"
    bl_label = "Import .obj File"
    bl_options = {'REGISTER', 'UNDO'}

    # 固定文件路径
    filepath = "E:\\Blender\\addon\\obj_test\\initial5.obj"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True

    def execute(self, context: bpy.types.Context):
        try:
            bpy.ops.preferences.addon_enable(module="io_scene_obj")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to enable OBJ import addon: {str(e)}")
            return {'CANCELLED'}

        if 'io_scene_obj' not in bpy.context.preferences.addons:
            self.report({'ERROR'}, "OBJ import addon is not enabled.")
            return {'CANCELLED'}

        # 删除场景中的默认立方体
        bpy.ops.object.select_all(action='DESELECT')
        if 'Cube' in bpy.data.objects:
            bpy.data.objects['Cube'].select_set(True)
            bpy.ops.object.delete()

        # 检查文件路径是否有效
        if not os.path.exists(self.filepath):
            self.report({'ERROR'}, f"File not found: {self.filepath}")
            return {'CANCELLED'}

        # 导入.obj文件
        try:
            bpy.ops.import_scene.obj(filepath=self.filepath)
        except AttributeError as e:
            self.report({'ERROR'}, f"Import operator not found: {str(e)}")
            return {'CANCELLED'}

        return {'FINISHED'}