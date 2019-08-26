ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3

# Copy data for add-on
COPY data/run.sh /
COPY data/main.py /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
