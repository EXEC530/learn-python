from random_walk import RandomWalk
import time
"""引入time用来计时"""
# 多次进行随机漫步
start_time = time.time()
while True:
    rw = RandomWalk(1000000)
    rw.fill_walk()
    # 对点进行渐变绘色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=0.5)
    # 对起点和终点进行突出
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break
end_time = time.time()
"""大概用了17秒"""
print('time cost', end_time - start_time, 's')
