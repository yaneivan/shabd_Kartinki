import cv2
import numpy as np

def cut_image(img, out_size, verbose=False):
	
	parts = []

	if verbose:
		count = 0
		img_copy = np.copy(img)

	for i in range(img.shape[0]//out_size):
		for j in range(img.shape[1]//out_size):
			h0 = i*128
			h1 = (i+1)*128
			w0 = j*128
			w1 = (j+1)*128
			
			part = img[h0:h1, w0:w1]

			parts.append(part)
			if verbose:
				cv2.rectangle(img_copy, (w0,h0), (w1,h1), (0, 255, 0), 2)
				cv2.putText(img_copy, str(i) + ";" + str(j) + "=" + str(count), (int(w0+out_size/5), int(h0 + out_size/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
				count += 1
	if verbose:
		cv2.imshow("Lol", img_copy)
		cv2.waitKey(0)

	return parts
