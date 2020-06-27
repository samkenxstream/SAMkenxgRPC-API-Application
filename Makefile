setup:
	# Create python virtualenv & source
	# elec_consumption ~/.devops/bin/activate
	python3 -m venv ~/.elec_consumption &&\
			source ~\.elec_consumption\bin\activate

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
			pip install -r requirements.txt

gRPCSetUp:
# This should not be run orelse you want to experiment and try it out yourself. I have generated the file automatically and they are service_pb2.py and service_pb2_grpc.py
	#python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/service.proto
#test:
	# Additional, optional, tests could go here
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

#lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	# This is linter for Dockerfiles
	#hadolint Dockerfile
	# This is a linter for Python source code linter: https://www.pylint.org/
	# This should be run from inside a virtualenv
	#pylint --disable=R,C,W1203 client.py

all: install