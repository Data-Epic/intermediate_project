#Use the official jupyter Docker stacks image
FROM jupyter/scipy-notebook:latest

# Copy jupyter notebook and any other files to the container
COPY . /home/jovyan/work

#work directory
WORKDIR /home/jovyan/work

#Copy requirements file
COPY requirements.txt /tmp/

#install dependencies
RUN pip install -r /tmp/requirements.txt

#Expose directory
EXPOSE 8888

#Command to run jupyter notebook
CMD ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0", "--port=88888"]
