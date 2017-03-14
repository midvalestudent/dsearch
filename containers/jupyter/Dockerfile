FROM python:3.5

# all the gosu stuff here is so that files in docker's mounted volumes have
#   same permissions and ownership as the host caller
#   see: http://denibertovic.com/posts/handling-permissions-with-docker-volumes/

# get ready for python
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

# install gosu -- install requirements
RUN DEBIAN_FRONTEND=noninteractive \
    && REPO=http://cdn-fastly.deb.debian.org \
    && echo "deb $REPO/debian jessie main\ndeb $REPO/debian-security jessie/updates main" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -yq --no-install-recommends \
        ca-certificates \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install gosu -- package download
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

# install package requirements for this project
WORKDIR /usr/local/bin

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD entrypoint.sh .
ENTRYPOINT ["/bin/bash", "/usr/local/bin/entrypoint.sh"]
