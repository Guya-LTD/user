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

from user.database import db


from .mixins.base_mixin import BaseMixin
from .mixins.timestamp_mixin import TimestampMixin
from .mixins.user_mixin import UserMixin


class UserRoles(db.Model, BaseMixin, TimestampMixin, UserMixin):
    """Permission ORM

    ...

    Attributes
    ----------
    __tablename__ : String
        Table Name
    """

    __tablename__ = 'user_roles'

    user_id = db.Column(db.String(), nullable = False)

    role_id = db.Column(db.String(), nullable = False)

