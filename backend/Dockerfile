FROM continuumio/anaconda3

# attach current dir
ADD . /backend/

# install requirements
RUN pip install -r /backend/requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "/backend/app.py"]
