import time
import turtle as t
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

    def borders(self):
        self.border.hideturtle()
        self.border.up()
        self.border.goto(-300, 300)
        self.border.down()
        self.border.goto(300, 300)
        self.border.goto(300, -300)
        self.border.goto(-300, -300)
        self.border.goto(-300, 300)

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
        self.cur_score += 10
        if self.cur_score > self.highest_score:
            self.highest_score = self.cur_score
        self.score.clear()

    def food_creation(self):
        self.food.shape('circle')
        self.food.color('red')
        self.food.up()
        self.food.speed(0)
        self.food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

    def scores(self):
        self.score.speed(0)
        self.score.shape('square')
        self.score.color('white')
        self.score.up()
        self.score.hideturtle()
        self.score.goto(0, 250)

        self.score.write('Score : {}    Highest Score : {}'.format(self.cur_score, self.highest_score), align='center',
                         font=('Arial', 20, 'bold'))
        t.mainloop()

    def move(self):
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
        self.screen.onkeypress(move_up, "w")
        self.screen.onkeypress(move_down, "s")
        self.screen.onkeypress(move_left, "a")
        self.screen.onkeypress(move_right, "d")

    def play(self):
        while True:
            self.screen.update()
            if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
                self.head.goto(0, 0)
                self.head.direction = "stop"


snake = Snake()
snake.game_screen()
snake.borders()
snake.head_creation()
snake.food_creation()
snake.scores()
snake.move()


"""
управление
движение
удлиннение змейки
тело и голова разного цвета
когда съедает еду, +балл к скору
Проверка на столкновение со стенкой и попытки самоедства
автоматический перезапуск после
"""