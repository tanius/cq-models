import cadquery as cq
from math import sin, cos, acos, radians, degrees
from types import SimpleNamespace as Measures

# A parametric Z axis end stop spacer for the Creality Ender 2 and Ender 3 3D printers.
#
# This spacer is to be glued with its mountplate face to the x axis assembly of the 3D printer, so that its spacer 
# section is placed between the points that usually touch when Z-homing. This way, you can compensate for adding a 
# (typically) 2-4 mm thick glass plate on the print bed, which otherwise can exceed the capacity of the bed levelling 
# screws. Such a spacer is a much easier solution than changing the mounting height of the Z endstop itself.
#
# Print with the largest surface to the bottom. Mounting works well with a drop of hotglue.
#
# Inspired by "Ender Z End-Stop Spacer" by ctheroux, https://www.thingiverse.com/thing:3152395 .
#
# To use this design, you need Python, CadQuery (https://cadquery.readthedocs.io/en/latest/) and 
# ideally also CQ-Editor, the CadQuery IDE (https://github.com/CadQuery/CQ-editor).
#
# License: Unlicence and Creative Commons Public Domain Dedication (CC-0).

m = Measures(
    width = 15.0,
    mountplate_depth= 2.4,
    spacer_depth = 5.2,
    mountplate_height = 21.0,
    spacer_height = 4.0,
    top_radius = 4.0
)

model = (
    cq.Workplane("XY")
    .rect(m.width, m.spacer_depth)
    .extrude(m.spacer_height)
    .center(0, -0.5 * m.spacer_depth)
    .rect(m.width, m.mountplate_depth)
    .extrude(m.mountplate_height)
    .edges("|Y").edges(">Z")
    .fillet(m.top_radius)
)

# Display the CAD model. Only works when opening the file in CQ-Editor.
show_options = {"color": "lightgray", "alpha": 0.0}
show_object(model, name = "model", options = show_options)
