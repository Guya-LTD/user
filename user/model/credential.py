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


class Credentials(db.Modle, BaseMixin, TimestampMixin):
    """Credentials ORM

    ...

    Attributes
    ----------
    __tablename__ : String
        Table Name

    user_id : Integer

    email : String

    password : String

    blocked : Boolean

    note : Text

    """

    __tablename__ = 'credentials'


    user_id = db.Column(db.Integer(), unique = True, nullable = False)


    password = db.Column(db.String(), unique = False, nullable = True)


    blocked = db.Column(db.Boolean())


    note = db.Column(db.Text(), nullable = True)
