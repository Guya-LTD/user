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


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style


This module provides means to perform operations on the database.
"""

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# global vars
db = SQLAlchemy()

migrate = Migrate()

def init(app: Flask) -> None:
    """This function initialize the datase ORM/ODM, providing a session
    and command line to create the tables/document in the database.

    Parameters:
    ----------    
        app (flask.app.Flask): The application instance.
    """
    
    db.init_app(app)

    migrate.init_app(app, db)

    import user.model
    
    db.create_all()