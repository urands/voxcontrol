FROM python:3.12

RUN pip install pipenv

WORKDIR /backend

COPY ./Pipfile ./Pipfile.lock ./

RUN pipenv requirements > requirements.txt
RUN pip install --user -r requirements.txt

COPY ./ ./

CMD python -m uvicorn architecton.app:app --host 0.0.0.0 --port 8000
