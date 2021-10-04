FROM python

LABEL Name=nlusrvverimdl Version=0.0.1



# Install Redis.
RUN \
  cd /tmp && \
  wget http://download.redis.io/redis-stable.tar.gz && \
  tar xvzf redis-stable.tar.gz && \
  cd redis-stable && \
  make && \
  make install && \
  cp -f src/redis-sentinel /usr/local/bin && \
  mkdir -p /etc/redis && \
  cp -f *.conf /etc/redis && \
  rm -rf /tmp/redis-stable* && \
  sed -i 's/^\(bind .*\)$/# \1/' /etc/redis/redis.conf && \
  sed -i 's/^\(daemonize .*\)$/# \1/' /etc/redis/redis.conf && \
  sed -i 's/^\(dir .*\)$/# \1\ndir \/data/' /etc/redis/redis.conf && \
  sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis/redis.conf

#RUN apt-get update
#RUN apt-get install vim -y

WORKDIR /app
ADD . /app

#Using pip:
RUN python -m pip install -r requirements.txt

# Define mountable directories.
VOLUME ["/data"]

# Define working directory.
WORKDIR /data

# Define default command.
#CMD ["redis-server", "/etc/redis/redis.conf --protected-mode=no &"]
CMD ["redis-server","--protected-mode","no"]

# Expose ports.
EXPOSE 6379

#RUN wget http://download.redis.io/redis-stable.tar.gz
#RUN tar xvzf redis-stable.tar.gz
#RUN cd redis-stable
#RUN make
#RUN redis-server &



#CMD [ "ls" ]
