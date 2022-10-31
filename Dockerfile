FROM amazonlinux
ENV PYTHONUNBUFFERED=1

RUN yum update -y
RUN yum upgrade -y
RUN yum groupinstall "Development Tools" -y
RUN yum install python3-devel -y

COPY app app
COPY README.md .
COPY FortranRNG FortranRNG
COPY requirements.txt .

RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install -r requirements.txt --no-cache-dir
RUN python3 -m pip install ./FortranRNG

EXPOSE 8000
CMD uvicorn app.api:API --host=0.0.0.0 --port=8000
