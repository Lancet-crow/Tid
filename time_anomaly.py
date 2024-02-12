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


def lineLineIntersect(p1, p2, p3, p4):
    p1 = (p1.pos_x, p1.pos_y)
    p2 = (p2.pos_x, p2.pos_y)
    p3 = (p3.pos_x, p3.pos_y)
    p4 = (p4.pos_x, p4.pos_y)
    d = (p2[0] - p1[0]) * (p4[1] - p3[1]) + (p2[1] - p1[1]) * (p3[0] - p4[0])
    if d == 0:
        return False
    t = ((p3[0] - p1[0]) * (p4[1] - p3[1]) + (p3[1] - p1[1]) * (p3[0] - p4[0])) / d
    u = ((p3[0] - p1[0]) * (p2[1] - p1[1]) + (p3[1] - p1[1]) * (p1[0] - p2[0])) / d
    return 0 <= t <= 1 and 0 <= u <= 1


def update_lines(lines, points):
    any_lines_intersect = False
    for i in points:
        i.update()
    for i in range(len(lines) - 1, -1, -1):
        a = False
        n = 0
        for j in range(len(lines) - 1, -1, -1):
            b = False
            if i == len(lines) - 1:
                if lines[j] != lines[i - 1] and lines[j] != lines[i] and lines[j] != lines[0]:
                    b = lineLineIntersect(lines[i].point_1, lines[i].point_2,
                                          lines[j].point_1, lines[j].point_2)
            else:
                if lines[j] != lines[i - 1] and lines[j] != lines[i] and lines[j] != lines[i + 1]:
                    b = lineLineIntersect(lines[i].point_1, lines[i].point_2,
                                          lines[j].point_1, lines[j].point_2)
            if b:
                n += 1
        if n > 0:
            a = True
            any_lines_intersect = True
        lines[i].change_color(a)
        lines[i].update()
    return not any_lines_intersect
