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
from user.model import Credential


class CredentialFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Credential
        # Use the not-so-global scoped_session
        # Warning: DO NOT USE common.Session()!
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    #user_id = factory.fuzzy.FuzzyInteger(1, 1000)

    identity = factory.Faker('email')

    password = factory.fuzzy.FuzzyText()