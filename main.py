from random import choices

##draw_figures, draw_point_s, draw_point_с, draw_point_с
##draw_stables, main, points, circle, square, rand_square

h = 30
l = 120

def zero():
    return [[],[],[]]

figures = zero()
stables = zero()
points_range = []
points_stble = []

#                 1111111111
#       01234567890123456789
cols = "@$%&=>: O#*,"
result = [" "] * l * h


def draw_figures(inn):
    for j in figures[0]:
        for i in range(l * h - 1):
            x = i % l
            y = i // l

            if int((x - j[0])**2*0.219) + (y - j[1])**2 <= (j[2])**2:
                inn[i] = cols[j[3]]

    for j in figures[1]:
        for i in range(l * h - 1):
            x = i % l
            y = i // l

            if abs(x-j[0]) < j[2]//2 and abs(y-j[1]) < j[3]//2:
                inn[i] = cols[j[4]]

    for j in figures[2]:
        for i in range(l * h - 1):
            x = i % l
            y = i // l

            if abs(x-j[0]) < j[2]//2 and abs(y-j[1]) < j[3]//2:
                inn[i] = choices(cols, j[4])[0]

    return inn

def draw_point_s(inn):
    for j in points_stble:
        try:
            inn[j[1] * 120 + j[0]] = cols[j[2]]
        except Exception:
            a = 0

    return inn

def draw_point_с(inn):
    for j in points_range:
        try:
            inn[j[1] * 120 + j[0]] = cols[j[2]]
        except Exception:
            a = 0

    return inn
            
def draw_stables(inn):
    for j in stables[0]:
        for i in range(l * h - 1):
            x = i % l
            y = i // l

            if int((x - j[0])**2*0.219) + (y - j[1])**2 <= (j[2])**2:
                inn[i] = cols[j[3]]

    for j in stables[1]:
        for i in range(l * h - 1):
            x = i % l
            y = i // l

            if abs(x-j[0]) < j[2]//2 and abs(y-j[1]) < j[3]//2*0.38:
                inn[i] = cols[j[4]]

    for j in stables[2]:
        for i in range(l * h - 1):
            x = i % l
            y = i // l

            if abs(x-j[0]) < j[2]//2 and abs(y-j[1]) < j[3]//2:
                inn[i] = choices(cols, j[4])[0]

    return inn



def main():    
    result = [" "] * l * h

    try:
        result = draw_stables(result)
    except Exception:
        a = 0
            
    try:
        result = draw_point_s(result)
    except Exception:
        a = 0
       
    try:
        result = draw_figures(result)
    except Exception:
        a = 0
       
    try:
        result = draw_point_с(result)
    except Exception:
        a = 0
       
    
    final = ""
    for i in result:
        final += i

##    print(final)
        
    global points_range
    points_range = []
    global figures
    figures = zero()
    
    return final

    

    
def points(x, y, col, stable = False):
    if stable == False:
        points_range.append([x, y, col])
    else:
        points_stble.append([x, y, col])

def circle(x, y, r, col, stable = False):
    if stable == False:
        figures[0].append([x, y, r, col])
    else:
        stables[0].append([x, y, r, col])

def square(x, y, wid, hei, col, stable = False):
    if stable == False:
        figures[1].append([x, y, wid, hei, col])
    else:
        stables[1].append([x, y, wid, hei, col])

def rand_square(x, y, wid, hei, cols = [10,9,8,5,2,1,1,1], stable = False):
    if stable == False:
        figures[2].append([x, y, wid, hei, cols])
    else:
        stables[2].append([x, y, wid, hei, cols])
