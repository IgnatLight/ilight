import base64

import streamlit as st

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local("1.jpg")



st.snow()

st.header("Проект Игната")

st.write("проект по курсу Python")

st.title("тест на знание Python")
st.text("тест помогает понять свои знания Python")

right_quest = 0

question1 = st.radio(
"каким является язык Python",
('компилируемый', 'Интерпретируемый', 'ни один ответ не верен'))
if question1 == 'Интерпретируемый':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question2 = st.radio(
"что такое Git",
('язык программирования', 'система управления версиями', 'ни один ответ не верен'))
if question2 == 'система управления версиями':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question3 = st.radio(
"команда list нужна для...",
('списков', 'чисел', 'строк'))
if question3 == 'списков':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question4 = st.radio(
"что такое docstring?",
('строка документации', 'строка ввода', 'строка списка'))
if question4 == 'строка документации':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question5 = st.radio(
"что такое модуль?",
('это директория', 'это файл', 'ни один ответ не верен'))
if question5 == 'это файл':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question6 = st.radio(
"каким является язык Python?",
('компилируемый', 'Интерпретируемый', 'ни один ответ не верен'))
if question6 == 'Интерпретируемый':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question7 = st.radio(
"что такое Git?",
('язык программирования', 'система управления версиями', 'ни один ответ не верен'))
if question7 == 'система управления версиями':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question8 = st.radio(
"команда list нужна для....",
('списков', 'чисел', 'строк'))
if question8 == 'списков':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question9 = st.radio(
"что такое docstring?.",
('строка документации', 'строка ввода', 'строка списка'))
if question9 == 'строка документации':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

question10 = st.radio(
"что такое модуль?.",
('это директория', 'это файл', 'ни один ответ не верен'))
if question10 == 'это файл':
    st.write('ответ верен')
    right_quest += 1
else:
    st.write('ответ неверен')

st.write('Количество правильных ответов:', right_quest)

