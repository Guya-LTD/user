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

from .factory.permission_factory import PermissionFactory, Session

class TestPermissionPersistence():

    def setup_class(self):
        # Prepeare a new, clean session
        self.session = Session()
        # init faker object
        self.faker = Faker()

    def test_permission_creation(self):
        permission = PermissionFactory()
        assert permission.id != None

