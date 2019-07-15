import simplegui

message = "Welcome!"

# Handler for mouse clicks
def click():
    global message
    message = "You took the blue pill"

def click2():
    global message
    message = "You took the Red pill"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 500)
frame.add_button("Click me", click)
frame.add_button("No, click me", click2)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
