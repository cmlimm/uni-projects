from datetime import datetime

def read_feeds(file_name):
    feeds = {}
    with open(file_name, 'r') as file:
        for line in file.readlines():
            item = line.split('::')
            if item[3].strip() == 'True':
                summary = True
            else:
                summary = False
            feeds[item[0]] = {'link':item[1], 'date':item[2], 'summary':summary}
    return feeds

def read_keywords(file_name):
    keywords = {}
    with open(file_name, 'r') as file:
        for line in file.readlines():
            temp = line.split('::')
            feed = temp[0]
            words = temp[1].split()
            keywords[feed] = words
    return keywords

def bump_feeds(file_name, feeds):
    with open(file_name, 'w') as file:
        for feed in feeds.keys():
            file.write(feed + '::' + feeds[feed]['link'] + '::' +\
            feeds[feed]['date'] + '::' + str(feeds[feed]['summary'])+'\n')

def bump_keywords(file_name, keywords):
    with open(file_name, 'w') as file:
        for feed in keywords:
            file.write(feed + '::' + ' '.join(keywords[feed])+'\n')

def add_to_log(file_name, error):
    with open(file_name, 'a') as file:
        file.write(error+datetime.now().strftime("%d %b %H:%M:%S")+'\n\n')
