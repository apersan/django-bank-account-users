# Pull official base image
FROM python:3.7.4-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the rest of the applicaion's code
COPY . /usr/src/app

# Create and set work directory
WORKDIR /usr/src/app

# Install required packages
RUN apk --update add \
    bash \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    # pillow dependencies
    jpeg-dev \
    zlib-dev

# Install dependencies
RUN pip3 install --upgrade pip -r requirements.txt
