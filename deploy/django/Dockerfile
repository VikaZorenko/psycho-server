FROM python:3.6-alpine3.7
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
            --upgrade \
    alpine-sdk \
    postgresql-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    libressl-dev \
    jpeg-dev \
    linux-headers

WORKDIR /wheels

COPY ./requirements.txt /wheels/requirements/
RUN pip install -U pip && pip wheel -r ./requirements/requirements.txt

FROM python:3.6-alpine3.7
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --upgrade -U \
        gettext \
        git \
        postgresql-client \
        gcc jpeg-dev cairo-dev pango-dev \
        libxml2 \
        libxslt \
        mailcap \
        xmlsec \
        openssh-keygen \
    && rm -rf /var/cache/apk/*
    
RUN wget --quiet https://releases.hashicorp.com/terraform/0.12.3/terraform_0.12.3_linux_amd64.zip \
  && unzip terraform_0.12.3_linux_amd64.zip \
  && mv terraform /usr/bin \
  && rm terraform_0.12.3_linux_amd64.zip

COPY --from=0 /wheels /wheels
RUN pip install -U pip \
        && pip install -r /wheels/requirements/requirements.txt \
                       -f /wheels \
        && rm -rf /wheels \
        && rm -rf /root/.cache/pip/*

COPY . /app
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
COPY deploy/uwsgi/uwsgi_docker.ini /uwsgi.ini
RUN mkdir /logs

WORKDIR /app/terraform/update
RUN terraform init
WORKDIR /app/terraform/create
RUN terraform init

WORKDIR /app
RUN ssh-keygen -t rsa -b 4096 -f sso/jwt-key -N ""

EXPOSE 3001/tcp

ARG app_version
ENV SERVER_VERSION=$app_version

CMD ["/docker-entrypoint.sh"]
