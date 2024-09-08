import os
from load_image import ft_load

def main():
    path = os.getcwd() + "/animal.jpeg"
    ft_load(path)


if __name__ == "__main__":
    main()