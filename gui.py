from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkfilebrowser import askopenfilenames
from pdf2image import convert_from_path
from draw import DrawShapes

def c_open_file():
    repl = []
    rep = askopenfilenames(parent=parent, initialdir='/', initialfile='tmp',
                           filetypes=[("Pictures or pdf ", "*.png|*.jpg|*.JPG|*.pdf"), ("All files", "*")])
    for i in range(len(rep)):
        repl.append(rep[i])
        for j in range(len(repl[i])):
            if repl[i][j] == "\\":
                repl[i] = repl[i][:j] + "/" + repl[i][j+1:]
    return repl
img_li = []
def get_img():
    rep = c_open_file()
    if rep:
        if len(rep) >= 1:
           
            try:
                for i in range(len(rep)):
                    print(rep[i])
                    if rep[i][-3:]=="pdf":
                        print("ddd")
                        images = convert_from_path(rep[i],size=(255*2,330*2),fmt="png") ###convert pdf to img f list images 
                        for i in range(len(images)):
                            img = ImageTk.PhotoImage(images[i])
                        # img = Image.open(rep[i])       ### kola img jat mn pdf tahia katzad f list dial images li aybano 
                        # img = ImageTk.PhotoImage(img)
                            img_li.append(img)
                    else: 
                        img = Image.open(rep[i])
                        img=img.resize((255*2,330*2))
                        img = ImageTk.PhotoImage(img)
                        img_li.append(img)
                return img_li
            except Exception as e:
                print("Error opening image:", e)
                return None

parent = Tk()
parent.geometry("1200x590")
parent.title("Modern Image Viewer")

# Configure a dark theme for the UI
parent.configure(bg="#2E2E2E")

# Create a left-side panel for controls
control_panel = Frame(parent, bg="#2E2E2E", width=100)
control_panel.pack(side=RIGHT, fill=Y,padx=60)

# Add a title to the control panel
Label(control_panel, text="MY_APP", font=('Helvetica', 16, 'bold'), bg="#2E2E2E", fg="white").pack(pady=20)

# Open button in the control panel
openBtn = Button(control_panel, text="Open Images", command=lambda: handle_img(),
                 bg="#4C4C4C", fg="white", activebackground="#5C5C5C", activeforeground="white", relief=FLAT,pady=11, padx=20)
openBtn.pack(pady=10, padx=10, fill=X)

# Scrollable frame for displaying images
image_frame = Frame(parent, bg="#2E2E2E")
image_frame.pack(side=LEFT, fill=BOTH, expand=True)



canvas = Canvas(image_frame, bg="#2E2E2E")
scrollable_frame = Frame(canvas, bg="#2E2E2E")
scrollbar = Scrollbar(image_frame, orient=VERTICAL, command=canvas.yview)

scrollable_frame_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
all_ids = canvas.find_all()
print(all_ids)
scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# lable_frame_window = canvas.create_window((255, 0), window=scrollable_frame, anchor="nw")
# canvas.bind("<Configure>",update_canvas_width)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)


# c = DrawShapes(scrollable_frame)
# c.pack()
# canvas.create_rectangle(50,50,50,50, width=5, fill='green')
# if __name__ == '__main__':
#     main()
img_ids=[]
def handle_img():
    # Use the existing logic to get images
    img_li = get_img()
    if img_li:
        canvas.delete("all")  # Clear any previous images from the canvas
        y_offset = 10  # Start with an initial vertical offset
        for img in img_li:
            # Center the image horizontally based on the canvas width
            canvas_width = canvas.winfo_width()
            image_width = img.width()
            x_center = max(0, (canvas_width - image_width) // 2)
            # Create the image on the canvas
            img_id=canvas.create_image(x_center, y_offset, image=img, anchor="nw")
            drawer = DrawShapes(canvas,img_id)
            img_ids.append(id)
            print("img_id: ",img_ids)
            # Increase y_offset for the next image (stack vertically)
            y_offset += img.height() + 20  # Add spacing between images
            # canvas.tag_bind(img_id, "<Button-1>", lambda event, id=img_id: drawer.on_click(event))
            # canvas.tag_bind(img_id, "<B1-Motion>", drawer.on_drag)
            # canvas.tag_bind(img_id, "<ButtonRelease-1>", drawer.on_release)
            canvas.tag_bind(img_id, "<Button-1>", lambda event, drawer=drawer: drawer.on_click(event))
            canvas.tag_bind(img_id, "<B1-Motion>", lambda event, drawer=drawer: drawer.on_drag(event))
            canvas.tag_bind(img_id, "<ButtonRelease-1>", lambda event, drawer=drawer: drawer.on_release(event))
        
        # Update the scrollable area of the canvas
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        print("Error with image list")

# Ensure the Canvas's scroll region is properly updated after adding images
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# def on_click(event,id):
#     print(f"Clicked at ({event.x}, {event.y}) on item {id}")
#     coords = canvas.coords(id)
#     scroll_y = canvas.yview()[0]  # Scroll position as a fraction of total scrollable area
#     x, y = event.x, coords[1]+event.y  # Use the first corner of the item's bounding box
#     rect_id = canvas.create_rectangle(x, y, x + 20, y + 20, fill="green")
#     rc=canvas.coords(rect_id)
#     canvas.tag_bind(rect_id, "<Button-1>",lambda event: on_click_rectangle(event,rect_id))
#     canvas.tag_bind(rect_id, "<Button-3>",lambda event: move(event,rect_id))

#     print("rec coords ",rc,id)
# def on_click_rectangle(event,rect_id):
#     rc=canvas.coords(rect_id)
#     x0,y0,x1,y1=rc
#     canvas.bind(rect_id,"<B1-Motion>", lambda event: move(event,rect_id))  # Resize the rectangle
#     print("on click rectangle",rc)
#     canvas.coords(rect_id,x0,y0,event.x ,event.y)
# def move(event,rect_id):
#     rc=canvas.coords(rect_id)
#     canvas.move(rect_id,event.x,event.y)
#     print("move me ")
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
    
# # Center scrollable_frame contents when Canvas is resized
def update_canvas_width(event):
    canvas_width = event.width
    scrollable_frame_width = scrollable_frame.winfo_reqwidth()
    x_offset = max((canvas_width - scrollable_frame_width) // 2, 0)
    canvas.coords(scrollable_frame_window, x_offset, 0)
    return x_offset,scrollable_frame_width
canvas.bind("<Configure>", update_canvas_width)


parent.mainloop()
