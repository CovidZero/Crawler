FROM python:3.7-alpine as base

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev && \
    apk add --no-cache --virtual .lxml_deps libxslt-dev 

FROM base as build

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

FROM base as release

WORKDIR /app

RUN addgroup -S app && \
    adduser -S -G app app && \
    chown -R app:app /app

COPY . /app/
COPY --from=build /usr/local/ /usr/local

USER app

CMD python app.py --salvars3
