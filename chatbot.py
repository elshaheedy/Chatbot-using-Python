import random
import re
import tkinter as tk

#list of possible responses
responses = ["I'm sorry, I didn't understand that.",
             "Could you please rephrase that?",
             "I'm not sure what you mean.",
             "Can you be more specific?",
             "I'm glad you asked that.",
             "That's an interesting point.",
             "I see what you're saying.",
             "That's a good question.",
             "I'm not sure, let me check.",
             "Let me get back to you on that.",
             "I'm here to help.",
             "Is there anything else you'd like to know?",
             "Thanks for chatting with me!"]

# function that generates a response
def generate_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    # Check if user input contains certain keywords
    if 'hello' in user_input:
        return 'Hi there!'
    elif 'how are you' in user_input:
        return 'I am good, thank you for asking.'
    elif 'help' in user_input:
        return 'sure , how can i help you ?'
    elif 'what can you do ?' in user_input:
        return 'i can do basic mathematical operations '
    elif 'what is your name' in user_input:
        return 'My name is Elshaheedy Chatboot.'
    elif re.search(r'\d+[\+\-\*/]\d+', user_input):
        # If user input contains a math expression, evaluate it
        try:
            result = eval(user_input)
            return str(result)
        except:
            return "Sorry, there was an error in your expression."
    else:
        #random response
        return random.choice(responses)

#function that handles user input and generates responses
def chatbot_response():
    user_input = input_box.get()
    if user_input.lower() == 'exit':
        root.destroy()
    response = generate_response(user_input)
    output_box.configure(state='normal')
    output_box.insert(tk.END, "You: " + user_input + "\n")
    output_box.insert(tk.END, "Chatbot: " + response + "\n")
    output_box.configure(state='disabled')
    input_box.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("Elshaheedy Chatbot")

# Set the window background color
root.configure(bg='#1E1F26')

# Set the font style and size
font_style = ('Arial', 12)

# Create the input box and button
input_box = tk.Entry(root, width=50, font=font_style, relief='flat', bg='#2A2D3E', fg='white', insertbackground='white', borderwidth=0)
input_box.pack(padx=10, pady=10)
input_box.bind("<Return>", lambda x: chatbot_response())
send_button = tk.Button(root, text="Send", command=chatbot_response, font=font_style, relief='flat', bg='#5A5F7D', fg='white', activebackground='#43475F', activeforeground='white', borderwidth=0)
send_button.pack(padx=10, pady=5)

# Create the output box
output_box = tk.Text(root, width=50, height=10, font=font_style, relief='flat', bg='#2A2D3E', fg='white', borderwidth=0)
output_box.pack(padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
