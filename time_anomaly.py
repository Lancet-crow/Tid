import pygame
import random


class Point:
    def __init__(self, x, y, screen):
        self.pos_x = x
        self.pos_y = y
        self.screen = screen
        self.connected_lines = 0
        self.radius = 15
        self.color = 'white'

    def update(self):
        pygame.draw.circle(self.screen, pygame.Color(self.color), (self.pos_x, self.pos_y), self.radius)

    def change_color(self, intersection=False, moving=False):
        if moving:
            self.color = 'yellow'
        elif intersection:
            self.color = 'red'
        else:
            self.color = 'white'


class Line:
    def __init__(self, point_1, point_2, screen):
        self.point_1 = point_1
        self.point_2 = point_2
        self.screen = screen
        self.color = 'white'

    def update(self):
        pygame.draw.aaline(self.screen, pygame.Color(self.color),
                           (self.point_1.pos_x, self.point_1.pos_y), (self.point_2.pos_x, self.point_2.pos_y), 15)

    def change_color(self, intersection=False):
        if intersection:
            self.color = 'red'
        else:
            self.color = 'white'


def web_generation(c_points, screen, points, lines):
    width, height = screen.get_size()
    for i in range(c_points):
        x = random.sample(range(100, width - 100), 1)
        y = random.sample(range(100, height - 100), 1)
        while (x, y) in [(j.pos_x, j.pos_y) for j in points]:
            x = random.sample(range(100, width - 100), 1)
            y = random.sample(range(100, height - 100), 1)
        a = Point(x[0], y[0], screen=screen)
        a.update()
        points.append(a)
    for i in range(c_points):
        p_1 = points[i]
        if p_1 == points[-1]:
            p_2 = points[0]
        else:
            p_2 = points[i + 1]
        a = Line(p_1, p_2, screen)
        a.update()
        lines.append(a)
        p_1.connected_lines += 1
        p_2.connected_lines += 1


def line_intersection(p1, p2, p3, p4):
    p1 = (p1.pos_x, p1.pos_y)
    p2 = (p2.pos_x, p2.pos_y)
    p3 = (p3.pos_x, p3.pos_y)
    p4 = (p4.pos_x, p4.pos_y)

    xdiff = (p1[0] - p2[0], p3[0] - p4[0])
    ydiff = (p1[1] - p2[1], p3[1] - p4[1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    print(div)
    return div != 0
    # vertical_line_1 = False
    # vertical_line_2 = False
    #
    # if p1[0] != p2[0]:
    #     a1 = int((p1[1] - p2[1]) / (p1[0] - p2[0]))
    # else:
    #     vertical_line_1 = True
    #     a1 = 0
    # if p3[0] != p4[0]:
    #     a2 = int((p3[1] - p4[1]) / (p3[0] - p4[0]))
    # else:
    #     vertical_line_2 = True
    #     a2 = 0
    # if a1 != a2 and not vertical_line_1 and not vertical_line_2:
    #     b1 = p1[1] - (a1 * p1[0])
    #     b2 = p3[1] - (a2 * p3[0])
    #     x_int = int((b2 - b1) / (a1 - a2))
    #     y_int = a1 * x_int + b1
    #     a = list(range(p1[0], p2[0] - 5)) if p1[0] < p2[0] else list(range(p2[0], p1[0] - 5))
    #     b = list(range(p3[0], p4[0] - 5)) if p3[0] < p4[0] else list(range(p4[0], p3[0] - 5))
    #     c = list(range(p1[1], p2[1] - 5)) if p1[1] < p2[1] else list(range(p2[1], p1[1] - 5))
    #     d = list(range(p3[1], p4[1] - 5)) if p3[1] < p4[1] else list(range(p4[1], p3[1] - 5))
        # линии отладки
        # if 0 <= b1 <= height:
        #     y1 = b1
        #     y2 = a1 * width + b1
        #     pygame.draw.line(screen, pygame.Color('green'), (0, y1), (width, y2), 1)
        # else:
        #     if a1 != 0:
        #         x1 = int((0 - b1) / a1)
        #         x2 = int((height - b1) / a1)
        #         pygame.draw.line(screen, pygame.Color('green'), (x1, 0), (x2, height), 1)
        #     else:
        #         pygame.draw.line(screen, pygame.Color('green'), (0, b1), (width, b1), 1)
        # # линии отладки
    #     if x_int in a and x_int in b and y_int in c and y_int in d:
    #         answer = True
    # elif vertical_line_1 != vertical_line_2:
    #     pass
    # else:
    #     answer = False
    #
    # return answer


def update_lines(lines, points):
    for i in points:
        i.update()
    for i in range(len(lines) - 1, -1, -1):
        a = False
        n = 0
        for j in range(len(lines) - 1, -1, -1):
            b = False
            if i == len(lines) - 1:
                if lines[j] != lines[i - 1] and lines[j] != lines[i] and lines[j] != lines[0]:
                    b = line_intersection(lines[i].point_1, lines[i].point_2,
                                          lines[j].point_1, lines[j].point_2)
            else:
                if lines[j] != lines[i - 1] and lines[j] != lines[i] and lines[j] != lines[i + 1]:
                    b = line_intersection(lines[i].point_1, lines[i].point_2,
                                          lines[j].point_1, lines[j].point_2)
            if b:
                n += 1
        if n > 0:
            a = True
        lines[i].change_color(a)
        lines[i].update()


def main():
    lines = []
    points = []

    pygame.init()

    width = 800
    height = 800
    screen = pygame.display.set_mode((width, height))
    screen.fill(pygame.Color('black'))

    web_generation(6, screen, points, lines)  # creating threads; int param is count of points

    moving = False
    moving_object = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # передвигание точек(старт кода)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in points:
                        if (i.pos_x - i.radius < event.pos[0] < i.pos_x + i.radius
                                and i.pos_y - i.radius < event.pos[1] < i.pos_y + i.radius):
                            moving_object = i
                            moving = True
            if event.type == pygame.MOUSEMOTION:
                if moving:
                    x_move, y_move = event.rel
                    moving_object.pos_x += x_move
                    moving_object.pos_y += y_move
                    moving_object.change_color(moving=True)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if moving:
                        moving_object.change_color(moving=False)
                    moving = False
                    moving_object = None
            # передвигание точек(конец кода)
        screen.fill(pygame.Color('black'))
        update_lines(lines, points)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
