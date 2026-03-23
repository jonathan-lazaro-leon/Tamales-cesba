import turtle, colorsys


#Este archivo solo sirve para entretenimiento
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
turtle.colormode(1.0)

# --- Parametros ---
numero_estrella = 75
giro = 145
paso = 3
h = 0.0
i = 0 #contador del paso actual

def steps_for(i):
    if i < 40:      return 1 # centro : 1 paso por frame
    elif i < 120:   return 2
    elif i < 240:   return 3
    else:           return 5 # Lejos del centro: acelera

def frame():
    global i, h
    spf = steps_for(i)

    for _ in range(spf):
        #color arcoiris neon
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        t.pencolor(r,g,b)

        # Grosor sueave creciente
        t.pensize(1 + (i // 60))

        #avance (si i ==0, no se ve; frozamos el avance minimo)
        step_len = max(1, i*paso)
        t.forward(step_len)
        t.right(giro)

        # siguente color y paso
        h = (h+ 0.06) % 1.0
        i += 1

        # Al completar el ciclo, reinicia ( para animacion infinita)
        if i > numero_estrella * 5 :
            i = 0
            t.clear()
            t.penup(); t.home(); t.setheading(0); t.pendown()

    screen.update()
    screen.ontimer(frame, 16) # 60 FPS

frame()
screen.exitonclick()