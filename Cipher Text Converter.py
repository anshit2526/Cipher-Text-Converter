import random
import tkinter as tk
import clipboard

random_words_range = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def result(operation, message):
    # Text box for cipher text
    status.config(text=operation)
    show = tk.Text(width=45, height=7)
    show.insert(tk.END, message)
    show.place(x=100, y=400)

    # Button for copy to clipboard
    copy_button = tk.Button(window, text="Copy", command=clipboard.copy(message))
    copy_button.place(x=470, y=400)


def paste_from_clipboard():
    text = clipboard.paste()
    text_box.delete('1.0', tk.END)  # Clear the entry widget
    text_box.insert(tk.END, text)


def encoding():
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

    cipher_text = " ".join(nwords)
    result('Cipher Text: ', cipher_text)


def decoding():
    # retrieving the key
    key = int(key_box.get("1.0", "end-1c"))

    # retrieving the message written in the text box
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

    result('Decipher Text: ', decipher_text)


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('640x640')
    window.title('Cypher Text Converter')

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

    # Button to encode
    encoding_button = tk.Button(text='Encode', command=encoding)
    encoding_button.place(x=100, y=250)

    # Button to Decode:
    decoding_button = tk.Button(text='Decode', command=decoding)
    decoding_button.place(x=170, y=250)

    # Button to Paste from clipboard
    paste_button = tk.Button(window, text="Paste", command=paste_from_clipboard)
    paste_button.place(x=470, y=50)

    # Result of Encoding and Decoding
    status = tk.Label(window)
    status.place(x=10, y=400)

    window.mainloop()
