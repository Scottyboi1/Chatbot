import os
import tkinter
import customtkinter
from vertexai.language_models import TextGenerationModel
from PIL import Image, ImageTk

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cred.json"

model = TextGenerationModel.from_pretrained("text-bison")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minus the Chatbot Tutor")
        self.geometry(f"{1300}x{550}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.subject_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select Subject and Grade Level", font=customtkinter.CTkFont(size=13, weight="bold"))
        self.subject_label.grid(row=4, column=0, padx=20, pady=(20, 10))

        self.subject_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Science", "Math", "English", "History"])
        self.subject_menu.grid(row=5, column=0, padx=20, pady=0)

        self.grade_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Elementary School", "Middle School", "High School"])
        self.grade_menu.grid(row=6, column=0, padx=20, pady=(10, 20))

        self.get_response_button = customtkinter.CTkButton(self.sidebar_frame, text = "Get Response", command= self.get_response)
        self.get_response_button.grid(row=7, column=0, padx=20, pady=(10, 20))

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Question")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.configure(bg_color="brown", fg_color="green")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.image = Image.open("robot.png")  # Load the image with PIL
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = customtkinter.CTkLabel(self, text = " ", image=self.photo)
        self.image_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def get_response(self):
        user_input = self.entry.get()
        
        self.textbox.delete("1.0", "end")

        prompts = {
            "Elementary School": "Explain how to solve this {} question on an elementary school level. ".format(self.subject_menu.get()) + user_input,
            "Middle School": "Explain how to solve this {} question on a middle school level. ".format(self.subject_menu.get()) + user_input,
            "High School": "Explain how to solve this {} question on a high school level. ".format(self.subject_menu.get()) + user_input,
        }
        
        prompt = prompts.get(self.grade_menu.get(), user_input)
        
        parameters = {
            "candidate_count": 1,
            "max_output_tokens": 1024,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }
        response = model.predict(prompt, **parameters)
        self.textbox.insert("1.0",response.text)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
