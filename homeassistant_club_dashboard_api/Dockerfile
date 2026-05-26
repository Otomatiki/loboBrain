ARG BUILD_FROM=alpine:3.17
FROM $BUILD_FROM
# ENV LANG C.UTF-8
# SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install requirements for add-on
RUN \
    apk add --no-cache \
        python3 \
        py3-pip

# RUN pip3 install paho-mqtt


# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

# Copy data for add-on
COPY run.sh /
# COPY requirements.txt /
COPY homeassistant_club_dashboard_api /homeassistant_club_dashboard_api/

RUN pip3 install flask
RUN pip3 install flask-cors
RUN pip3 install requests
RUN pip3 install paho-mqtt
RUN pip3 install websockets
RUN pip3 install "python-socketio[client]"
RUN pip3 install flask-socketio

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]