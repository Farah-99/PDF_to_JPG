import tkinter.filedialog
from tkinter import *
from tkinter import messagebox
from pdf2image import convert_from_path


class Convertor:

    # method that allow o choose a file among the ones on the desktop// return path
    def choose(self):
        global file
        file = tkinter.filedialog.askopenfilename()
        # print(file)
        return file

    # Convert file from pdf to image and store in the file
    def pdf2img(self):
        try:
            # print(file)
            images = convert_from_path(file, 500, poppler_path=r'C:\Users\css\Downloads\poppler-21.03.0\Library\bin')
            for img in images:
                fname = "C:\\Users\\css\\Documents\\Internship\\output.jpg"
                img.save(fname, 'JPEG')
        except:
            result = "failure"
            messagebox.showinfo("Result", result)

        else:
            result = "success"
            messagebox.showinfo("Result", result)

    def gui(self):
        master = Tk()
        master.title("Pdf2Image")

        b2 = Button(master, text="Choose File", command=self.choose)
        b2.grid(row=0, column=1, columnspan=1, padx=15)

        b = Button(master, text="Convert File", command=self.pdf2img)
        b.grid(row=0, column=2, columnspan=2, padx=15, pady=15)

        mainloop()


if __name__ == '__main__':
    c = Convertor()
    c.gui()
