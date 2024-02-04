PYTHON_VERSION := 3.12.0
PROTOC_VERSION := 24.4

get_version = $(shell echo $(1) | grep -Eo '([0-9]+\.)+[0-9]+')
get_protoc_version = $(call get_version,$(shell protoc --version))

.PHONY: gen-python
gen-python:
	cd ./api/generated/python && \
		poetry install && \
		poetry run python3 -m grpc_tools.protoc \
		-I../.. \
		--python_out=. \
		--pyi_out=. \
		--grpc_python_out=. \
		../../v1api.proto

.PHONY: gen-all
gen-all: gen-python
