from random import randrange
from curtsies.fmtfuncs import blue, cyan, gray, green, magenta, red, yellow, plain
from time import sleep

ALPHA = 1
ALPHA = 10
BETA = 1
#BETA = 5
ITERATIONS = 32
ITERATIONS = 256
INTERVAL = 1
INTERVAL = 0.05

colours = green, magenta, gray, red, cyan, yellow, plain, blue

def printfunc(x): print x

def proportional_random(counts):
    
    r = randrange(sum(counts))

    def greater(n, i, sofar, l):
        if sofar + l[0] > n:
            return i
        return greater(n, i+1, sofar + l[0], l[1:])
    return greater(r, 0, 0, counts)

def polya_draw_from(urn):
    i = proportional_random(urn)
    return i, urn[:i] + [urn[i]+BETA] + urn[i+1:]

def dirichlet_draw_from(urn):
    i = proportional_random(urn)
    if i == 0:
        return i, urn + [BETA]
    return i, urn[:i] + [urn[i]+BETA] + urn[i+1:]
                       
def print_urn(urn):
    for i in range(len(urn)):
        print colours[i%len(colours)]('-' * urn[i] + ' (' + str(urn[i]) + ') ')

def print_urn_by_rank(urn):
    print_urn(reversed(sorted(urn)))
    
urn = [1,5,8]
draw = polya_draw_from

urn = [ALPHA]
draw = dirichlet_draw_from

print_urn(urn)

for iteration in range(ITERATIONS):
    i, urn = draw(urn)
    print '\n', iteration, ':', i
    print_urn(urn)
    sleep(INTERVAL)

if draw == dirichlet_draw_from:
    print '\n'
    print 'By rank:'
    print_urn_by_rank(urn)
