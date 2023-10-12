FROM python:3.8-alpine


RUN pip install -r requirements.txt




# Set the working directory inside the container
WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/ravenstudios/flask_shopping_list.git:main /app

COPY . /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# Define environment variable
$ENV NAME World

# Run app.py when the container launches
CMD ["python3", "gunicorn -w 4 -b 0.0.0.0:5000 app:app"]
