# Use an official Python runtime as a parent image
FROM python:3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/
COPY . /templates/app/
COPY .  /static/app/
COPY . /compareAnalysis/app/





# Install any needed packages specified in requirements.txt
#RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt


EXPOSE 8001:5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
