FROM python:latest
ADD . /src/my_project
WORKDIR /src/my_project
EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip flask_sqlalchemy
RUN python setup.py develop
# ENTRYPOINT ["python", "wsgi.py"]
