FROM python:3.10-slim-buster

RUN pip install pipenv

WORKDIR /yacg

ADD yacg.py yacg.py
ADD incrementVersion.py incrementVersion.py
ADD modelToJson.py modelToJson.py
ADD modelToYaml.py modelToYaml.py
ADD normalizeSchema.py normalizeSchema.py
ADD createRandomData.py createRandomData.py
ADD randomDataServer.py randomDataServer.py
ADD customRandomConstraints.py customRandomConstraints.py
ADD validate.py validate.py
ADD version.txt version.txt
ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
COPY yacg yacg/

#RUN cd /yacg && \
#    pipenv --python 3.8 && \
#    pipenv --three install --system

RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

WORKDIR /yacg

ENTRYPOINT [ "python3", "yacg.py"]