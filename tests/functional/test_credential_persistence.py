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

import pytest
from faker import Faker

from .factory.credential_factory import CredentialFactory, Session


class TestCredentialPersistences():

    def setup_class(self):
        # prepeare a new clean session
        self.session = Session()
        # init faker object
        self.faker = Faker()

    #def test_credential_creation(self):
        #credential = CredentialFactory()
        #assert credential.id != None