import time
import turtle as t
import random
from random import randrange


class Snake:
    def __init__(self):
        self.snake = t.Turtle()
        self.screen = t.Screen()
        self.border = t.Turtle()
        self.head = t.Turtle()
        self.food = t.Turtle()
        self.score = t.Turtle()
        self.head_direction = t.Turtle()
        self.body_direction = t.Turtle()
        self.new_segment = t.Turtle()
        self.segments = []
        self.cur_score = 0
        self.highest_score = 0
        self.delay = 0.1

    def game_screen(self):
        self.screen.title('Snake')
        self.screen.bgcolor('black')
        self.screen.setup(600, 600)
        self.screen.tracer(1)

    # def borders(self):
    #     self.border.hideturtle()
    #     self.border.up()
    #     self.border.goto(-300, 300)
    #     self.border.down()
    #     self.border.goto(300, 300)
    #     self.border.goto(300, -300)
    #     self.border.goto(-300, -300)
    #     self.border.goto(-300, 300)

    def head_creation(self):
        self.head.shape('square')
        self.head.color('green')
        self.head.up()
        self.head.goto(0, 0)
        self.head_direction = "stop"

    def body_creation(self):
        self.new_segment.speed(0)
        self.new_segment.shape("square")
        self.new_segment.color("orange")
        self.new_segment.up()
        self.segments.append(self.new_segment)
        self.delay -= 0.001

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

    def something(self):
        for index, segment in enumerate(self.segments):
            if index == 0:


    def play(self):
        while True:
            self.screen.update()
            self.move()
            if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
                time.sleep(1)
                self.head.goto(0, 0)
                self.head.direction = 'stop'
                for i in self.segments:
                    i.goto(1000, 1000)
                self.segments.clear()
                self.cur_score = 0
                self.delay = 0.1
                self.score.clear()
                self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score),
                                 align='center', font=('Arial', 20, 'bold'))
            if self.head.distance(self.food) < 20:
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                self.food.goto(x, y)

                self.body_creation()
                self.cur_score += 1

                if self.cur_score > self.highest_score:
                    self.highest_score = self.cur_score
                self.score.clear()
                self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score),
                                 align='center', font=('Arial', 20, 'bold'))

                for index in range(len(self.segments) - 1, 0, -1):
                    x = self.segments[index - 1].xcor()
                    y = self.segments[index - 1].ycor()
                    self.segments[index].goto(x, y)

                if len(self.segments) > 0:
                    x = self.head.xcor()
                    y = self.head.ycor()
                    self.segments[0].goto(x, y)
                    self.move()
                for segment in self.segments:
                    if segment.distance(self.head) < 20:
                        # time.sleep(1)
                        self.head.goto(0, 0)
                        self.head.direction = "stop"
                        for j in self.segments:
                            j.goto(1000, 1000)
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


"""
управление
движение
удлиннение змейки
тело и голова разного цвета
когда съедает еду, +балл к скору
Проверка на столкновение со стенкой и попытки самоедства
автоматический перезапуск после
"""