FROM python:3.9.5-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && pip install pip-tools
COPY ./requirements.in .
RUN pip-compile requirements.in > requirements.txt && pip-sync
RUN pip install -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

CMD python manage.py run -h 0.0.0.0