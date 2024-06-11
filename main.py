import glob
import streamlit as st

diaries = glob.glob("diary/*.txt")

d = []

for diary in diaries:
    if diary.endswith(".txt"):
        with open(diary, "r") as files:
            content = files.read().strip()
            d.append(content)


