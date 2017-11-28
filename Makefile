# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

PY27?=python2.7
DEV_APPSERVER?=$(shell which dev_appserver.py)

help:
	@echo 'Makefile for google-auth-on-gae'
	@echo ''
	@echo 'Usage:'
	@echo '   make app-run       Run app'
	@echo '   make clean         Clean generated files'
	@echo ''

lib: requirements.txt
	rm -fr lib
	$(PY27) -m pip install \
	    --target lib \
	    --requirement requirements.txt
	# Remove deps handled by GAE
	rm -f lib/six.py*
	rm -fr lib/six-*.dist-info

clean-env:
	$(PY27) -m virtualenv --python=$(PY27) clean-env
	clean-env/bin/pip install \
	    --requirement env-requirements.txt

app-run: lib clean-env app.yaml
	clean-env/bin/python2.7 $(DEV_APPSERVER) app.yaml

clean:
	rm -f \
	    *pyc
	rm -fr \
	    clean-env \
	    lib

.PHONY: help app-run clean
