FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY routes/ /code/routes/
COPY validator/ /code/validator/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python app.py
