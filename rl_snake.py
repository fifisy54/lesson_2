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

# агент -- змейка(класс); среда -- экран; состо€ни€ -- ?; действи€ -- движение; награда -- +1(€блоко)/-1(смерть)


class Snake:
    def __init__(self):
        self.snake = t.Turtle()
        self.screen = t.Screen()
        self.border = t.Turtle()
        self.head = t.Turtle()
        self.food = t.Turtle()
        self.score = t.Turtle()
        self.head_direction = t.Turtle()
        self.segments = []
        self.cur_score = 0
        self.highest_score = 0
        self.delay = 0.1

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

    def control(self):
        def move_up():
            if self.head_direction != 'down':
                self.head_direction = 'up'

        def move_down():
            if self.head_direction != 'up':
                self.head_direction = 'down'

        def move_left():
            if self.head_direction != 'right':
                self.head_direction = 'left'

        def move_right():
            if self.head_direction != 'left':
                self.head_direction = 'right'

        self.screen.listen()
        self.screen.onkeypress(move_up, 'w')
        self.screen.onkeypress(move_down, 's')
        self.screen.onkeypress(move_left, 'a')
        self.screen.onkeypress(move_right, 'd')

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

            # if len(self.segments) > 0:
            #     x = self.head.xcor()
            #     y = self.head.ycor()
            #     self.segments[0].goto(x, y)
            self.move()

            for segment in self.segments:
                if segment.distance(self.head) < 20:
                    self.head.goto(0, 0)
                    self.head.direction = "stop"
                    for i in self.segments:
                        i.goto(1000, 1000)
                    segment.clear()
                    self.cur_score = 0
                    self.delay = 0.1
                    self.score.clear()
                    self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score),
                                     align='center', font=('Arial', 20, 'bold'))
            time.sleep(self.delay)


snake = Snake()
snake.game_screen()
snake.head_creation()
snake.food_creation()
snake.scores()
snake.control()
snake.move()
snake.play()


class Model:

    def __init__(self, env):
        self.model = Sequential()
        self.batch_size = 500
        self.action_space = env.action_space
        self.state_space = env.state_space
        self.layer_sizes = [128, 128, 128]
        self.learning_rate = 0.00025
        self.memory = deque(maxlen=2500)
        self.model = self.fit()
        # states =
        # actions =
        # rewards =
        # next_states =

    def preprocess(self):
        ...

    def fit(self):
        for i in range(len(self.layer_sizes)):
            if i == 0:
                self.model.add(Dense(self.layer_sizes[i], input_shape=(self.state_space,), activation='relu'))
            else:
                self.model.add(Dense(self.layer_sizes[i], activation='relu'))
        self.model.add(Dense(self.action_space, activation='softmax'))
        self.model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return self.model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def chart(self):
        # history = self.model.fit(..., epochs=1, verbose=0)
        ...
