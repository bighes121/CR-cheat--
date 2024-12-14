import tkinter as tk
from functools import partial

class DrawShapes:
    def __init__(self, canvas, image_id):
        self.canvas = canvas
        self.image_id = image_id
        self.rect_id = None
        self.start_x = None
        self.start_y = None

    def on_click(self, event):
        # Handle the click event to start a rectangle
        print(f"Clicked at ({event.x}, {event.y} on image: {self.image_id})")
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.start_x = event.x
        self.start_y = event.y
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="green")
        self.canvas.tag_bind(self.rect_id, "<ButtonRelease-1>", self.on_release)
        self.canvas.tag_bind(self.rect_id, "<B1-Motion>", self.on_drag)

    def on_drag(self, event):
        # Update the rectangle's coordinates as the mouse moves
        # print(f"Dragging to ({event.x}, {event.y},{self.rect_id})")
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        # Finalize the rectangle when the mouse is released
        print(f"Released at ({event.x}, {event.y})")
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, event.x, event.y)
        self.rect_id = None  # Reset after releasing
