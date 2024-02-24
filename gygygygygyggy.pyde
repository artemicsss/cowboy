z=1000
def setup():
    size(600,600)
def draw():
    global z
    translate(300,300)
    strokeWeight(random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(0,0,z,z)
    z=z-2
