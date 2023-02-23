# start by pulling the python image
FROM python:3.9.7-slim-bullseye

RUN apt-get update && apt-get -y install \
gcc \
libgtk-3-dev \
libpq-dev \
locales \
&& rm -rf /var/lib/apt/lists/ \
&& sed -i 's/^# *\(es_ES.UTF-8\)/\1/' /etc/locale.gen \
&& locale-gen

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]