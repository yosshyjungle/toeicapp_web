import streamlit as st
from PIL import Image
import random
import time
import webbrowser
# import pyttsx3

st.title("TOEIC英単語学習アプリ")

#トップ画像の表示
image = Image.open('toeic.png')
st.image(image, use_column_width=True)

st.header('英語が2秒間表示されます。その後日本語が1秒表示されて次の問題へ遷移します。')
st.subheader('★★問題はランダムに問出題されます★★')


st.sidebar.header('レベルに合わせて挑戦しよう！')
# st.sidebar.subheader('ボタンをクリックすると音声も流れます。音声が不要な方はミュートにしておいてください。')
def get_problems(num):

    with open(f"words{num}-1.txt", "r") as f:
        problems = f.readlines()
        # print(problems[0:10])
        problems = [x.strip() for x in problems]
    return problems

def start_english_words_test(problems):

    for index, p in enumerate(problems):
        x = p.split(",")

        english = x[0]
        japanese = x[1]
        st.write("===========第{}問目===========".format(index + 1))

        st.write(str(english))
#         engine = pyttsx3.init()
#         voices = engine.getProperty('voices')
#         engine.setProperty("voice",voices[1].id)
#         engine.say(english)
#         engine.runAndWait()

        time.sleep(2)
        st.write(str(japanese))
        time.sleep(1)



    return st.write('以上で問題は終了です')



if st.sidebar.button('TOEIC400'):
    p = get_problems(400)
    random.shuffle(p)
    start_english_words_test(problems=p)
st.sidebar.write('初級問題↑↑↑')

if st.sidebar.button('TOEIC700'):
    p = get_problems(700)
    random.shuffle(p)
    start_english_words_test(problems=p)
st.sidebar.write('中級問題↑↑↑')

if st.sidebar.button('TOEIC850'):
    p = get_problems(850)
    random.shuffle(p)
    start_english_words_test(problems=p)
st.sidebar.write('上級問題↑↑↑')


def stopping():
    return

if st.sidebar.button('STOP'):
    stopping()
st.sidebar.write('ストップ↑↑↑')





st.write('Copyright © 2021 Tomoyuki Yoshikawa. All Rights Reserved.')


