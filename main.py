import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use("TkAgg")
# lllllllllllllllllllllllllllllllllllllll
from scipy.ndimage import gaussian_filter

import cv2
import numpy as np

def apply_oil_painting_effect(image, brush_size=8, levels=6):
    # 对图像应用高斯模糊
    blurred = cv2.GaussianBlur(image, (brush_size, brush_size), 0)

    # 将图像像素离散化为指定级别
    quantized = np.floor(blurred * levels) / levels

    # 返回离散化后的图像
    return quantized

# 创建一个空白画布
canvas_size = 400
canvas = np.ones((canvas_size, canvas_size, 3), dtype=np.uint8) * 255

# 绘制苹果的轮廓
center_x, center_y = canvas_size // 2, canvas_size // 2
radius = min(center_x, center_y) * 0.4
apple_color = (0, 0, 255)  # 蓝色（BGR格式）
cv2.circle(canvas, (center_x, center_y), radius, apple_color, -1)

# 绘制苹果的茎和叶子
stem_color = (0, 255, 0)  # 绿色（BGR格式）
stem_height = radius * 0.6
stem_width = radius * 0.1
leaf_length = radius * 0.4
stem_bottom = (center_x, int(center_y + radius * 0.5))
stem_top = (center_x, int(center_y - stem_height))
leaf_tip = (int(center_x - leaf_length), int(center_y - stem_height * 0.8))
leaf_bottom = (int(center_x + leaf_length), int(center_y - stem_height * 0.8))
leaf_points = np.array([leaf_tip, stem_top, leaf_bottom], np.int32)
cv2.fillPoly(canvas, [leaf_points], stem_color)
cv2.rectangle(canvas, (int(stem_bottom[0] - stem_width / 2), stem_bottom[1]),
              (int(stem_bottom[0] + stem_width / 2), stem_top[1]), stem_color, -1)

# 应用油画效果
oil_painting = apply_oil_painting_effect(canvas)

# 显示绘制结果
cv2.imshow("Oil Painting Apple", oil_painting)
cv2.waitKey(0)
cv2.destroyAllWindows()