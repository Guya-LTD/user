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
        - Catalog service for Guya microservices
    * Description
        - Catalog mangement service
"""


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style


Exception.
"""


from werkzeug.exceptions import HTTPException

class DocumentDoesNotExist(HTTPException):
    code = 204

    def __init__(self, description=None, response=None):
        desc = {
            'status_code': 204,
            'status': 'No Content',
            'message': 'Document not found from collection'
            }
        if description is not None:
            desc.update(description)
        super().__init__(description=desc, response=None)