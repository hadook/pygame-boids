from vector import Vector

v_up = Vector(0, -1)
v_right = Vector(1, 0)
v_down = Vector(0, 1)
v_left = Vector(-1, 0)
v_upleft = Vector(-1, -1)

print("UP:", v_up.as_polar())
print("RIGHT:", v_right.as_polar())
print("DOWN:", v_down.as_polar())
print("LEFT:", v_left.as_polar())
print("UP-LEFT:", v_upleft.as_polar())
