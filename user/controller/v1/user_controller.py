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


"""REST namespace Controller

Responses List :
    1xx -> :            Informational response - The request was received, continuing process
        * 100           Continue
        * 101           Switching Protocols
        * 102           Processing
        * 103           Early Hints (RFC 8297)

    2xx -> :            Successful - The request was successfully received, understood, and accepted
        * 200           Ok
        * 201           Created
        * 202           Accepted
        * 203           Non-Authoritative Information
        * 204           No Content
        * 205           Reset Content
        * 206           Partial Content
        * 207           Multi-Status
        * 208           Already Reported
        * 226           IM Used

    3xx -> :            Redirection - Further action needs to be taken in order to complete the request
        * 300           Multiple Choices
        * 301           Moved Permanently
        * 302           Found (Previously "Moved temporarily")
        * 303           See Other
        * 304           Not Modified
        * 305           Use Proxy
        * 306           Switch Proxy
        * 307           Temporary Redirect
        * 308           Permanent Redirect

    4xx -> :            Client Error - The request contains bad syntax or cannot be fulfilled
        * 400           Bad  Request
        * 401           Unauthorized
        * 402           Payment Required
        * 403           Forbidden
        * 404           Not Found
        * 405           Method Not Allowed
        * 406           Not Acceptable
        * 407           Proxy Authentication Required
        * 408           Request Timeout
        * 409           Conflict
        * 410           Gone
        * 411           Length Required
        * 412           Precondition Failed
        * 413           Payload Too Large
        * 414           URI Too Long
        * 415           Unsupported Media Type
        * 416           Range Not Satisfiable
        * 417           Expection Failed
        * 418           I'm a teapot
        * 421           Misdirected Request
        * 422           Unprocessable Entity
        * 423           Locked
        * 424           Failed Dependency
        * 425           Too Early
        * 426           Upgrade Required
        * 428           Precondition Required
        * 429           Too Many Requests
        * 431           Request Header Fields Too Large
        * 451           Unavailable For Legal Reasons

    5xx -> :            Server Error - The server failed to fulfil an apparently valid request
        * 500           Internal Server Error
        * 501           Not Implemented
        * 502           Bad Gateway
        * 503           Service Unavaliable
        * 504           Gateway Timeout
        * 505           HTTP Version Not Supported
        * 506           Variant Also Negotiates
        * 507           Insufficent Storage
        * 508           Loop Detected
        * 510           Not Extended
        * 511           Network Authentication Required


Functions:
    * get - returns list of datas
    * post - returns creation status with the newly created resource link
    * put - return update status with the the newly updated resource link
    * patch - returns the semi updated status with the newly semi updated resource link
    * delete - return delation status

"""


from flask_restplus import Resource

from user.dto.user_dto import UserDto
from user.blueprint.v1.user import namespace


@namespace.route('')
@namespace.response(100, 'Continue')
@namespace.response(101, 'Switching Protocols')
@namespace.response(102, 'Processing')
@namespace.response(103, 'Early Hints (RFC 8297)')
@namespace.response(200, 'Ok')
@namespace.response(201, 'Created')
@namespace.response(202, 'Accepted')
@namespace.response(203, 'Non-Authoritative Information')
@namespace.response(204, 'No Content')
@namespace.response(205, 'Reset Content')
@namespace.response(206, 'Partial Content')
@namespace.response(207, 'Multi-Status')
@namespace.response(208, 'Already Reported')
@namespace.response(226, 'IM Used')
@namespace.response(300, 'Multiple Choices')
@namespace.response(301, 'Moved Permanently')
@namespace.response(302, 'Found (Previously "Moved temporarily")')
@namespace.response(303, 'See Other')
@namespace.response(304, 'Not Modified')
@namespace.response(305, 'Use Proxy')
@namespace.response(306, 'Switch Proxy')
@namespace.response(307, 'Temporary Redirect')
@namespace.response(308, 'Permanent Redirect')
@namespace.response(400, 'Bad  Request')
@namespace.response(401, 'Unauthorized')
@namespace.response(402, 'Payment Required')
@namespace.response(403, 'Forbidden')
@namespace.response(404, 'Not Found')
@namespace.response(405, 'Method Not Allowed')
@namespace.response(406, 'Not Acceptable')
@namespace.response(407, 'Proxy Authentication Required')
@namespace.response(408, 'Request Timeout')
@namespace.response(409, 'Conflict')
@namespace.response(410, 'Gone')
@namespace.response(411, 'Length Required')
@namespace.response(412, 'Precondition Failed')
@namespace.response(413, 'Payload Too Large')
@namespace.response(414, 'URI Too Long')
@namespace.response(415, 'Unsupported Media Type')
@namespace.response(416, 'Range Not Satisfiable')
@namespace.response(417, 'Expection Failed')
@namespace.response(418, 'I\'m a teapot')
@namespace.response(421, 'Misdirected Request')
@namespace.response(422, 'Unprocessable Entity ')
@namespace.response(423, 'Locked')
@namespace.response(424, 'Failed Dependency')
@namespace.response(425, 'Too Early')
@namespace.response(426, 'Upgrade Required')
@namespace.response(428, 'Precondition Required')
@namespace.response(429, 'Too Many Requests')
@namespace.response(431, 'Request Header Fields Too Large')
@namespace.response(451, 'Unavailable For Legal Reasons')
@namespace.response(500, 'Internal Server Error')
@namespace.response(501, 'Not Implemented')
@namespace.response(502, 'Bad Gateway')
@namespace.response(503, 'Service Unavaliable')
@namespace.response(504, 'Gateway Timeout')
@namespace.response(505, 'HTTP Version Not Supported')
@namespace.response(506, 'Variant Also Negotiates')
@namespace.response(507, 'Insufficent Storage')
@namespace.response(508, 'Loop Detected')
@namespace.response(510, 'Not Extended')
@namespace.response(511, 'Network Authentication Required')
class UsersResource(Resource):
    """Foobar Related Operation

    ...

    `asc'  +
    `desc` -


    Attributes
    ----------
    LIMIT : Integer
        Max allowed rows

    Methods
    -------
    get() :
        Get All/Semi datas from database

    post() :
        Save data/datas to database

    """

    def get(self):
        """Get All/Semi datas from database

        ...

        Query Examples:
            * Filtering :
                - name.en=eq:abc&name.am=neq:abc

        Returns
        -------
            Json Dictionaries

        """

        # Validate querys if existed
        # or set them to default value
        limit = int(request.args.get('limit', self._LIMIT))
        page = int(request.args.get('page', 1 ))
        offset = (page - 1) * limit
        # last_offset = (total_page -1) * limit
        # previous_offset = ((current_page - 1) - 1) * limit
        # next_offset = ((current_page + 1) - 1) * limit

        # Open database session
        # fetch everything
        # returns a Query object
        users =  db.session.query(Users)
        # applay filtering to Query object
        # Filtering short url names with their corsponding mathematical symbole:
        # eq   => equal to                 =>  `=`
        # ne   => not equal to             =>  `!=`
        # lt   => less than                =>  `<`
        # lte  => less than or equal to    =>  `<=`
        # gt   => greater than             =>  `>`
        # gte  => greater than or equal to =>  `>=`
        # not  => negate a standard check  =>  `neg`
        # in   => value is in the list (a list of values should be provided)
        # nln  => Value is not in the list (a list of values should be provided)
        # all  => every item in the list of values provided is in array
        filter_operators = {
            'eq'  :  '=',
            'ne'  :  '!=',
            'lt'  :  '<',
            'lte' :  '<=',
            'gt'  :  '>',
            'gte' :  '>='
        }
        # First step to get filter varables assoication type
        # key : value
        filters = {
            'name' : request.args.get('name'),
            'email' : request.args.get('email'),
            'pnum' : request.args.get('pnum')
        }
        # filter through the Query object and applay the filter
        for parent_key, parent_value in filters.items():
            if isinstance(parent_value, dict):
                for child_key, child_value in parent_value.items():
                    # check if Query value is set
                    if child_value:
                        # split the operation from the query value
                        splited = child_value.split(':')
                        # check if filter operation is correct
                        if splited[0] in filter_operators:
                            users = users.filter(
                                text(
                                    "(%s->> '%s') %s '%s'"
                                    % (parent_key, child_key, filter_operators[splited[0]], splited[1] )
                                )
                            )
            else:
                # check if value is null or note
                if parent_value:
                    #s plit the operation form the query value
                    splited = parent_value.split(':')
                    # check if filter operatior is correct
                    if splited[0] in filter_operators:
                        users = users.filter(
                            text(
                                "%s %s '%s'"
                                % (parent_key, child_key, filter_operators[splited[0]], splited[1] )
                            )
                        )
        # user results
        # split multiple order bys
        if request.args.get('order_by'):
            order_bys = request.args.get('order_by').split(',')
            for value in order_bys:
                if value:
                    splited = re.split('\+|-', value)
                    qs = 1
                    if value[0] == '+':
                        qs = '%s %s' % (splited[1], 'ASC')
                    elif value[0] == '-':
                        qs = '%s %s' % (splited[1], 'DESC')
                    #
                    users = users.order_by(
                        text(
                            str(qs)
                        )
                    )
        else:
            # if there is no order Query, order by updated_at
            users = users.order_by(
                Users.updated_at.desc()
            )


    @namespace.expect(UserDto.request, validate = True)
    def post(self):
        """Save data/datas to database

        ...

        Returns
        -------
            Json Dictionaries

        """
        # create new user
        # start by validating request fields for extra security
        # step 1 validation: strip payloads for empty string
        


@namespace.route('')
@namespace.response(100, 'Continue')
@namespace.response(101, 'Switching Protocols')
@namespace.response(102, 'Processing')
@namespace.response(103, 'Early Hints (RFC 8297)')
@namespace.response(200, 'Ok')
@namespace.response(201, 'Created')
@namespace.response(202, 'Accepted')
@namespace.response(203, 'Non-Authoritative Information')
@namespace.response(204, 'No Content')
@namespace.response(205, 'Reset Content')
@namespace.response(206, 'Partial Content')
@namespace.response(207, 'Multi-Status')
@namespace.response(208, 'Already Reported')
@namespace.response(226, 'IM Used')
@namespace.response(300, 'Multiple Choices')
@namespace.response(301, 'Moved Permanently')
@namespace.response(302, 'Found (Previously "Moved temporarily")')
@namespace.response(303, 'See Other')
@namespace.response(304, 'Not Modified')
@namespace.response(305, 'Use Proxy')
@namespace.response(306, 'Switch Proxy')
@namespace.response(307, 'Temporary Redirect')
@namespace.response(308, 'Permanent Redirect')
@namespace.response(400, 'Bad  Request')
@namespace.response(401, 'Unauthorized')
@namespace.response(402, 'Payment Required')
@namespace.response(403, 'Forbidden')
@namespace.response(404, 'Not Found')
@namespace.response(405, 'Method Not Allowed')
@namespace.response(406, 'Not Acceptable')
@namespace.response(407, 'Proxy Authentication Required')
@namespace.response(408, 'Request Timeout')
@namespace.response(409, 'Conflict')
@namespace.response(410, 'Gone')
@namespace.response(411, 'Length Required')
@namespace.response(412, 'Precondition Failed')
@namespace.response(413, 'Payload Too Large')
@namespace.response(414, 'URI Too Long')
@namespace.response(415, 'Unsupported Media Type')
@namespace.response(416, 'Range Not Satisfiable')
@namespace.response(417, 'Expection Failed')
@namespace.response(418, 'I\'m a teapot')
@namespace.response(421, 'Misdirected Request')
@namespace.response(422, 'Unprocessable Entity ')
@namespace.response(423, 'Locked')
@namespace.response(424, 'Failed Dependency')
@namespace.response(425, 'Too Early')
@namespace.response(426, 'Upgrade Required')
@namespace.response(428, 'Precondition Required')
@namespace.response(429, 'Too Many Requests')
@namespace.response(431, 'Request Header Fields Too Large')
@namespace.response(451, 'Unavailable For Legal Reasons')
@namespace.response(500, 'Internal Server Error')
@namespace.response(501, 'Not Implemented')
@namespace.response(502, 'Bad Gateway')
@namespace.response(503, 'Service Unavaliable')
@namespace.response(504, 'Gateway Timeout')
@namespace.response(505, 'HTTP Version Not Supported')
@namespace.response(506, 'Variant Also Negotiates')
@namespace.response(507, 'Insufficent Storage')
@namespace.response(508, 'Loop Detected')
@namespace.response(510, 'Not Extended')
@namespace.response(511, 'Network Authentication Required')
class UserResource(Resource):
    """"Single Foobar Related Operation

    ...

    Methods
    -------
    get(id:String) :
        Get a data from database

    put(id:String) :
        Update a data from database

    delete(id:String) :
        Delete a data from database

    """

    def get(self, id):
        """Get All/Semi datas from database

        ...

        Parameters
        ----------
        id : integer
            Object Id, i.e 12-byte, 24 char hexadicmal

        Returns
        -------
            Json Dictionaries

        """


    @namespace.expect(UserDto.request, validate = True)
    def put(self, id):
        """Update a data from database

        ...

        Parameters
        ----------
        id : String
            Object Id, i.e 12-byte, 24 char hexadicmal

        Returns
        -------
            Json Dictionaries

        """
