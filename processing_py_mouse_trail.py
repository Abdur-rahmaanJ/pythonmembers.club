class MouseTrail:
    def __init__(self):
        self.history = []
        
    def update(self):
        self.history.append([mouseX, mouseY])
        if len(self.history)  > 200:
            self.history.pop(0)
            
    def display_mouse(self):
        fill(100, 100, 100, 100)
        ellipse(mouseX, mouseY, 50, 50)
        
    def display_trail(self):
        beginShape()
        stroke(0)
        strokeWeight(1)
        noFill()
        for v in self.history:
            vertex(v[0], v[1])
        endShape()
        
    def run(self):
        self.update()
        self.display_mouse()
        self.display_trail()

trail = None

def setup():
    global trail
    trail = MouseTrail()
    size(500, 500)
    
def draw():
    global trail
    background(255)
    trail.run()
