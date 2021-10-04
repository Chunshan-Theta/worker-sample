#FROM python:3.7.3-alpine
FROM  python:3.7


WORKDIR /app
ADD . /app

#Using pip:
RUN python -m pip install -r requirements.txt
#RUN apt-get install vim -y

#CMD ["python", "server.py"]
CMD /bin/bash
CMD python3 simpleServer.py
