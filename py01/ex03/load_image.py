from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)
        img_arr = np.array(img, dtype=np.int32)
        print("The shape of image is:", img_arr.shape)
        print(img_arr)
        img_cropped = img.crop((450, 100, 850, 500))
        img_gray = img_cropped.convert('L')
        img_arr = np.array(img_gray, dtype=np.int32)
        img_arr = img_arr.reshape(400, 400)
        print("New shape after slicing:", img_arr.shape)
        print(img_arr)
        img_arr_stacked = np.stack((img_arr, img_arr, img_arr), axis=-1)
        plt.imshow(img_arr_stacked)
        plt.show()
        return img_arr

    except Exception as e:
        print(f'이미지 로드 중 에러 발생: {e}')
        return None