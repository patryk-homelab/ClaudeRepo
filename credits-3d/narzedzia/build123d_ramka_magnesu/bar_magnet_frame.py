from build123d import *
# Bar magnet frame for Printables 1051202 (Carlos Gonzalez, CC BY), rebuilt with clearance.
# Original BAR_MAGNET_FRAME_60X10: outer 66 x 16 x 2.8 mm, opening exactly 60.0 x 10.0 mm (zero clearance for a 60 x 10 x 3 mm magnet).
# Here: same outer size and height, opening 60.4 x 10.4 mm (0.2 mm per side).
OUT_L, OUT_W, H = 66.0, 16.0, 2.8
MAG_L, MAG_W, CLR = 60.0, 10.0, 0.2
with BuildPart() as frame:
    Box(OUT_L, OUT_W, H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    Box(MAG_L + 2 * CLR, MAG_W + 2 * CLR, H, align=(Align.CENTER, Align.CENTER, Align.MIN), mode=Mode.SUBTRACT)
f = frame.part
show(f, 'magnet_frame')
print(round(f.volume, 3), f.bounding_box().size)
