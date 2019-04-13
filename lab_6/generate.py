import numpy as np

rotation = lambda rot_angle: np.array([[np.cos(rot_angle), -np.sin(rot_angle), 0], 
									   [np.sin(rot_angle),  np.cos(rot_angle), 0],
									   [0,                  0,                 1]])

angle = np.pi/2
start_angle = 0
angle_partitioning = 20

z_start = -0.4
sector_height = 0.8
height_partitioning = 20
arcs_horizontal_step = 20


angles = np.linspace(start_angle, start_angle + angle, angle_partitioning)
height_steps = np.linspace(z_start, z_start+sector_height, height_partitioning)

x = np.cos(angles) * 0.5
y = np.sin(angles) * 0.5

parallels = np.array([[[x[i], y[i], height] for i in range(len(x))] for height in height_steps])
meridians = np.array([[parallels[0][i],parallels[-1][i]] for i in range(len(x))]).reshape(2*len(x), 3)


arcs_step = np.linspace(0, 1, arcs_horizontal_step)[1:-1]
arcs = np.empty([2*(arcs_horizontal_step-2), angle_partitioning, 3])

for i in range(arcs_horizontal_step-2):
	arcs[2*i] = parallels[0]*np.array([arcs_step[i], arcs_step[i], 1])
	arcs[2*i + 1] = parallels[-1]*np.array([arcs_step[i], arcs_step[i], 1])


cut_horizontal = np.array([[[0,0,height_steps[i]], parallels[i][0]] for i in range(len(height_steps))])
cut_horizontal = cut_horizontal.reshape(cut_horizontal.shape[0]*cut_horizontal.shape[1], 3)
cut_horizontal = np.concatenate((cut_horizontal,  np.dot(cut_horizontal, rotation(-angle))))

cut_vertical = np.array([[arcs[i][0], arcs[i+1][0]] for i in range(0, arcs.shape[0], 2)]).reshape(arcs.shape[0], 3)
cut_vertical = np.concatenate((cut_vertical,  
							   np.dot(cut_vertical, rotation(-angle)), np.array([[0, 0, z_start], 
							   [0,0, z_start+sector_height]])))

cut_angle = np.array([[[0,0,z_start], parallels[0][i]] for i in range(angle_partitioning)])[1:-1].reshape((angle_partitioning-2)*2, 3)
cut_angle = np.concatenate((cut_angle, cut_angle+np.array([0, 0, sector_height])))
