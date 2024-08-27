from turtle import Turtle
FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.scoreboard_update()


    def scoreboard_update(self):
        self.clear()
        self.goto(-230, 250)
        self.current_level += 1
        self.write(f"level:{self.current_level}", font=FONT, align="center")

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER.", font=("courier", 40, "bold"), align="center")
