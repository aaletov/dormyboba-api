PYTHON_VERSION := 3.12.0
# PYTHON_ARCHIVE := v${PYTHON_VERSION}.tar.gz
# PYTHON_LINK := https://github.com/python/cpython/archive/refs/tags/${PYTHON_ARCHIVE}
# PYTHON_SOURCE := cpython-${PYTHON_VERSION}

# ${PYTHON_SOURCE}:
# wget -qO- ${PYTHON_LINK} | tar xz

define NEWLINE


endef
export NEWLINE

define PYENV_MAGIC

Add this to your .bashrc

export PYENV_ROOT="$$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$$PYENV_ROOT/bin:$$PATH"
eval "$$(pyenv init -)"
endef
export PYENV_MAGIC

.PHONY: install-python
install-python:
ifeq ($(shell which python3),)
	ifeq ($(shell which pyenv),)
		apt update && \
			apt install -y libffi-dev pkg-config
		curl https://pyenv.run | bash
	endif
	pyenv install ${PYTHON_VERSION}
	@echo $(subst "$$NEWLINE",\n,"$$PYENV_MAGIC")
	pyenv global 3.12.0
endif

.PHONY: install-poetry
install-poetry: install-python
ifeq ($(shell which poetry),)
	curl -sSL https://install.python-poetry.org | python3 -
	${HOME}/.local/bin/poetry config virtualenvs.in-project true
endif

.PHONY: install-go
install-go:
ifeq ($(shell which go),)
	wget -qO- https://go.dev/dl/go1.21.3.linux-amd64.tar.gz | \
		tar xz -C ${HOME}/.local
endif

.PHONY: install-protoc
install-protoc:


.PHONY: install-deps
install-deps: install-python install-poetry install-go install-protoc