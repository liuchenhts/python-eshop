 FROM python:3
 ENV PYTHONUNBUFFERED 1
 ARG working_dir=/code
 RUN mkdir ${working_dir}
 ADD . ${working_dir}/
 WORKDIR ${working_dir}
 RUN pip install --trusted-host pypi.python.org -r requirements.txt
