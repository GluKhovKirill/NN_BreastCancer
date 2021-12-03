FROM python:3.8-slim-buster
COPY server.py server.py
COPY model.pckl model.pckl
RUN pip3 install flask
RUN pip3 install -U scikit-learn
CMD ["python3", "-u", "server.py"]
