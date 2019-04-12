import numpy as np

angle = np.pi/2
start_angle = 0
angle_partitioning = 10
angles = np.linspace(start_angle, start_angle + angle, angle_partitioning)

sector_height = 0.8
height_partitioning = 20
z_start = -0.7
height_steps = np.linspace(z_start, sector_height, height_partitioning)

x = np.cos(angles) * 0.5
y = np.sin(angles) * 0.5

parallels = np.array([[[x[i], y[i], height] for i in range(len(x))] for height in height_steps])
meridians = np.transpose(parallels, (1,0,2))

arcs_horizontal_step = 4

arcs_step = np.linspace(0, 1, arcs_horizontal_step)[1:-1]
arcs = np.empty([2*(arcs_horizontal_step-2), angle_partitioning, 3])

for i in range(arcs_horizontal_step-2):
	arcs[2*i] = parallels[0]*np.array([arcs_step[i], arcs_step[i], 1])
	arcs[2*i + 1] = parallels[-1]*np.array([arcs_step[i], arcs_step[i], 1])

obj_borders = np.array([[[0, 0, parallels[i][j][2]],[parallels[i][j][0],parallels[i][j][1],parallels[i][j][2]]] 
	for i in [-1, 0] for j in [-1,0]]).reshape(8, 3)
# print()
obj_borders = np.concatenate((obj_borders, np.array([obj_borders[0], obj_borders[-2]])))
print(obj_borders)