if __name__ == "__main__":
    dockerfile = dict()
    dockerfile['others'] = '''
FROM python:3.8.1
RUN pip install --upgrade pip
RUN apt-get update -y
RUN apt-get install -y git
'''
    for l in open('requirements.txt'):
        l = l.strip()
        if not l or l.startswith('#'):
            continue
        dockerfile['others'] += "RUN pip install {}\n".format(l)
    dockerfile['others'] += '''
WORKDIR /app
    '''
    with open('Dockerfile', 'w') as file:
        file.write(dockerfile['others'])
