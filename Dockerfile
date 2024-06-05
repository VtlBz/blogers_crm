FROM python:3.10.13-alpine3.19

EXPOSE 8000/tcp

RUN --mount=type=bind,source=/infra_dev,target=/tmp/infra \
  /tmp/infra/docker_assembling.sh

RUN --mount=type=bind,source=./requirements.txt,target=/tmp/requirements.txt \
  pip3 install --upgrade pip && pip3 install --upgrade setuptools \
  && pip3 install -r /tmp/requirements.txt --no-cache-dir

WORKDIR /blogers_csm_backend

COPY src .

RUN export DJANGO_DEBUG_STATE=True && python manage.py collectstatic --no-input

USER master

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ]