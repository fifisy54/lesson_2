import time
import turtle as t
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from collections import deque
from keras.layers import Dense
from keras.optimizers import Adam
# from rl.agents.dqn import DQNAgent
# from rl.policy import EpsGreedyQPolicy
# from rl.memory import SequentialMemory


class DqnAgent:
    def __init__(self, state, action, future_state):
        self.memory = deque(maxlen=100000)
        self.batch_size = 128
        self.state = state
        self.action = action
        self.future_state = future_state


    def get_state(self):
        ...

    def Dqn(self):
        agent = Sequential()
        agent.add(Dense(64, input_shape=(?), activation='relu'))
        agent.add(Dense(64, activation='relu'))
        agent.add(Dense(?, activation='linear'))
        agent.compile(loss='mse', optimizer=Adam(lr=0.001))
        return agent

    def remember(self, state, action, reward, future_state, done):
        self.memory.append((state, action, reward, future_state, done))


class Environment:
    def __init__(self):
        self.snake = t.Turtle()
        self.screen = t.Screen()
        self.head = t.Turtle()
        self.food = t.Turtle()
        self.score = t.Turtle()
        self.head_direction = t.Turtle()
        self.segments = []
        self.cur_score = 0
        self.highest_score = 0
        self.delay = 0.1
        self.reward = 0

    def game_screen(self):
        self.screen.title('Snake')
        self.screen.bgcolor('black')
        self.screen.setup(600, 600)
        self.screen.tracer(1)

    def head_creation(self):
        self.head.shape('square')
        self.head.color('blue')
        self.head.up()
        self.head.goto(0, 0)
        self.head_direction = "stop"

    def food_creation(self):
        self.food.shape('circle')
        self.food.color('red')
        self.food.up()
        self.food.speed(0)
        self.food.goto(0, 100)

    def scores(self):
        self.score.speed(0)
        self.score.shape('square')
        self.score.color('white')
        self.score.up()
        self.score.hideturtle()
        self.score.goto(0, 250)

        self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score), align='center',
                         font=('Arial', 20, 'bold'))

    # def control(self):
    #     def move_up():
    #         if self.head_direction != 'down':
    #             self.head_direction = 'up'
    #
    #     def move_down():
    #         if self.head_direction != 'up':
    #             self.head_direction = 'down'
    #
    #     def move_left():
    #         if self.head_direction != 'right':
    #             self.head_direction = 'left'
    #
    #     def move_right():
    #         if self.head_direction != 'left':
    #             self.head_direction = 'right'
    #
    #     self.screen.listen()
    #     self.screen.onkeypress(move_up, 'w')
    #     self.screen.onkeypress(move_down, 's')
    #     self.screen.onkeypress(move_left, 'a')
    #     self.screen.onkeypress(move_right, 'd')

    def move(self):
        if self.head_direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head_direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head_direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head_direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def play(self):
        while True:
            self.screen.update()
            if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
                self.head.goto(0, 0)
                self.head.direction = 'stop'
                for segment in self.segments:
                    segment.goto(1000, 1000)
                self.segments.clear()
                self.cur_score = 0
                self.reward -= 1
                self.score.clear()
                self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score),
                                 align='center', font=('Arial', 20, 'bold'))

            if self.head.distance(self.food) < 20:
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                self.food.goto(x, y)

                self.new_segment = t.Turtle()
                self.new_segment.speed(0)
                self.new_segment.shape("square")
                self.new_segment.color("grey")
                self.new_segment.up()
                self.segments.append(self.new_segment)
                self.delay -= 0.001
                self.cur_score += 1
                self.reward += 1

                if self.cur_score > self.highest_score:
                    self.highest_score = self.cur_score
                self.score.clear()
                self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score),
                                 align='center', font=('Arial', 20, 'bold'))

            print(self.segments)
            for index, segment in enumerate(self.segments[::-1]):
                if index == len(self.segments) - 1:
                    x = self.head.xcor()
                    y = self.head.ycor()
                    self.segments[-1].goto(x, y)
                else:
                    x = self.segments[index + 1].xcor()
                    y = self.segments[index + 1].ycor()
                    self.segments[index].goto(x, y)

            self.move()

            for segment in self.segments:
                if segment.distance(self.head) < 20:
                    self.head.goto(0, 0)
                    self.head.direction = "stop"
                    for i in self.segments:
                        i.goto(1000, 1000)
                    segment.clear()
                    self.cur_score = 0
                    self.reward -= 1
                    self.delay = 0.1
                    self.score.clear()
                    self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score),
                                     align='center', font=('Arial', 20, 'bold'))
            time.sleep(self.delay)

