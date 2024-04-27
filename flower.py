import turtle as tr

s = tr.Screen()

tr.setup(800, 800)
s.bgcolor('#262626')
tr.pencolor('#540d6e')
tr.speed(0)
tr.tracer(100)
tr.pensize(1)
col = ('#DDA0DD', '#DA70D6', '#BA55D3', '#9932CC')

for i in range(3):
  for n in range(400):
    tr.color(col[n%4])
    tr.circle(190-n/2, 90)
    tr.left(90)
    tr.circle(190-n/2, 90)
    tr.color(col[n%4])
  tr.left(30)
s.exitonclick()  