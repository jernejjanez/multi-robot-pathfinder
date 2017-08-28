from graphics import *

def draw(my_map, paths):
    colors = ["gray", "cyan", "yellow", "pink", "orange", 
              "red", "salmon", "lightgreen", "green", "violet",
              "teal", "silver", "lime", "maroon", "blue"]
    robots = dict()
    animations = dict()
    animations_text = dict()
    goals = dict()
    text = dict()
    max_ = 0
    for i in range(len(paths)):
        robots[i] = {}
        animations[i] = {}
        animations_text[i] = {}
        goals[i] = {}
        text[i] = {}
        if len(paths[i]) > max_:
            max_ = len(paths[i])

    arr_y = len(my_map)
    arr_x = len(my_map[0])

    size        = arr_y*5
    goal_size   = arr_y*10
    size_square = arr_y*2
    size_circle = arr_y*3
    text_size   = arr_y*2
    width = height = 100
    win = GraphWin('Floor', arr_x*height, arr_y*width)

    win.setCoords(0.0, arr_y, arr_x, 0.0)
    win.setBackground("white")

    # draw grid
    for x in range(arr_y):
        for y in range(arr_x):
            if my_map[x][y] == -1:
                square = Rectangle(Point(x+float(arr_y)/size,y+float(arr_y)/size), 
                                   Point(x+1-float(arr_x)/size,y+1-float(arr_x)/size))
                square.draw(win)
                square.setFill("black")

            win.plotPixel(x*height, y*width, "black")

    for i in range(max_):
        done = len(paths)
        for j in range(len(paths)):
            try:
                if i == 0:
                    goals[j][i] = Circle(Point(paths[j][max_-1][1]+float(arr_y)/size,
                                               paths[j][max_-1][0]+float(arr_y)/size), float(arr_y)/goal_size)
                    goals[j][i].draw(win)
                    goals[j][i].setFill(colors[j])

                robots[j][i] = Circle(Point(paths[j][i][1]+float(arr_y)/size_square,
                                            paths[j][i][0]+float(arr_y)/size_square), float(arr_y)/size_circle)
                robots[j][i].draw(win)

                if i == len(paths[j])-1 or paths[j][i] == paths[j][len(paths[j])-1] and paths[j][i:].count(paths[j][i]) == len(paths[j][i:]):
                    text[j][i] = Text(Point(paths[j][i][0]+float(arr_y)/text_size,
                                            paths[j][i][1]+float(arr_y)/text_size), "R"+str(j+1)+"\nGoal")
                    robots[j][i].setFill(colors[j])
                    done -= 1
                else:
                    text[j][i] = Text(Point(paths[j][i][0]+float(arr_y)/text_size,
                                            paths[j][i][1]+float(arr_y)/text_size), "R"+str(j+1))
                    robots[j][i].setFill(colors[j])
                
                text[j][i].draw(win)
                
            except IndexError:
                continue
            except KeyError:
                continue

        
        if i == 0:
            win.getMouse()

        # fluent movement
        if i != max_-1:
            num_of_anim = 200 / done
            for k in range(1,num_of_anim):
                for l in range(len(paths)):
                    if i == len(paths[j])-1 or paths[l][i] == paths[l][len(paths[l])-1] and paths[l][i:].count(paths[l][i]) == len(paths[l][i:]):
                        continue

                    if k == 1:
                        robots[l][i].undraw()
                        text[l][i].undraw()
                    
                    pty = paths[l][i][1]+float(arr_y)/size_square
                    offset_y = (paths[l][i+1][1]+float(arr_y)/size_square) - (paths[l][i][1]+float(arr_y)/size_square)
                    ptx = paths[l][i][0]+float(arr_y)/size_square
                    offset_x = (paths[l][i+1][0]+float(arr_y)/size_square) - (paths[l][i][0]+float(arr_y)/size_square)
                    
                    animations[l][k] = Circle(Point(pty+float(k)/num_of_anim*offset_y, 
                                                    ptx+float(k)/num_of_anim*offset_x), float(arr_y)/size_circle)
                    animations[l][k].setFill(colors[l])
                    animations_text[l][k] = Text(Point(paths[l][i][0]+float(arr_y)/text_size+float(k)/num_of_anim*offset_x,
                                                       paths[l][i][1]+float(arr_x)/text_size+float(k)/num_of_anim*offset_y), "R"+str(l+1))
                    
                    animations[l][k].draw(win)
                    animations_text[l][k].draw(win)

                    if k != 1:
                        animations[l][k-1].undraw()
                        animations_text[l][k-1].undraw()
                    
                    if k == num_of_anim-1:
                        animations[l][k].undraw()
                        animations_text[l][k].undraw()
    
    win.getMouse()
    win.close()