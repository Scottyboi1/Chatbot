import os
import tkinter as tk
from vertexai.language_models import TextGenerationModel

# Set the path to your service account key JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cred.json"

# Initialize the chatbot model
model = TextGenerationModel.from_pretrained("text-bison")

# Function to get the chatbot response
def get_response(grade_level):
    user_input = input_entry.get()
    
    # Define prompts for different grade levels
    prompts = {
        "elementary": "Explain how to solve this on an elementary school level. " + user_input,
        "middle": "Explain how to solve this on a middle school level. " + user_input,
        "high": "Explain how to solve this on a high school level. " + user_input,
    }
    
    # Use the appropriate prompt based on the selected grade level
    prompt = prompts.get(grade_level, user_input)
    
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    response = model.predict(prompt, **parameters)
    response_text.set(response.text)

# Create the main window
window = tk.Tk()
window.title("Chatbot Tutor")

# Create an input entry field
input_label = tk.Label(window, text="Enter your question:")
input_label.pack()
input_entry = tk.Entry(window, width=50)
input_entry.pack()

# Create radio buttons to select the grade level
grade_level = tk.StringVar()
grade_level.set("middle")  # Default to middle school

elementary_button = tk.Radiobutton(window, text="Elementary School", variable=grade_level, value="elementary")
middle_button = tk.Radiobutton(window, text="Middle School", variable=grade_level, value="middle")
high_button = tk.Radiobutton(window, text="High School", variable=grade_level, value="high")

elementary_button.pack()
middle_button.pack()
high_button.pack()

# Create a button to get the response
get_response_button = tk.Button(window, text="Get Response", command=lambda: get_response(grade_level.get()))
get_response_button.pack()

# Create a label to display the response
response_text = tk.StringVar()
response_label = tk.Label(window, textvariable=response_text)
response_label.pack()

# Start the Tkinter main loop
window.mainloop()
