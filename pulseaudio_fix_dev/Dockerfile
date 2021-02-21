ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8
# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Setup base
ARG BUILD_ARCH=amd64
RUN \
    set -x \
    && apk add --no-cache \
        alsa-plugins-pulse \
        alsa-utils \
        pulseaudio-utils \
        python3

# Build arguments
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Copy files
COPY main.py /

# Labels
LABEL \
    io.hass.name="Alsa & PulseAudio Fix dev version" \
    io.hass.description="This add-on eliminates the problem of 'Device or resource busy' on computers with an external ALSA and PULSEAUDIO caused by the docker container 'hassio_audio'" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Anodev <https://github.com/OPHoperHPO>" \
    org.label-schema.description="This add-on eliminates the problem of 'Device or resource busy' on computers with an external ALSA and PULSEAUDIO caused by the docker container 'hassio_audio'" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="Alsa & PulseAudio Fix dev version" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/OPHoperHPO/hassio-addons/tree/master/pulseaudio_fix_dev" \
    org.label-schema.usage="https://github.com/OPHoperHPO/hassio-addons/tree/master/pulseaudio_fix_dev" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/OPHoperHPO/hassio-addons/tree/master/pulseaudio_fix_dev" \
    org.label-schema.vendor="Anodev <https://github.com/OPHoperHPO>"

CMD [ "python3", "/main.py" ]
