FROM django
ADD Code /Code
RUN apt-get update
RUN apt-get install python-pip -y
RUN pip install -r /Code/requirements.txt
