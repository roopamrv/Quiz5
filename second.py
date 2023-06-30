import tkinter as tk
from tkinter import messagebox

def validate_text():
    text = text_entry.get("1.0", "end-1c")  # Get the entered text
    
    min_words = int(min_words_entry.get())
    max_words = int(max_words_entry.get())
    max_part_words = int(max_part_words_entry.get())
    max_word_length = int(max_word_length_entry.get())
    
    sentences = text.split(".")
    errors = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            words = sentence.split()
            sentence_errors = []
            
            # Check sentence length
            num_words = len(words)
            if num_words < min_words or num_words > max_words:
                sentence_errors.append(f"Number of words: {num_words} (min: {min_words}, max: {max_words})")
            
            # Check first word capitalization
            first_word = words[0]
            if not first_word[0].isupper():
                sentence_errors.append(f"First word not capitalized: {first_word}")
            
            # Check last character
            last_char = sentence[-1]
            if last_char not in ["?", "!", "."]:
                sentence_errors.append(f"Invalid ending character: {last_char}")
            
            # Check word length
            for word in words:
                if len(word) > max_word_length:
                    sentence_errors.append(f"Word too long: {word}")
            
            # Check comma separation and part length
            if "," in sentence:
                parts = sentence.split(",")
                for part in parts:
                    part_words = part.split()
                    if len(part_words) > max_part_words:
                        sentence_errors.append(f"Part too long: {part}")
            
            if sentence_errors:
                errors.append((sentence, sentence_errors))
    
    if errors:
        error_message = "Invalid text:\n"
        for sentence, sentence_errors in errors:
            error_message += f"\nSentence: {sentence}\n"
            for error in sentence_errors:
                error_message += f"- {error}\n"
        
        messagebox.showerror("Validation Error", error_message)
    else:
        messagebox.showinfo("Validation Success", "Text is valid!")

# Create the main window
window = tk.Tk()
window.title("Text Validator")

# Create the text entry area
text_label = tk.Label(window, text="Enter text:")
text_label.pack()

text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Create the input form
form_frame = tk.Frame(window)
form_frame.pack()

min_words_label = tk.Label(form_frame, text="Minimum words per sentence:")
min_words_label.grid(row=0, column=0)
min_words_entry = tk.Entry(form_frame)
min_words_entry.grid(row=0, column=1)

max_words_label = tk.Label(form_frame, text="Maximum words per sentence:")
max_words_label.grid(row=1, column=0)
max_words_entry = tk.Entry(form_frame)
max_words_entry.grid(row=1, column=1)

max_part_words_label = tk.Label(form_frame, text="Maximum words per part (comma separated):")
max_part_words_label.grid(row=2, column=0)
max_part_words_entry = tk.Entry(form_frame)
max_part_words_entry.grid(row=2, column=1)

max_word_length_label = tk.Label(form_frame, text="Maximum word length:")
max_word_length_label.grid(row=3, column=0)
max_word_length_entry = tk.Entry(form_frame)
max_word_length_entry.grid(row=3, column=1)

# Create the validate button
validate_button = tk.Button(window, text="Validate", command=validate_text)
validate_button.pack()

# Start the main event loop
window.mainloop()
