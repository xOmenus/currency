FROM python:3-alpine
VOLUME /db
RUN apk update && apk --no-cache add sqlite && mkdir /currency \
    && pip install requests
COPY main.py /currency
CMD ["python", "/currency/main.py"]

