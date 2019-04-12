import numpy as np

angle = np.pi/2
start_angle = 0
angle_partitioning = 10
angles = np.linspace(start_angle, start_angle + angle, angle_partitioning)

sector_height = 0.8
height_partitioning = 20
z_start = -0.7
radius = 0.5
height_steps = np.linspace(z_start, sector_height, height_partitioning)

x = np.cos(angles) * radius
y = np.sin(angles) * radius

parallels = np.array([[[x[i], y[i], height] for i in range(len(x))] for height in height_steps])
meridians = np.transpose(parallels, (1,0,2))

arcs_horizontal_step = 4

arcs_step = np.linspace(0, 1, arcs_horizontal_step)[1:-1]
arcs = np.empty([2*(arcs_horizontal_step-2), angle_partitioning, 3])
print(arcs_step.shape)

for i in range(arcs_horizontal_step-2):
	arcs[2*i] = parallels[0]*np.array([arcs_step[i], arcs_step[i], 1])
	arcs[2*i + 1] = parallels[-1]*np.array([arcs_step[i], arcs_step[i], 1])

print(arcs)