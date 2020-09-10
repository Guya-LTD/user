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

"""Marshmallow SQLAlchemy Serializer class."""


from user.marshmallow_serializer import ma


class CredentialSchema(ma.Schema):
    """Json serializer

    """

    class Meta:
        """ Serializable Fields

        """

        # Fileds to expose
        fields = [
            'identity',
            'blocked',
            'note',
            'credential'
            'created_at',
            'updated_at'
        ]