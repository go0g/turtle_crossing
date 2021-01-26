from turtle import Turtle
import random

CAR_COLORS = ['green', 'yellow', 'blue', 'purple']
START_POSITION = 300
END_POSITION = -320


class TrafficControl():
    def __init__(self):
        self.cars = []
        self.tick_counter = 0
        self.add_cars()

    def add_cars(self):
        for _ in range(random.randint(0, 5)):
            self.cars.append(Car())

    def remove_cars(self):
        self.cars = list(filter(lambda car: car.xcor() > -350, self.cars))
        print(len(self.cars))

    def move(self):
        self.tick_counter += 1
        if self.tick_counter > 10 and random.choice([True, False]):
            self.tick_counter = 0
            self.add_cars()
        for car in self.cars:
            car.forward(car.speed)
        self.remove_cars()


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(CAR_COLORS))
        self.shape('square')
        self.speed = random.randint(8, 10)
        self.penup()
        self.shapesize(1, 2, 0)
        self.setheading(180)
        self.goto(y=random.randrange(-240, 280, 20), x=START_POSITION)
