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

from .factory.user_factory import UserFactory, Session


class TestUserPersistence():

    def setup_class(self):
        # Prepeare a new, clean session
        self.session = Session()
        # init faker object
        self.faker = Faker()

    def test_creation(self):
        user = UserFactory()
        assert user.id != None

    def test_name_with_empty_string(self):
        with pytest.raises(ValueError):
            UserFactory(name = '')

    def test_name_with_invalid_charset(self):
        with pytest.raises(ValueError):
            UserFactory(name = '-' + self.faker.name())

    def test_email_with_empty_string(self):
        with pytest.raises(ValueError):
            UserFactory(email = '')

    #def test_email_with_invalid_charset(self):
        #with pytest.raises(ValueError):
            #UserFactory(email = '*' + self.faker.email())

    def test_email_with_out_at_sign(self):
        with pytest.raises(ValueError):
            UserFactory(email = self.faker.first_name())

    def test_pnum_with_less_charset_length(slef):
        with pytest.raises(ValueError):
            UserFactory(pnum = '1234567')

    