import numpy as np 
import cv2

from visual_odometry import PinholeCamera, VisualOdometry

# 1) KITTI Dataset
# 2) College Library Indoors
# 3) Indoor Hallway

print("1. KITTI Dataset")
print("2. College Library Indoors")
print("3. Indoor Hallway")

selection = 1
selection = input("Enter your choice number: ")

cam = PinholeCamera(1241.0, 376.0, 718.8560, 718.8560, 607.1928, 185.2157) 

if selection == "1":
	cam = PinholeCamera(1241.0, 376.0, 718.8560, 718.8560, 607.1928, 185.2157) 

elif selection == "2" or selection == "3":
	cam = PinholeCamera(1080.0, 1920.0, 718.8560, 718.8560, 607.1928, 185.2157) #phone camera

vo = VisualOdometry(cam, 'ground_truth.txt')

traj = np.zeros((600,600,3), dtype=np.uint8)

range1 = 4541
range2 = 1363
range3 = 1115

for img_id in range(range3):

	if selection == "1":
		img = cv2.imread('data/kitti/image_0/'+str(img_id).zfill(6)+'.png', 0)

	elif selection == "2":
		img = cv2.imread('data/college-library/'+str(img_id).zfill(6)+'.jpg', 0)

	else:
		img = cv2.imread('data/indoorsample/'+str(img_id).zfill(6)+'.jpg', 0)

	vo.update(img, img_id)

	cur_t = vo.cur_t
	if(img_id > 2):
		x, y, z = cur_t[0], cur_t[1], cur_t[2]
	else:
		x, y, z = 0., 0., 0.
	draw_x, draw_y = int(x)+290, int(z)+90
	true_x, true_y = int(vo.trueX)+290, int(vo.trueZ)+90

	cv2.circle(traj, (draw_x,draw_y), 1, (img_id*255/4540,255-img_id*255/4540,0), 1)
	cv2.rectangle(traj, (10, 20), (600, 60), (0,0,0), -1)
	text = "Coordinates: x=%2fm y=%2fm z=%2fm"%(x,y,z)
	cv2.putText(traj, text, (20,40), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, 8)

	cv2.imshow('Camera View', img)
	cv2.imshow('Trajectory', traj)
	cv2.waitKey(1)

cv2.imwrite('map.png', traj)
