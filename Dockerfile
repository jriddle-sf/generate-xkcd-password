# Set base image
FROM python:3.9.6-alpine

# Copy the the configuration files to /tmp/.
COPY ./conf/requirements.txt /tmp/

# Copy the the source files to 
COPY ./src/ /app/

# Set the Work Directory for pip install.
WORKDIR /tmp/

# Install Dependencies
RUN pip install --requirement requirements.txt

# Set the Work Directory for application
WORKDIR /app/

# Command to execute within the container
CMD [ "python", "password-rotation.py"]
