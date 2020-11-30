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


"""This module registers the error handler on the application."""


from flask import jsonify
from sqlalchemy import exc
from werkzeug.exceptions import HTTPException, default_exceptions


from .log import log_exception

def register_handler(app):
    """Registers the error handler is a function to common error HTTP codes

    Parameters:
    ----------
        app (flask.app.Flask): The application instance.
    """

    ################################################################
    #                                                              #
    # generic error handlers                                       #
    #                                                              #
    ################################################################
    
    def generic_http_error_handler(error):
        """Deal with HTTP exceptions.

        Parameters:
        ----------
            error (HTTPException): A werkzeug.exceptions.BadRequest exception object.

        Returns:
        -------
            A flask response object.
        """
        if isinstance(error, HTTPException):
            result = {
                'status_code': error.code, 
                'status': '',
                'message': error.description, 
                'type': 'HTTPException',
                'error': str(error.update({'type': 'HTTPException'}))}
        else:
            result = {
                'status_code': 500,
                'status': 'Internal Server Error',
                'message': error.description,
                'error': str(error.update({'type': 'Other Exceptions'}))}

        logger.exception(str(error), extra=result.update(EXTRA))
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp


    # sqlaclhemy generic error handler
    def generic_sqlalchemy_error_handler(error):
        """Deal with mongoengine exceptions.

        Parameters:
        ----------
            error (r.RedisError): Core exceptions raised by the Redis client.

            code int: An HTTP status code.

        Returns:
        -------
            A flask response object.
        """
        from .database import db

        # Rollback on session on exception
        db.session.rollback()

        custome_error = {
            'type': 'SQLAlchemyError',
            'message': str(error)
        }

        # formatting the exception
        result = {
            'status_code': 500, 
            'status': 'Internal Server Error', 
            'extra_message': 'Sqlalchemy Error',
            'error': custome_error
        }

        # logg exception
        log_exception(error = error, extra = result)
        resp = jsonify(result)
        resp.status_code = 500
        return resp

    ################################################################
    #                                                              #
    # register exception handlers to flask                         #
    #                                                              #
    ################################################################

    # register http code errors
    for code in default_exceptions.keys():
        app.register_error_handler(code, generic_http_error_handler)


    #
    app.register_error_handler(exc.SQLAlchemyError, generic_sqlalchemy_error_handler)