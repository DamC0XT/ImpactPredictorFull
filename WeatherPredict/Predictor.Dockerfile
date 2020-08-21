# Use an official Python runtime as a parent image - for a list of others see https://hub.docker.com/_/python/

FROM python:3-stretch



# Set the working directory to /app - this is a directory that gets created in the image

WORKDIR /app



# Copy the current host directory contents into the container at /app

COPY . Runner.py /app/
COPY . /MLClasses/app/ 

# Install any needed packages specified in requirements.txt
#RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt && pip3 install --upgrade pip



# Make port 4000 available to the world outside this container

EXPOSE 4000



# Run Predictor  when the container launches

CMD ["python3", "Runner.py"]
