import cv2
import numpy as np
from shapely.geometry import LineString

def equation_of_line(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def get_value_orientation(A, B, D):
    m, b = equation_of_line(A[0], A[1], B[0], B[1])
    orientation_value = int(m * D[0] + b - D[1])
    return orientation_value

def check_intersection(A, B, C, D):
    line_AB = LineString([A, B])
    line_CD = LineString([C, D])

    return line_AB.intersects(line_CD)

def check_object_cross_line(A, B, D, current_point, old_point):
    curent_orientation_value =  get_value_orientation(A, B, D) * get_value_orientation(A, B, current_point)
    old_orientation_value =  get_value_orientation(A, B, D) * get_value_orientation(A, B, old_point)
    if curent_orientation_value > 0 and old_orientation_value < 0 and check_intersection(A, B, current_point, old_point):
        return True
    else: 
        return False

# Tạo một hình ảnh trắng với kích thước 500x500
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Tọa độ của điểm A và B
A = (100, 100)
B = (400, 400)

# Tọa độ của điểm M và N
D = (350, 200)
M = (300, 250)
N = (50, 250)

# Vẽ đường thẳng AB
cv2.line(image, A, B, (0, 0, 255), 2)

# Vẽ điểm A, B, M, N
cv2.circle(image, A, 5, (0, 255, 0), -1)  # A
cv2.circle(image, B, 5, (0, 255, 0), -1)  # B
cv2.circle(image, D, 5, (255, 0, 0), -1)  # M
cv2.line(image, (int((A[0]+B[0])//2), int((A[1] + B[1])//2)), D, (0, 0, 255), 2)
cv2.circle(image, M, 5, (255, 0, 0), -1)  # M
cv2.circle(image, N, 5, (255, 0, 0), -1)  # N

# Kiểm tra sự tương phản của M và N với đường thẳng AB
result_m = get_value_orientation(A, B, M)
result_n = get_value_orientation(A, B, N)

if result_m * result_n > 0:
    print("M và N nằm cùng phía")
else:
    print("M và N nằm khác phía")

if check_intersection(A, B, M, N):
    print("Đoạn AB cắt đoạn MN.")
else:
    print("Đoạn AB không cắt đoạn MN.")

if check_object_cross_line(A, B, D, M, N):
    print("cross line")
else: 
    print("Not cross line")
# Hiển thị hình ảnh
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
