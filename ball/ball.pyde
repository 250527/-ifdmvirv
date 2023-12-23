def  setup():
    size(600,600)
    background(0)
    
def draw():
    strokeWeight(3)
    stroke(random(0,255),random(0,255),random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    rect(random(0,600),random(0,600),20,20)
    ellipse(random(0,600),random(0,600),20,20)
    
