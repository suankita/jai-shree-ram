from turtle import*
title('jai shreeram')
bgcolor('black')
pensize(5)
pencolor("orange")
Ram_name = ["जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम",]
angle = 360/49
penup()
sety(-1)
for i in range(50):
    left(angle)
    forward(260)
    write(Ram_name[i], align="right",
    font=('Arial',12,"bold"))
    backward(260)
penup()
goto(-40,-20)
pendown()
write("|| राम ||", font=("Arial", 60,
"normal"), aIgn="center")
hideturtle()
done()