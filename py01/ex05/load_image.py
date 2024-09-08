from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)
        img_arr = np.array(img, dtype=np.int32)
        print("The shape of image is:", img_arr.shape)
        return img_arr

    except Exception as e:
        print(f'이미지 로드 중 에러 발생: {e}')
        return None