import CoDrone
from tkinter import Tk, Canvas, BOTH
from math import sin, cos, radians
from random import choice, randint

class BrickBreaker(Tk):

    lives = 3
    bricks = []

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.resizable(0, 0)
        self.canvas = Canvas(self, bg='black', width=400, height=400)
        self.canvas.pack(expand=1, fill=BOTH)
        self.makeBall()
        self.makePaddle()
        self.makeBricks()

    def makeBall(self):
        self.canvas.create_oval(60, 100, 70, 110, fill='lawn green', outline='white', tags='ball')
        #self.after(1000, self._move_ball)

    def updateCoords(self, brickCoords):
        brickCoords[0] += 30
        brickCoords[2] += 30
        if brickCoords[2] > 395:
            brickCoords[0] = 5
            brickCoords[2] = 35
            brickCoords[1] += 10
            brickCoords[3] += 10
        return brickCoords

    def makeBricks(self):
        brickCoords = [5, 5, 35, 15]
        for i in range(39):
            self.canvas.create_rectangle(*brickCoords, outline='white', fill=('#{}'.format(randint(100000, 999999))),tags='brick' + str(i))
            self.bricks[i] = None
            brickCoords = self.updateCoords(brickCoords)

    def makePaddle(self):
        self.canvas.create_rectangle(175, 375, 225, 385, fill='black', outline='white', tags='paddle')
        self.bind('<Key>', self.updatePaddle()) #Possibly Dont?

    def updateBall(self, incX, incY):
        self.canvas.move('ball', incX, incY)

    def deleteBrick(self, brick):
        self.canvas.delete(brick)
        del self.bricks[brick]

    def updatePaddle(self, roll):
        self.canvas.move('paddle', roll, 0) #Adjust roll to be reasonable

    def gameLoop(self):
        ball = self.canvas.find_withtag('ball')[0]
        bounds = self.canvas.find_overlapping(0, 0, 400, 400)
        paddle = self.canvas.find_overlapping(*self.canvas.coords('paddle'))
        for brick in self.bricks.iterkeys():
            self.bricks[brick] = self.canvas.find_overlapping(*self.canvas.bbox(brick))

        # calculate change in x,y values of ball
        angle = self.angle - 90  # correct for quadrant IV
        increment_x = cos(radians(angle)) * self.speed
        increment_y = sin(radians(angle)) * self.speed

        # finite state machine to set ball state
        if ball in bounds:
            self.ball_state = 'moving'
            for brick, hit in self.bricks.iteritems():
                if ball in hit:
                    self.ball_state = 'hit_brick'
                    delete_brick = brick
                elif ball in paddle:
                    self.ball_state = 'hit_wall'
        elif ball not in bounds:
            if self.canvas.coords('ball')[1] < 400:
                self.ball_state = 'hit_wall'
            else:
                self.ball_state = 'out_of_bounds'
                self._initiate_new_ball()

        # handler for ball state
        if self.ball_state is 'moving':
            self.canvas.move('ball', increment_x, increment_y)
            self.after(15, self._move_ball)
        elif self.ball_state is 'hit_brick' or self.ball_state is 'hit_wall':
            if self.ball_state == 'hit_brick':
                self.deleteBrick(self, delete_brick)
            self.canvas.move('ball', -increment_x, -increment_y)
            self.angle += choice([119, 120, 121])
            self._move_ball()