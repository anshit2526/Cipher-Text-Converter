# # # # import random
# # # #
# # # # random_words_rang = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# # # #
# # # # message = input('Enter message: ')
# # # # key = int(input("Enter key: "))
# # # #
# # # # i = 1
# # # # pre_random_words = ""
# # # # while i <= key:
# # # #     pre_random_words = pre_random_words + random.choice(random_words_rang)
# # # #     i = i + 1
# # # # print(pre_random_words)
# # # #
# # # # j = 1
# # # # post_random_word = ""
# # # # while j <= key:
# # # #     post_random_word = post_random_word + random.choice(random_words_rang)
# # # #     j = j + 1
# # # # print(post_random_word)
# # # #
# # # # words = message.split(" ")
# # # # nwords = []
# # # # for word in words:
# # # #     word = word[::-1]
# # # #     word = pre_random_words + word + post_random_word
# # # #     nwords.append(word)
# # # #     print(" ".join(nwords))
# # # #
# # # #
# # #
# # # '''Speech Recognizer'''
# # # import speech_recognition as sr
# # #
# # # def speech_to_text():
# # #     recognizer = sr.Recognizer()
# # #
# # #     with sr.Microphone() as source:
# # #         print("Listening...")
# # #         audio = recognizer.listen(source)
# # #         recognizer.energy_threshold = 50
# # #
# # #     try:
# # #         print("Transcribing...")
# # #         text = recognizer.recognize_sphinx(audio)
# # #         print("You said:", text)
# # #     except sr.UnknownValueError:
# # #         print("Sorry, I could not understand audio.")
# # #     except sr.RequestError as e:
# # #         print("Error:", str(e))
# # #
# # #
# # # # Example usage
# # # speech_to_text()
# # #
# # # '''Clipboard paste'''
# # # import tkinter as tk
# # # import clipboard
# # #
# # # # def paste_from_clipboard():
# # # #     text = clipboard.paste()
# # # #     # entry.delete('1.0', tk.END)  # Clear the entry widget
# # # #     entry.insert(tk.END, text)
# # # #
# # # # window = tk.Tk()
# # # #
# # # # # Create an entry widget to display the pasted text
# # # # entry = tk.Text(window, width=30)
# # # # entry.pack()
# # # #
# # # # # Create a button to trigger the paste operation
# # # # paste_button = tk.Button(window, text="Paste", command=paste_from_clipboard)
# # # # paste_button.pack()
# # #
# # # # window.mainloop()
# # #
# # #
# #
# #
# #
# # with open('G:/Programing and Coding/Python/Training/instagram.ico', 'rb') as file:
# #     source_code = str(file.read())
# #     list = source_code.split(" ")
# #     for l in list:
# #         print(l)
# #         print('-'*100)
# #
# #
#
#
# import tkinter as tk
# from tkinter import filedialog as fd
#
#
# def open_file():
#     file_path = fd.askopenfilename()
#     return file_path
#
#
#
#
# window = tk.Tk()
# window.title("rough")
# window.geometry('500x500')
#
# button = tk.Button(window, text='open', command=open_file)
# button.pack()
#
# file_path = open_file()
# file = file_path.split('/')[-1]
# print(file)
#
# window.mainloop()

import random

random_words_range = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
pre_random_words = list()
key = 4
i = 0
words = ""

for j in range(0, 3):

    while i != key:
        words = words + random.choice(random_words_range)
        print("words: ", words)
        i = i + 1

    pre_random_words.append(words)
    print("random words: ", pre_random_words)

print(pre_random_words)
