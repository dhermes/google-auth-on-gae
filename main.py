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

import flask
import google.auth
import google.auth.transport.requests


app = flask.Flask(__name__)

SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
MAIN_HTML = """\
<html>
  <pre>
  >>> import google.auth
  >>> scope = {scope}
  >>> credentials, _ = google.auth.default(scopes=(scope,))
  >>> credentials
  {credentials}
  >>> credentials.token is None
  {is_none}
  >>>
  >>> import google.auth.transport.requests
  >>> request = google.auth.transport.requests.Request()
  >>> credentials.refresh(request)
  >>> credentials.token
  {token!r}
</html>
"""


@app.route('/')
def main():
    credentials, _ = google.auth.default(scopes=(SCOPE,))
    is_none = credentials.token is None
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    if credentials.token is None:
        token_str = ''
    else:
        token_str = credentials.token[:15] + '...'

    return MAIN_HTML.format(
        scope=SCOPE,
        credentials=flask.escape(repr(credentials)),
        is_none=is_none,
        token=token_str,
    )
