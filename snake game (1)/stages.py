from util import vector

snake = [vector(20, 20)]
walls = {vector(100, 0), vector(-100, 0)}
pwalls = {vector(150, 0) : 5}
thorns = {vector(10, 10)}
lasers = [[vector(-100, 0), vector(100, 0)]]
teledict = {vector(0, 100) : vector(0, -100)}
foods = {vector(0, 0), vector(50, 50)}
stage = []

stage.append([snake, walls, pwalls, thorns, lasers, teledict, foods])

snake = [vector(100, 100)]
walls = {vector(100, 0), vector(-100, 0)}
pwalls = {vector(150, 0) : 5}
thorns = {vector(10, 10)}
lasers = [[vector(-100, 0), vector(100, 0)]]
teledict = {vector(0, 100) : vector(0, -100)}
foods = {vector(0, 0), vector(50, 50)}

stage.append([snake, walls, pwalls, thorns, lasers, teledict, foods])