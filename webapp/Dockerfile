FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1# Section 3- Compiler and OS libraries
#RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev && rm -rf /var/lib/apt/lists/*# Section 4- Project libraries and User Creation

EXPOSE 8000/tcp

# Add code
ADD ./running /srv/running

# Install application requirements
ADD ./config/requirements.txt /srv/running/
RUN pip install -r /srv/running/requirements.txt

# # Add start script
# ADD ./config/start.sh /

# Add uWSGI config
ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# # Add database check script
# ADD ./config/database-check.py /srv/config/database-check.py

# Create django user, will own the Django app. This is needed
# because we defined this, in the uwsgi.ini file
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/running

# Execute start script
#CMD ["./start.sh"]
RUN python /srv/running/manage.py runserver

