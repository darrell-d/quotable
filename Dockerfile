FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

COPY . /code/

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
COPY package.json package.json  
RUN npm install
RUN apt-get install apache2 apache2-dev vim -y
RUN pip install -r requirements.txt
COPY django-apache.conf  /etc/apache2/sites-available/000-default.conf

# RUN echo "ServerName localhost" | tee -a /etc/apache2/apache2.conf
# RUN echo "LoadModule wsgi_module /usr/local/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-aarch64-linux-gnu.so" | tee -a /etc/apache2/apache2.conf
# RUN echo "Include /code/django-apache.conf" | tee -a /etc/apache2/apache2.conf