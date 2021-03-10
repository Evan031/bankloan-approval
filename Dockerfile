# Python and Linux Version
FROM frolvlad/alpine-python-machinelearning

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

# Configure Server
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory
WORKDIR /app

ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]

# CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
