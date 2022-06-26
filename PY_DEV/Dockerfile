# setting base image
FROM python:3.9.2

# set working directory in the container
WORKDIR /WORKDIR

# copy dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install awscli
RUN pip install --requirement ./requirements.txt

# copy content of the local src directory to the working directory
COPY src/ .

# command to run on container start
# CMD ['python', './prcss_st.st_trips.py', '20220625']
