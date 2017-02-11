FROM python:3.5

ENV PYTHONUNBUFFERED 1

WORKDIR /var/src/app

ADD requirements.txt .
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

# install the protobuf compiler
RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -yq --no-install-recommends \
        protobuf-compiler \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh .
ENTRYPOINT ["bash", "entrypoint.sh"]
