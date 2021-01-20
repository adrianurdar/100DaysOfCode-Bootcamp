from tkinter import *
from tkinter import filedialog, colorchooser
from PIL import Image, ImageFont, ImageDraw


PINK = "#eb5c6c"
FONT_FAMILY = ("Helvetica", 14, "bold")
FONTS = ["Arial",
         "Courier New",
         "Comic Sans MS",
         "Fixedsys",
         "MS Sans Serif",
         "MS Serif",
         "Symbol",
         "System",
         "Times New Roman",
         "Verdana"]
POSITION_OPTIONS = ["Top-Left",
                    "Top-Right",
                    "Center",
                    "Bottom-Left",
                    "Bottom-Right"]


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("INSTAMARK")
        self.config(padx=50, pady=50)

        self.image_paths = []
        self.watermark_text = ""
        self.font_family = "Arial"
        self.font_size = 10
        self.font_color = (255, 255, 255)

        self.canvas = Canvas(width=800, height=600, highlightthickness=0)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.grid(row=9, column=0, columnspan=3)

        self.image_on_canvas = self.canvas.create_image(400, 300, image=self.logo_img)

        # UPLOAD IMAGES BUTTON
        self.upload_images_btn = Button(text="Select Images", command=self.upload_images)
        self.upload_images_btn.grid(row=1, column=0, sticky="E")

        # UPLOAD IMAGES TEXT LABEL
        self.upload_images_confirmation = Label(text=f"Only .png files allowed.", fg=PINK)
        self.upload_images_confirmation.grid(row=1, column=1, columnspan=2, sticky="W")

        # ADD WATERMARK LABEL
        self.add_text_label = Label(text="Watermark Text: ")
        self.add_text_label.grid(row=2, column=0, sticky="E")

        # ADD WATERMARK USER INPUT
        self.add_text_input = Entry(width=40)
        self.add_text_input.grid(row=2, column=1, columnspan=2, sticky="W")

        # SELECT FONT LABEL
        self.add_font_label = Label(text="Select Watermark Font: ")
        self.add_font_label.grid(row=3, column=0, sticky="E")

        # SELECT FONT DROPDOWN
        self.font_options = StringVar(self)
        self.font_options.set(FONTS[0])
        self.add_font_options = OptionMenu(self, self.font_options, *FONTS)
        self.add_font_options.grid(row=3, column=1, columnspan=2, sticky="W")

        # SELECT FONT SIZE LABEL
        self.select_font_size_label = Label(text="Select Watermark Font Size: ")
        self.select_font_size_label.grid(row=4, column=0, sticky="E")

        # SELECT FONT SIZE SLIDER
        self.select_font_size_slider = Scale(from_=10, to=40, orient=HORIZONTAL)
        self.select_font_size_slider.grid(row=4, column=1, columnspan=2, sticky="W")

        # SELECT FONT COLOR LABEL
        self.select_font_color_label = Label(text="Select Watermark Font Color: ")
        self.select_font_color_label.grid(row=5, column=0, sticky="E")

        # SELECT FONT COLOR BUTTON
        self.select_font_color_btn = Button(text="Choose Color", command=self.choose_color)
        self.select_font_color_btn.grid(row=5, column=1, columnspan=2, sticky="W")

        # SELECT WATERMARK POSITION LABEL
        self.add_position_label = Label(text="Select Position of Watermark: ")
        self.add_position_label.grid(row=6, column=0, sticky="E")

        # SELECT WATERMARK POSITION DROPDOWN
        self.position_options = StringVar(self)
        self.position_options.set(POSITION_OPTIONS[0])
        self.add_position_options = OptionMenu(self, self.position_options, *POSITION_OPTIONS)
        self.add_position_options.grid(row=6, column=1, columnspan=2, sticky="W")

        # SAVE WATERMARK
        self.save_btn = Button(text="Save Watermark", command=self.save_watermark)
        self.save_btn.grid(row=7, column=0, columnspan=3)

        # CONFIRMATION MESSAGE
        self.confirmation_message = Label(text="")
        self.confirmation_message.grid(row=8, column=0, columnspan=3)

    def choose_color(self):
        self.select_font_color = colorchooser.askcolor(title="Choose Color")

    # Allow user to upload one or more images
    def upload_images(self):
        self.image_paths = filedialog.askopenfilenames()
        self.images = [PhotoImage(file=image) for image in self.image_paths]
        print(self.images)

        # If user selected at least one image, display it on the canvas
        if len(self.images) > 0:
            self.upload_images_confirmation.config(text=f"{len(self.images)} images uploaded.")
            self.canvas.itemconfig(self.image_on_canvas, image=self.images[0])
        else:
            self.upload_images_confirmation.config(text="No images uploaded.")

    # Allow user to save and add watermark to all images
    def save_watermark(self):
        self.watermark_text = self.add_text_input.get()
        print(self.watermark_text)

        self.font_family = self.font_options.get()
        print(self.font_family)

        self.font_size = self.select_font_size_slider.get()
        print(self.font_size)

        self.font_color = self.select_font_color[1]
        print(self.font_color)

        self.watermark_position = self.position_options.get()
        print(self.watermark_position)

        # ADD WATERMARK TO THE IMAGE AND SAVE IMAGE
        if len(self.image_paths) > 0:
            for image in self.image_paths:
                print(image)
                with Image.open(image) as img:
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype(self.font_family, self.font_size)

                    # SET POSITION OF THE WATERMARK TEXT
                    if self.watermark_position == "Top-Left":
                        self.watermark_position = (25, 25)
                    elif self.watermark_position == "Top-Right":
                        self.watermark_position = (-(25 + self.font_size), img.size[1] - (25 + self.font_size))
                    elif self.watermark_position == "Center":
                        self.watermark_position = (img.size[0] / 2 - self.font_size, img.size[1] / 2 - self.font_size)
                    elif self.watermark_position == "Bottom-Left":
                        self.watermark_position = (img.size[0] - (25 + self.font_size), 25)
                    else:
                        self.watermark_position = (img.size[0] - (25 + self.font_size), img.size[1] - (25 + self.font_size))

                    draw.text(self.watermark_position, self.watermark_text, self.font_color, font=font)

                    # SAVE FILE AS A COPY OF THE ORIGINAL
                    fname = image.split("/")[-1]
                    img.save(f'copy-{fname}')
                    self.confirmation_message.config(text="Image saved.", fg="Green")
        else:
            self.confirmation_message.config(text="Please upload images.", fg=PINK)


if __name__ == "__main__":
    root = Root()
    root.mainloop()
