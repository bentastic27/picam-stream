FROM nginx:stable

RUN apt update && apt install python3 python3-pip --yes  && pip3 install jinja2 kubernetes && \
    apt purge --yes python3-pip && apt autoremove --yes && apt clean

COPY . /
EXPOSE 80
CMD ["bash", "/entrypoint.sh"]