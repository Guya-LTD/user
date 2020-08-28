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

import factory
import factory.fuzzy

from .postgres_engine import Session
from user.model.user import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = User
        # Use the not-so-global scoped_session
        # Warning: DO NOT USE common.Session()!
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker('name')

    email = factory.Faker('email')

    pnum = factory.fuzzy.FuzzyText(length = 9, prefix = '+251', chars = '0123456789')
