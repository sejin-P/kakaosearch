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
RUN pyppeteer-install
RUN ssh-keyscan -t rsa github.com > /root/.ssh/known_hosts
RUN pip install -e git+git@github.com:allganize/allganize-utils.git@v0.1.14#egg=allganize
RUN pip install -e git+https://github.com/mnpk/BERT-keras-minimal.git#egg=bertkeras


WORKDIR /app
    '''
    with open('Dockerfile', 'w') as file:
        file.write(dockerfile['others'])
