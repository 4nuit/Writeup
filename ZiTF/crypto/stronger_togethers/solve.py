from PIL import Image
import numpy as np

img1 = np.array(Image.open("proboscis_monkey.png"))
img2 = np.array(Image.open("spider_monkey.png"))
img3 = np.array(Image.open("vervet_monkey.png"))
img4 = np.array(Image.open("squirrel_monkey.png"))

# XOR 
for i in range(1,5):
	for j in range(1,5):
		result = np.bitwise_xor(eval(f'img{i}'), eval(f'img{j}'))
		result_image = Image.fromarray(result.astype('uint8')).convert('RGB')
		result_image.save(f"result_{i}_{j}.jpg")
