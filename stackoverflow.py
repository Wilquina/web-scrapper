import requests
import headers
from bs4 import BeautifulSoup
from tkinter import *
from gui.scrollableFrame import ScrollableFrame


def call_so_newest_questions(frame):
    urlSeed = "https://stackoverflow.com/questions/"
    questionList = get_response(urlSeed)
    pack_questions(frame, questionList)


def call_so_bountied_questions(frame):
    urlSeed = "https://stackoverflow.com/questions/?tab=Bounties"
    questionList = get_response(urlSeed)
    pack_questions(frame, questionList)


def get_response(urlSeed):
    response = requests.get(urlSeed, headers=headers.HEADERS)

    soup = BeautifulSoup(response.text)
    questionsContainer = soup.find(id="questions")
    questionList = questionsContainer.find_all('div', class_="s-post-summary")

    return questionList


def pack_questions(frame, questionList):
    for question in questionList:
        title = "Q: " + question.find('h3').text.replace('\n', '')
        description = "A: " + question.find(class_='s-post-summary--content-excerpt').text.replace('\n', '').replace('\r', '').strip()

        question_label = Label(
            frame.scrollable_frame,
            text=title
        )

        description_label = Label(
            frame.scrollable_frame,
            text=description
        )

        question_label.pack()
        description_label.pack()


window = Tk()

frame = ScrollableFrame(window)

questions = Label(
    window,
    text="Questions",
    width=25,
    height=5
)
questions.pack()

button = Button(
   window,
   text="Call Stackoverflow bountied questions",
   command=lambda: call_so_bountied_questions(frame),
)
button.pack()

button2 = Button(
   window,
   text="Call Stackoverflow newest questions",
   command=lambda: call_so_newest_questions(frame),
)
button2.pack()

empty = Label(
    window,
    width=25,
    height=5
)
empty.pack()

frame.pack()

window.mainloop()