import bpy

from AID3_addon.addons.AID3_addon.config import __addon_name__
from AID3_addon.addons.AID3_addon.operators.AddonOperators import ExampleOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import ResetOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import XAxisOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import YAxisOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import ZAxisOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import XRotateOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import YRotateOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import ZRotateOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import XExpandOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import YExpandOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import ZExpandOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import GenerateOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import MovingOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import DancingOperator
from AID3_addon.addons.AID3_addon.operators.AddonOperators import ImportFixedOBJOperator
from AID3_addon.common.i18n.i18n import i18n


class ExampleAddonPanel(bpy.types.Panel):
    bl_label = "Example Addon Side Bar Panel"
    bl_idname = "SCENE_PT_sample"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    # name of the side panel
    bl_category = "ExampleAddon"

    def draw(self, context: bpy.types.Context):
        addon_prefs = context.preferences.addons[__addon_name__].preferences

        layout = self.layout

        layout.label(text=i18n("Example Functions") + ": " + str(addon_prefs.number))
        layout.prop(addon_prefs, "filepath")
        layout.separator()

        row = layout.row()
        row.prop(addon_prefs, "number")
        row.prop(addon_prefs, "boolean")

        layout.operator(ExampleOperator.bl_idname)
        layout.operator(ResetOperator.bl_idname)
        layout.operator(XAxisOperator.bl_idname)
        layout.operator(YAxisOperator.bl_idname)
        layout.operator(ZAxisOperator.bl_idname)
        layout.operator(XRotateOperator.bl_idname)
        layout.operator(YRotateOperator.bl_idname)
        layout.operator(ZRotateOperator.bl_idname)
        layout.operator(XExpandOperator.bl_idname)
        layout.operator(YExpandOperator.bl_idname)
        layout.operator(ZExpandOperator.bl_idname)
        layout.operator(GenerateOperator.bl_idname)
        layout.operator(MovingOperator.bl_idname)
        layout.operator(DancingOperator.bl_idname)
        layout.operator(ImportFixedOBJOperator.bl_idname)

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None
