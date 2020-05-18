import requests
import bs4
import re
from data import *

brs_HTML = requests.get(url)
brs_Soup = bs4.BeautifulSoup(brs_HTML.text)

clear_HTML_re = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def clear_HTML(text):
    return re.sub(clear_HTML_re, '', text)

subjects_short = [subject.text.strip('</b>') \
                  for subject \
                  in brs_Soup.find('div', {'class': 'page_info'}).find_all('b')]
subjects_full = [re.findall("</b> - (.*?)</li>", str(subject))[0] \
                 for subject \
                 in brs_Soup.find('div', {'class': 'page_info'}).find_all('li')]
subjects = dict(zip(subjects_short, subjects_full))

students = brs_Soup.find('tbody').find_all('tr')
students = {clear_HTML(student.find('a').text): [int(clear_HTML(score.text)) \
            if clear_HTML(score.text) else 0 \
            for score in student.find_all('td', {'class': 'w50 no_mobile'})] \
            for student in students if student.find('a')}

inverse_participants_nicknames = {short: full for full, short in participants.items()}

participants_scores = {student: students[student] for student in students if student in participants}

def one_subject_stats(name):
    index = subjects_short.index(name)
    text = subjects[name] + '\n'
    for participant in participants_scores:
        text += participants[participant] + ': ' + str(participants_scores[participant][index]) + '\n'
    return(text[:-1])

def all_stats():
    text = 'Статистика по БРС' + '\n\n'
    for subject in subjects_short:
            text += one_subject_stats(subject) + '\n\n'
    return text[:-2]

def one_student_stats(name):
    full_name = inverse_participants_nicknames[name]
    text = name + '\n'
    for i in range(len(participants_scores[full_name])):
        text += subjects[subjects_short[i]] + ': ' + str(participants_scores[full_name][i]) + '\n'
    return text[:-1]

def show_subjects():
    text = 'Предметы:\n'
    for subject in subjects:
        text += subject + ': ' + subjects[subject] + '\n'
    return text[:-1]

def show_participants():
    text = 'Участники:\n'
    for member in inverse_participants_nicknames:
        text += member + ': ' + inverse_participants_nicknames[member] + '\n'
    return text[:-1]
