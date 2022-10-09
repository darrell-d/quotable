FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir .aws
COPY .aws/config /root/.aws/


RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

COPY . /code/
RUN chmod +x backup.sh


RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
COPY package.json package.json  
RUN npm install
RUN apt-get install apache2 apache2-dev vim -y
RUN pip install -r requirements.txt

RUN echo "ServerName localhost" | tee -a /etc/apache2/apache2.conf
RUN echo "LoadModule wsgi_module /usr/local/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so" | tee -a /etc/apache2/apache2.conf
RUN echo "Include /code/django-apache.conf" | tee -a /etc/apache2/apache2.conf

# RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell

# Setup cronjob
RUN apt-get install -y cron
RUN echo "00 12 1 * * /code/backup.sh" | tee -a /var/spool/cron/crontabs/root
RUN service cron restart