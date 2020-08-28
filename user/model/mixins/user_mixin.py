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

"""Mixins Meta Model,Genearal behaviour models."""

"""Mixins Meta Model, Genearal behaviour models."""


from user.database import db


class UserMixin(object):
    """Time Stamped Mixin

    Attributes
    ----------
    created_by : Integer
        Users/Admins Unique Identifier

    updated_by : Integer
        Users/Admins Unique Identifier

    """

    created_by = db.Column(db.Integer, nullable = False)


    updated_by = db.Column(db.Integer, nullable = True)