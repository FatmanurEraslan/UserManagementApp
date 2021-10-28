FROM python:3.6
RUN mkdir /app
WORKDIR /app
COPY requirement.txt /app
ENV IN_DOCKER_CONTAINER Yes
COPY run.py /app
COPY . /app/
RUN pip3 install -r requirement.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
