import heapq

def execute_sequence(pos, sequence):
    for move, cost in sequence:
        pos.move(move)

def undo_sequence(pos, sequence):
    for move, cost in reversed(sequence):
        pos.undo_move(move)

def A(pos, limit = 1000000):
    # A* best-first heuristic search
    # cand_paths: a priority queue of candidate paths;
    # visited: dictionary of already generated nodes and best g-values (and f-values) seen to reach them (thus no duplicates!)
    cand_paths = [(pos.evaluate(), [], pos.ID())]
    visited = { pos.ID(): (0, pos.evaluate()) }
    ix = 1
    while cand_paths:
        if ix > limit: 
            print "Limit Reached!"
            return None     # limit on expanded nodes reached
        if ix % 100000 == 0:
            print ix
        ix += 1

        val, path, id = heapq.heappop(cand_paths)

        execute_sequence(pos, path)

        if pos.solved():
            undo_sequence(pos, path)
            return path

        if visited[id][1] < val:
            undo_sequence(pos, path)
            continue
            
        # generate candidates
        for move, cost in pos.generate_moves():
            pos.move(move)
            new_id = pos.ID()
            if new_id not in visited or visited[new_id][0] > visited[id][0] + cost:
                # if a better path to state is found, add it to candidates
                visited[new_id] = (visited[id][0] + cost, visited[id][0] + cost + pos.evaluate())
                pos.num_expanded += 1
                heapq.heappush(cand_paths, (visited[new_id][1], path + [(move, cost)], new_id))
            pos.undo_move(move)
        undo_sequence(pos, path)

    print "No more candidates."
    return None     # no more candidate paths and solution was not found