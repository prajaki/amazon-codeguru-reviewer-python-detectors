#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

from flask import request
import html
import docker


# {fact rule=docker-arbitrary-container-run@v1.0 defects=1}
@app.route('/someUrl')
def docker_arbitrary_container_run_noncompliant():
    client = docker.from_env()
    img = request.args.get("image")
    # Noncompliant: Unsanitised user input is passed to `run`.
    client.containers.run(img, 'echo non compliant')
# {/fact}


# {fact rule=docker-arbitrary-container-run@v1.0 defects=0}
@app.route('/someUrl')
def docker_arbitrary_container_run_compliant():
    img = html.escape(request.args.get("image"))
    # Compliant: User input is sanitised using `html.escape`.
    client.containers.run(img, 'echo hello world')
# {/fact}
