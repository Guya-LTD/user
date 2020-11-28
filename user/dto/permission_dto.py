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
        - User Service
    * Description
        - User Service for Guya
"""

from flask_restplus import Namespace, fields

from user.blueprint.v1.permission import namespace

class PermissionDto:
    """Request and Respons Data Transfer Object."""

    request = namespace.model('permission_request', {
        'name': fields.String(),
        'key': fields.String(),
        'create': fields.Boolean(),
        'read': fields.Boolean(),
        'update': fields.Boolean(),
        'delete': fields.Boolean()
    })