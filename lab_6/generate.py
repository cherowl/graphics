import numpy as np

rotation = lambda rot_angle: np.array([[np.cos(rot_angle), 0, -np.sin(rot_angle)], 
									   [0,                 1,  0                ],
									   [np.sin(rot_angle), 0,  np.cos(rot_angle)]])

angle = 2*np.pi/3
start_angle = np.pi/3

y_start = -0.4
sector_height = 0.8

angle_partitioning = 10
height_partitioning = 10
arcs_horizontal_step = 10


angles = np.linspace(start_angle, start_angle + angle, angle_partitioning)
height_steps = np.linspace(y_start, y_start+sector_height, height_partitioning)

x = np.cos(angles) * 0.5
z = np.sin(angles) * 0.5

parallels = np.array([[[x[i], height, z[i]] for i in range(len(x))] for height in height_steps])
meridians = np.transpose( parallels, (1, 0, 2) )
 
arcs_step = np.linspace(0, 1, arcs_horizontal_step)[1:-1]
arcs = np.empty([2*(arcs_horizontal_step-2), angle_partitioning, 3])

for i in range(arcs_horizontal_step-2):
	arcs[2*i] = parallels[0]*np.array([arcs_step[i], 1, arcs_step[i]])
	arcs[2*i + 1] = parallels[-1]*np.array([arcs_step[i], 1, arcs_step[i]])


cut_horizontal = np.array([[[0, height_steps[i], 0], parallels[i][0]] for i in range(len(height_steps))])
cut_horizontal = np.concatenate((cut_horizontal,  np.dot(cut_horizontal, rotation(-angle))))

cut_vertical = np.array([[arcs[i][0], arcs[i+1][0]] for i in range(0, arcs.shape[0], 2)])

cut_vertical = np.concatenate((cut_vertical,  
							   np.dot(cut_vertical, rotation(-angle)), 
							   np.array([[[0, y_start, 0], [0,y_start+sector_height, 0]]])))


cut_angle = np.array([[[0,y_start,0], parallels[0][i]] for i in range(angle_partitioning)])[1:-1]
cut_angle = np.concatenate((cut_angle, cut_angle+np.array([0, sector_height, 0])))


cuts = np.concatenate((cut_horizontal, cut_vertical, cut_angle))
