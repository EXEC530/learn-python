from random import choice


class RandomWalk:
    """一个用来进行随机漫步的类"""

    def __init__(self, num_points=5000):
        """初始化设置"""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """每次漫步的步长和方向"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """记录所有的点"""
        while len(self.x_values) < self.num_points:
            # 不断漫步直到到达指定长度
            x_step = self.get_step()
            y_step = self.get_step()
            # 决定前进的方向和距离
            if x_step and y_step == 0:
                continue
            # 随机漫步拒绝原地踏步
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            # 计算点
            self.x_values.append(next_x)
            self.y_values.append(next_y)

