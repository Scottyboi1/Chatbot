import os
import tkinter as tk
from vertexai.language_models import TextGenerationModel

# Set the path to your service account key JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cred.json"

# Initialize the chatbot model
model = TextGenerationModel.from_pretrained("text-bison")

# Function to get the chatbot response
def get_response():
    user_input = input_entry.get()
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    response = model.predict(user_input, **parameters)
    response_text.set(response.text)

# Create the main window
window = tk.Tk()
window.title("Chatbot Tutor")

# Create an input entry field
input_label = tk.Label(window, text="Enter your question:")
input_label.pack()
input_entry = tk.Entry(window, width=50)
input_entry.pack()

# Create a button to get the response
get_response_button = tk.Button(window, text="Get Response", command=get_response)
get_response_button.pack()

# Create a label to display the response
response_text = tk.StringVar()
response_label = tk.Label(window, textvariable=response_text)
response_label.pack()

# Start the Tkinter main loop
window.mainloop()
