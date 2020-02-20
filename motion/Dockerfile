FROM ubuntu:18.04

RUN apt update && apt install motion python3 python3-pip --yes &&  \
    pip3 install jinja2 kubernetes && apt clean && \
    mv /etc/motion/motion.conf /etc/motion/motion.conf.orig && \
    mkdir /etc/motion/conf.d

COPY motion.conf /etc/motion/motion.conf
COPY entrypoint.sh /entrypoint.sh
COPY config-gen.py /config-gen.py

CMD ["bash", "/entrypoint.sh"]