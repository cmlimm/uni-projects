def add_feed_to_file(file_name, feed_name, feed_link):
    with open(file_name, 'a') as file:
            file.write(feed_name + '::' + feed_link + '\n')

def read_feeds_from_file(file_name):
    feeds = {}
    with open(file_name, 'r') as file:
            for line in file.readlines():
                item = line.split('::')
                feeds[item[0]] = item[1].strip()
    return feeds

def add_keywords_to_file(file_name, keywords):
    with open(file_name, 'a') as file:
        for word in keywords:
            file.write(word.lower()+'\n')

def read_keywords_from_file(file_name):
    keywords = []
    with open(file_name, 'r') as file:
            for word in file.readlines():
                keywords.append(word.strip())
    return keywords

def bump_feeds_to_file(file_name, feeds):
    with open(file_name, 'w') as file:
        for feed in feeds.keys():
            file.write(feed + '::' + feeds[feed] + '\n')

def bump_keywords_to_file(file_name, keywords):
    with open(file_name, 'w') as file:
        for word in keywords:
            file.write(word + '\n')

def add_to_log(file_name, error):
    with open(file_name, 'w') as file:
        file.write(error)
