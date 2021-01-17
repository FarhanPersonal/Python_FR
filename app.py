# Following mosh's lecture 5.19:

point = dict(x=1, y=3)

print(point["x"])
print(point["y"])

point["x"] = 10
print(point["x"])

# point["z"] = 30

print(len(point))

for key in point:
    print(key, point[key])
