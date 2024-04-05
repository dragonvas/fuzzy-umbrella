uwu=0
owo=0
def setup():
    size(1000,1000)
    colorMode(HSB)
def draw():
    background(0)
    for uwu in range(500, 860, 20):
        for owo in range(20,360,20):
            fill(owo,100,100)
            ellipse(uwu,owo,owo,owo)
