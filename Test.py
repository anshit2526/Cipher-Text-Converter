import random
import tkinter as tk
import clipboard
from tkinter import filedialog

random_words_range = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,<.>/?;:'"[{]}\|`~!@#$%^&*()_+=-"



def open_file():
    """This function is used to open a file by dialog box."""
    file_path = filedialog.askopenfilename()  # file_path variable store the complete path of the file.
    print(file_path)

    # display the file on text box
    file = file_path.split("/")
    text_box.insert(tk.END, file[-1]+"\n")
    return file_path


def operation_on_file():
    file = open_file()
    with open(file, 'rb') as f:
        print(file)


def result(operation, message):
    """This function displays the output in the text box of that function in which it is called."""
    # Text box for cipher text
    status.config(text=operation)
    show = tk.Text(width=45, height=7)
    show.insert(tk.END, message)
    show.place(x=100, y=400)

    # Button for copy to clipboard
    copy_button = tk.Button(window, text="Copy", command=clipboard.copy(message))
    copy_button.place(x=470, y=400)

    key_box.delete('1.0', tk.END)
    text_box.delete('1.0', tk.END)


def paste_from_clipboard():
    """This function paste the content from clipboard on the text box."""
    text = clipboard.paste()
    text_box.delete('1.0', tk.END)  # Clear the entry widget
    text_box.insert(tk.END, text)


def encoding():
    """This function encodes the text received from the text box on the basis of specific key."""
    # retrieving the key
    key = int(key_box.get("1.0", "end-1c"))

    # retrieving the message written in the text box
    message = text_box.get("1.0", "end-1c")

    # Encoding
    i = 1
    pre_random_words = ""
    while i <= key:
        pre_random_words = pre_random_words + random.choice(random_words_range)
        i = i + 1

    j = 1
    post_random_word = ""
    while j <= key:
        post_random_word = post_random_word + random.choice(random_words_range)
        j = j + 1

    words = message.split(" ")
    nwords = []
    for word in words:
        word = word[::-1]
        word = pre_random_words + word + post_random_word
        nwords.append(word)

    # putting all words together from the list nwords.
    cipher_text = " ".join(nwords)

    # calling the result method to display the encoded text.
    result('Cipher Text: ', cipher_text)


def decoding():
    """This function decodes the text received from text box using the the specific key."""
    # retrieving the key from text box as integer
    key = int(key_box.get("1.0", "end-1c"))

    # retrieving the message written in the text box as string
    message = text_box.get("1.0", "end-1c")

    # Decoding
    words = message.split(" ")
    nwords = []
    for word in words:
        word = word[key:len(word)]
        word = word[:len(word) - key]
        word = word[::-1]
        nwords.append(word)

    decipher_text = " ".join(nwords)

    # calling result function to display the decoded text.
    result('Decipher Text: ', decipher_text)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('640x640')
    window.title('Test')

    # Label
    label1 = tk.Label(text='Write message: ')
    label1.place(x=10, y=50)

    # Taking message from user
    text_box = tk.Text(width=45, height=7)
    text_box.place(x=100, y=50)

    # Taking Key from user
    label2 = tk.Label(text='Enter Key: ')
    label2.place(x=10, y=190)

    key_box = tk.Text(width=10, height=1)
    key_box.place(x=100, y=190)

    # Encode
    encoding_button = tk.Button(text='Encode', command=encoding)
    encoding_button.place(x=100, y=250)

    # Decode:
    decoding_button = tk.Button(text='Decode', command=decoding)
    decoding_button.place(x=170, y=250)

    # Paste
    paste_button = tk.Button(window, text="Paste", command=paste_from_clipboard)
    paste_button.place(x=470, y=50)

    # Result of Encoding and Decoding
    status = tk.Label(window)
    status.place(x=10, y=400)

    # Open Button for open file
    open_f = tk.Button(window, text='Open', command=open_file)
    open_f.place(x=470, y=80)


    window.mainloop()
