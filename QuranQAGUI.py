import torch
from transformers import BertTokenizerFast, BertForQuestionAnswering

def get_answer_from_model(model_path, passage, question):
    tokenizer = BertTokenizerFast.from_pretrained(model_path)
    model = BertForQuestionAnswering.from_pretrained(model_path)
    #Ensure the model is in evaluation mode
    model.eval()
    
    #Define the device
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)

    #Tokenize the input context and question
    inputs = tokenizer.encode_plus(question, passage, return_tensors='pt')
    
    #Move inputs to the specified device
    input_ids = inputs['input_ids'].to(device)
    attention_mask = inputs['attention_mask'].to(device)
    
    #Perform a forward pass to get the model's output for the given inputs
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
    
    #Get the predicted start and end positions
    start_logits = outputs['start_logits']
    end_logits = outputs['end_logits']
    
    start_idx = torch.argmax(start_logits, dim=1).item()
    end_idx = torch.argmax(end_logits, dim=1).item()
    
    #Decode the predicted answer from the input ids
    answer_ids = input_ids[0][start_idx:end_idx+1]
    answer = tokenizer.decode(answer_ids, skip_special_tokens=True)
    return answer
    
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, OptionMenu, Text, Scrollbar, Frame

model_name = ""

def open_popup(passage, question):
    global popup, text_widget
    
    window.destroy()
    
    # Create a new window
    popup = Tk()
    popup.title("Popup Window")
    popup.geometry("640x480")
    
    # Create a StringVar for the dropdown menu
    selected_option = StringVar(popup)
    selected_option.set("AraBERT")  # Set default option
    
    # Create a dropdown menu
    options = ["AraBERT", "MARBERT"]
    dropdown_menu = OptionMenu(popup, selected_option, *options, command=option_selected)
    dropdown_menu.pack(pady=10)
    
    global model_name  
    model_name = 'model/araBert-quranQA'
    
    # Create a frame to hold the Text widget and scrollbar
    text_frame = Frame(popup)
    text_frame.pack(pady=10, padx=10, fill='both', expand=True)
    
    # Create a Text widget for multi-line text display
    text_widget = Text(text_frame, wrap='word', bg="#D9D9D9", fg="#000716", bd=0, height=15)
    text_widget.config(state='disabled')  # Make the Text widget read-only
    
    # Create a vertical scrollbar
    scrollbar = Scrollbar(text_frame, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    
    # Pack the Text widget and scrollbar
    text_widget.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    # Create a button that displays text
    display_button = Button(popup, text="Display Text", command=lambda: display_text(popup, get_answer_from_model(model_name, passage, question)))
    display_button.pack(pady=10)

    # Define on_closing function
    def on_closing():
        popup.destroy()
        view_main_window()
    
    popup.protocol("WM_DELETE_WINDOW", on_closing)

def option_selected(option):
    global model_name  
    if option == "AraBERT":
        model_name = 'model/araBert-quranQA'
    elif option == "MARBERT":
        model_name = 'model/MARBERT-quranQA'

def display_text(popup, text):
    global text_widget
    
    # Clear the existing text in the Text widget
    text_widget.config(state='normal')  # Allow editing
    text_widget.delete('1.0', 'end')  # Clear all text
    
    # Insert the new text
    text_widget.insert('1.0', text)
    text_widget.config(state='disabled')  # Make the Text widget read-only



from pathlib import Path
import os

# from tkinter import *
# Explicit imports to satisfy Flake8


# Determine the root directory
if '__file__' in globals():
    ROOT_DIR = Path(__file__).parent
else:
    # Fallback to current working directory
    ROOT_DIR = Path(os.getcwd())

# Define the assets directory relative to the root directory
ASSETS_PATH = ROOT_DIR / Path("assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def view_main_window():
    global window
    window = Tk()

    window.geometry("632x455")
    window.configure(bg="#FFFFFF")
    
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=455,
        width=632,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    
    canvas.create_rectangle(
        0.0,
        0.0,
        632.0,
        455.0,
        fill="#FFFFFF",
        outline=""
    )
    
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        316.0,
        36.0,
        image=image_image_1
    )
    
    canvas.create_text(
        0.0,
        20.0,
        anchor="nw",
        text="نظام سؤال وجواب في كتاب اللَّه الكريم",
        fill="#000000",
        font=("AnonymousPro Regular", 20 * -1)
    )
    
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        316.0,
        223.5,
        image=entry_image_1
    )
    entry_1 = Text(
        window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=43.0,
        y=127.0,
        width=546.0,
        height=191.0
    )
    
    canvas.create_text(
        33.0,
        93.0,
        anchor="nw",
        text="قم بادخال النص القرآني هنا",
        fill="#000000",
        font=("AnonymousPro Regular", 20 * -1)
    )
    
    canvas.create_text(
        33.0,
        333.0,
        anchor="nw",
        text="قم بادخال السؤال هنا",
        fill="#000000",
        font=("AnonymousPro Regular", 20 * -1)
    )
    
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        316.0,
        379.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=43.0,
        y=367.0,
        width=546.0,
        height=23.0
    )
    
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_popup(entry_1.get("1.0", "end-1c"), entry_2.get()),
        relief="flat"
    )
    button_1.place(
        x=282.0,
        y=401.0,
        width=68.0,
        height=40.0
    )
    
    window.resizable(False, False)
    window.mainloop()
    
view_main_window()