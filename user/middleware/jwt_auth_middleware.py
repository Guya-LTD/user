# -*- coding: utf-8 -*-

"""Copyright Header Details

Copyright
---------
    Copyright (C) Guya , PLC - All Rights Reserved (As Of Pending...)
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential

LICENSE
-------
    This file is subject to the terms and conditions defined in
    file 'LICENSE.txt', which is part of this source code package.

Authors
-------
    * [Simon Belete](https://github.com/Simonbelete)
 
Project
-------
    * Name: 
        - Guya E-commerce & Guya Express
    * Sub Project Name:
        - Branch Service
    * Description
        - Branch location and details service
"""


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style


This module contains the factory function 'create_app' that is
responsible for initializing the application according
to a previous configuration.
"""

import requests
from flask import jsonify, make_response

from user.endpoint import Endpoint

class JWTAuthMiddleWare(object):
    """Simple WSGI middleware."""

    def __init__(self, request):
        self.endpoint = Endpoint()
        self.request = request 
        self.response = None
        self.user = None

    def authorize(self): 
        if not self.request.headers.get('Authorization'):
            # No Authorization header not found
            # Return U 401 status code
            self.response =  make_response(jsonify({
                'status_code': 401,
                'status': 'Unauthorized',
                'message': 'Authorization not found on header',
            }), 401)
            return False
        else:
            authorization = self.request.headers.get('Authorization')
            # Authorization header
            headers = {
                'Content-type': 'text/json',
                'Authorization': authorization
            }
            # Make request to gatekeeper and decode jwt token
            gatekeeper_request = requests.get(
                self.endpoint.gatekeeper('sessions/'),
                headers = headers
            )
            # Check if jwt decoding is sucessful
            if gatekeeper_request.status_code == 200:
                self.user = gatekeeper_request.json()['data']
                return True
            else:
                # Decoding Failed
                self.response =  make_response(jsonify({
                    'status_code': gatekeeper_request.status_code,
                    'status': "",
                    'message': "Jwt Middleware",
                    'error': {}
                }), gatekeeper_request.status_code)
                return False