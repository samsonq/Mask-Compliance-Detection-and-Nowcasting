FROM continuumio/miniconda:4.5.4

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt install -y python3

COPY requirements.txt /Mask-Compliance-Detection-and-Nowcasting/requirements.txt
RUN pip3 install -r /Mask-Compliance-Detection-and-Nowcasting/requirements.txt

WORKDIR /Mask-Compliance-Detection-and-Nowcasting/src
CMD python3 app.py
