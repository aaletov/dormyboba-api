PYTHON_VERSION := 3.12.0
GO_VERSION := 1.21.3
PROTOC_VERSION := 24.4
PROTOC_GEN_GO_VERSION := 1.31.0
PROTOC_GEN_GO_GRPC_VERSION := 1.3.0

get_version = $(shell echo $(1) | grep -Eo '([0-9]+\.)+[0-9]+')
get_python_version = $(call get_version,$(shell python3 --version))
get_go_version = $(call get_version,$(shell go version))
get_protoc_version = $(call get_version,$(shell protoc --version))
get_protoc_gen_go_version = $(call get_version,$(shell protoc-gen-go --version))
get_protoc_gen_go_grpc_version = $(call get_version,$(shell protoc-gen-go-grpc --version))

install-protoc-gen-go:
	go install google.golang.org/protobuf/cmd/protoc-gen-go@v${PROTOC_GEN_GO_VERSION}

install-protoc-gen-go-grpc:
	go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v${PROTOC_GEN_GO_GRPC_VERSION}


gen-go:
ifneq ($(call get_python_version),${PYTHON_VERSION})
	$(error ti eblan)
endif
ifneq ($(call get_go_version),${GO_VERSION})
	$(error ti vashe eblan)
endif
ifneq ($(call get_protoc_version),${PROTOC_VERSION})
	$(error ti vashe vashe eblan)
endif
ifneq ($(call get_protoc_gen_go_version),${PROTOC_GEN_GO_VERSION})
	$(error ti vashe vashe vashe eblan)
endif
ifneq ($(call get_protoc_gen_go_grpc_version),${PROTOC_GEN_GO_GRPC_VERSION})
	$(error ti vashe vashe vashe vashe eblan)
endif
	protoc ./api/v1api.proto \
		--go-grpc_opt=paths=source_relative \
		--go-grpc_out=./api/generated/go

.PHONY: gen-python
gen-python:
	cd ./api/generated/python && poetry run python3 -m grpc_tools.protoc \
		-I../.. \
		--python_out=. \
		--pyi_out=. \
		--grpc_python_out=. \
		../../v1api.proto

.PHONY: gen-all
gen-all: gen-go gen-python
