ARG BUILD_FROM
FROM ${BUILD_FROM}

# Copy root filesystem
COPY rootfs /

	
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
		mysql-client wget \
        python3-distutils \
		jq gnupg2 sudo \
		python3-configobj python3-cheetah python3-pil \
		python3-usb python3-serial python3-mysqldb \
		tzdata procps joe \
		python3-dev \
		python3-pip netbase \
    && pip install pyephem	paho-mqtt eventlet python-socketio 
         
RUN wget -qO - https://weewx.com/keys.html | sudo apt-key add - \
	&& wget -qO - https://weewx.com/apt/weewx-python3.list | sudo tee /etc/apt/sources.list.d/weewx.list 

RUN sudo apt-get update \
    && sudo apt-get install -y weewx \
	&& apt-get clean autoclean \
    && apt-get autoremove --yes 
    
RUN wget https://github.com/anastas78/weewx-mqtt/archive/master.zip -O /tmp/weewx-mqtt.zip && \
	wget https://github.com/matthewwall/weewx-interceptor/archive/master.zip -O /tmp/weewx-interceptor.zip && \
	wget https://github.com/poblabs/weewx-belchertown/releases/download/weewx-belchertown-1.2/weewx-belchertown-release-1.2.tar.gz -O /tmp/belcher.tgz && \
	cd /tmp && \
    wee_extension --install weewx-mqtt.zip && \
	wee_extension --install weewx-interceptor.zip && \
	wee_extension --install belcher.tgz && \
	wee_config --reconfigure --driver=weewx.drivers.simulator --latitude=0 --longitude=0 --altitude=0,meter --location=unknown --units=metric --no-prompt
	  
#---- uncomment to set your timezone to other than UTC
RUN TIMEZONE="Europe/Sofia" && rm /etc/timezone && rm /etc/localtime && echo $TIMEZONE > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata	

# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION


#Labels
LABEL \
    io.hass.name="weewx" \
    io.hass.description="Full implementation of the weewx aplication for monitoring user weather station" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="aharalampiev@gmail.com" \
    org.opencontainers.image.title="Weewx" \
    org.opencontainers.image.description="Weewx Hassio addon" \
    org.opencontainers.image.vendor="Anastas Haralampiev" \
    org.opencontainers.image.authors="Anastas Haralampiev <aharalampiev@gmail.com>" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://addons.community" \
    org.opencontainers.image.source="https://github.com/anastas78/hassio-addons/" \
    org.opencontainers.image.documentation="https://github.com/anastas78/hassio-addons/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}

