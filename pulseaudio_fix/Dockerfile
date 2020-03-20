ARG BUILD_FROM=hassioaddons/base:7.0.2
FROM $BUILD_FROM
ENV LANG C.UTF-8
# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Add env
ENV TERM="xterm-256color"

# Copy Python requirements file
COPY requirements.txt /tmp/

# Setup base
ARG BUILD_ARCH=amd64
RUN \
    apk add --no-cache \
        alsa-plugins-pulse=1.2.1-r0 \
        alsa-utils=1.2.1-r0 \
        pulseaudio-utils=13.0-r2 \
        python3=3.8.2-r0 \
    && pip3 install \
        --no-cache-dir \
        --find-links "https://wheels.home-assistant.io/alpine-3.11/${BUILD_ARCH}/" \
        -r /tmp/requirements.txt

# Build arguments
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="Alsa & Pulseaudio Fix" \
    io.hass.description="Fixes alsa device busy issue on desktop systems with external alsa & pulse server" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Anodev <https://github.com/OPHoperHPO>" \
    org.label-schema.description="Fixes alsa device busy issue on desktop systems with external alsa & pulse server" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="Alsa & Pulseaudio Fix" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/OPHoperHPO" \
    org.label-schema.usage="https://github.com/OPHoperHPO" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/OPHoperHPO" \
    org.label-schema.vendor="Anodev"

# Copy data for add-on
COPY data/run.sh /
COPY data/main.py /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]