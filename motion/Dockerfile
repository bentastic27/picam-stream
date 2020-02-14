FROM ubuntu:18.04
RUN apt update && apt install motion --yes && apt clean
RUN rm /etc/motion/motion.conf
COPY motion.conf /etc/motion/motion.conf