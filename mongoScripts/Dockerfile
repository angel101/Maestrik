FROM gettyimages/spark
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY  importdatasetwithclusterstomongo.py /code/
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
#COPY . /code/
#RUN python3 manage.py migrate