def path(my_map, start, moves, print_=1):
    steps = 0
    if moves == None:
        print 'Can\'t find optimal paths'
    else:        
        paths = dict()
        for i in range(len(moves[0][0])):
            paths[i] = [start[i]]

        for move in moves:
            for j in range(len(move[0])):
                temp_location = [a_i + b_i for a_i, b_i in zip(start[move[0][j][0]-1], move[0][j][1])]
                paths[move[0][j][0]-1].append(temp_location)
                start[move[0][j][0]-1] = temp_location

        for i in range(len(paths)):
            for j in range(len(paths[i])):
                if j == len(paths[i])-1 or paths[i][j] == paths[i][len(paths[i])-1] and paths[i][j:].count(paths[i][j]) == len(paths[i][j:]):
                    if print_ == 1:
                        print 'Path for robot', i+1, '->', paths[i][0:j+1]
                    if j > steps:
                        steps = j
                    break
        return paths, steps