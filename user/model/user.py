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

import re

from user.database import db
from sqlalchemy.orm import validates

from .mixins.base_mixin import BaseMixin
from .mixins.user_mixin import UserMixin
from .mixins.timestamp_mixin import TimestampMixin


class User(db.Model, BaseMixin, UserMixin, TimestampMixin):
    """User ORM
    
    ...

    Attributes
    ----------
    __tablename__ : String
        Table Name

    name: String 
        User's full name, i.e first name and father name

    cell_phone_num : String(13)
        Example :
            - +251966751230
    """

    __tablename__ = 'user'

    __legal_characters = '^[a-zA-Z]+$'

    __phone_num_patterns = '^\+[0-9]+$'

    __name_pattern = '^[a-zA-Z]+\s[a-zA-Z]+\s?[a-zA-Z]*$'

    ACTIVE = True

    DEACTIVE = False

    name = db.Column(db.String(), nullable = False)

    email = db.Column(db.String(), unique = True, nullable = False)

    pnum = db.Column(db.String(13), unique = True, nullable = True)

    @validates('name')
    def validate_name(self, key, value):
        if not re.match(self.__name_pattern, value):
            raise ValueError('First Name cannot contain illegal characters VALUE => %s' % value)
        return value

    @validates('email')
    def validate_email(self, key, value):
        if not '@' in value or not value.strip():
            raise ValueError('Company Email Address must contain @ symbol or cannot be empty VALUE => %s' % value)
        else:
            return value

    @validates('pnum')
    def validate_phone_num(self, key, value):
        if not value.strip():
            return None
        elif not re.match(self.__phone_num_patterns, value) or len(value) != 13:
            raise ValueError('Phone Number cannot contain illegal characters, or must be 13 characters VALUE => %s' % value)
        else:
            return value
