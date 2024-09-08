from load_image import ft_load
from pimp_image import ft_invert
# , ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

array = ft_load("landscape.jpg")
print(type(array))

plt.imshow(array)
plt.show()

ft_invert(array)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)


print(ft_invert.__doc__)
