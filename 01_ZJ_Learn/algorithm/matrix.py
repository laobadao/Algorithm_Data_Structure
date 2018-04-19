"""
 题目 ：
 给定一个0、1矩阵，求该矩阵内部的满足以下条件的最大的矩形的左上角所在的行和列，
 以及该矩形的长和宽。该矩形满足边上全为1，内部可以为0，可以为1，不做限定（假设所有输入有且仅有一个矩形满足条件）。

  输入描述：
 首先输入矩阵行和列 m n，接下来输入0,1矩阵 Mat[ m ][ n ]

 输出描述：
 四个数字，依次代表满足条件矩形左上角所在的行数和列数，以及该矩形的高（垂直长度）和宽（水平长度）

 样例输入：
 6 9

0 0 1 1 0 0 0 0 1
0 1 1 1 1 1 1 1 1
0 1 1 0 1 0 1 0 1
1 0 1 0 0 0 0 0 1
0 0 1 1 1 1 1 1 1
1 0 0 0 1 0 1 0 0

样例输出：
左上角 行数：2  列数 ：3 矩形的高（垂直长度）： 4 宽（水平长度） ：7

"""
from numpy import *

M = array([[0, 0, 1, 1, 0, 0, 0, 0, 1],
           [0, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 1],
           [0, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 1, 0, 1, 0, 0], ])

left_up_points = []  # 左上 list
left_down_points = []  # 左下 list
right_up_points = []  # 右上 list
right_down_points = []  # 右下 list

# 矩阵的行
m = M.shape[0]

# 矩阵的列
n = M.shape[1]

# 循环遍历寻找左上角，也就是这个点是 1 且下方和右方的点 也是 1 ,然后将这个点的坐标加到 left_up_points list 中
# 行数从上往下 0 —— m-1 列数从左往右 0 —— n-1
for i in range(m - 1):
    for j in range(n - 1):
        if M[i, j] == M[i, j + 1] == M[i + 1, j] == 1:
            left_up_points.append((i, j))

# 循环遍历寻找右上角，也就是这个点和这个点的下方以及左边一点都是 1 ，然后加到 right_up_points list 中
# 行数 从 上往下 0 —— m-1 列数 从左往右 1 — n 从第一行第二列 坐标（ 0,1 ）
#  注意： 当 矩阵满足条件是，右上角 的坐标 查询最快的话 也是 （0,1） 也就是 列数 纵坐标肯定大于1
for i in range(m - 1):
    for j in range(1, n):
        if M[i, j] == M[i, j - 1] == M[i + 1, j] == 1:
            right_up_points.append((i, j))

# 循环遍历左下角，也就是这个点的右边以及上边 一点是1 ，。。。
# 但这个点不可能是（0，n -1）( m-1 ,n -1)
for i in range(1, m):
    for j in range(n - 1):
        if M[i, j] == M[i - 1, j] == M[i, j + 1] == 1:
            left_down_points.append((i, j))

# 循环遍历右下角 ，也就是这个点以及点的上方和左边都是 1

for i in range(1, m):
    for j in range(1, n):
        if M[i, j] == M[i - 1, j] == M[i, j - 1] == 1:
            right_down_points.append((i, j))

# 找出所有可能的长方形 4 重 for 循环遍历，左上 x == 右上 x ， 右上 y==右下 y ，左 上y = 左下 y ,右下x= 左下 x
# (left_up_x,left_up_y) ( left_down_x,left_down_y) (right_up_x ,right_up_y) (right_down_x,right_down_y)
# left_up_x == right_up_x & right_up_y == right_down_y & right_down_x == left_down_x & left_up_y & left_down_y

rectangles = []
for left_up_point in left_up_points:
    for right_up_point in right_up_points:
        for left_down_point in left_down_points:
            for right_down_point in right_down_points:
                if left_up_point[0] == right_up_point[0]:
                    if right_up_point[1] == right_down_point[1]:
                        if left_up_point[1] == left_down_point[1]:
                            if right_down_point[0] == left_down_point[0]:
                                if (left_up_point != right_up_point) & (right_up_point != right_down_point) \
                                        & (right_down_point != left_down_point) & (left_down_point != left_up_point) \
                                        & (left_up_point != right_down_point) & (right_up_point != left_down_point):
                                    rectangles.append(
                                        (left_up_point, right_up_point, left_down_point, right_down_point))

# rectangles.append( (left_up_point, right_up_point, left_down_point, right_down_point))
# 存长方形 坐标时 是按（左上，右上，左下，右下）存储的，索引对应的就是  0,1,2,3

# 找出面积最大的长方形
# area 长方形的面积 和宽
area = []
# 长方形 准确的坐标参数
candidate = []
# 循环遍历算面积
for rectangle in rectangles:
    # 算面积之前 先验证 横向和纵向每个边长的， 每一步 也就是每个坐标上的值都是 1
    h1 = 0
    # 比如 (1,2 ) ---(1,8 ) 也就是 验证（1,3） （1,4）（1,5）（1,6）（1,7） （1,8） 这些坐标点的值是不是 1 ？？？？
    for each_step_h1 in range(1, rectangle[1][1] - rectangle[0][1] + 1):
        #  取 x 坐标 rectangle[0][0] ，递增 y 坐标 rectangle[0][1]
        if M[rectangle[0][0], rectangle[0][1] + each_step_h1] == 1:
            h1 += 1
    # 比如 (1,2 ) ---(4,2 ) 也就是 验证(1,2 ) (2,2 ) (3,2 ) (4,2 ) 这些坐标点的值是不是 1
    v1 = 0
    for each_step_v1 in range(1, rectangle[2][0] - rectangle[0][0] + 1):
        # 取 y 坐标固定 rectangle[0][1] ， 递增 x 坐标值 rectangle[0][0] + each_step_v1
        if M[rectangle[0][0] + each_step_v1, rectangle[0][1]] == 1:
            v1 += 1

    # 再次验证 计算面积 存数据
    if (h1 == (rectangle[1][1] - rectangle[0][1])) & (v1 == (rectangle[2][0] - rectangle[0][0])):
        candidate.append(rectangle)
        area.append(((h1 + 1) * (v1 + 1), v1, h1))

print(area)
index = area.index(max(area))
print("左上角行数 :", (candidate[index][0][0] + 1), '列数 ：', (candidate[index][0][1] + 1),
      "矩形的高（垂直长度）：", (area[index][1] + 1), " 宽（水平长度）：", (area[index][2] + 1))


# print(M)
# print(left_up_points)
# print(left_down_points)
# print(right_up_points)
# print(right_down_points)
# print(list(range(3)))  # 不包含 最后一个 小于3
# print(list(range(1, 3)))
# print(rectangles)
# print("rectangles[0][1]=", rectangles[0][1])  # 长方形列表里 [0] 索引 0 的 数据里的 右上角 坐标

# for rectangle in rectangles:
#     print(rectangle)
#     print("rectangle[0][0]", rectangle[0][0])

# ((0, 2), (0, 3), (1, 2), (1, 3))
# rectangle[0][0]  0  也就是 （0,2）中的 x 坐标
