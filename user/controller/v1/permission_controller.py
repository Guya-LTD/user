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
        - Permission Service
    * Description
        - Permission Service for Guya
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

from flask import request, jsonify, make_response
from flask_restplus import Resource

from user.database import db
from user.dto.permission_dto import PermissionDto
from user.exception import ValueEmpty, DocumentDoesNotExist, InvalidPayload
from user.model.permission import Permission
from user.blueprint.v1.permission import namespace
from user.serializer.permission_serializer import PermissionSchema
from user.middleware.jwt_auth_middleware import JWTAuthMiddleWare

@namespace.route('')
class PermissionResource(Resource):
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

    _LIMIT = 10

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
        permissions =  db.session.query(Permission)
        #print(x.__dict__)
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
            'key' : request.args.get('key')
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
                            permissions = permissions.filter(
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
                        permissions = permissions.filter(
                            text(
                                "%s %s '%s'"
                                % (parent_key, filter_operators[splited[0]], splited[1] )
                            )
                        )
        # permissions results
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
                    permissions = permissions.order_by(
                        text(
                            str(qs)
                        )
                    )
        else:
            # if there is no order Query, order by updated_at
            permissions = permissions.order_by(
                Permission.updated_at.desc()
            )

        # applay limit to Query object
        permissions = permissions.offset(offset)
        # applay paging to Query object
        permissions = permissions.limit(limit)
        # Create multi-value schema support
        permissions_schema = PermissionSchema(many = True)
        # Serialized Query inorder to send it over network
        serialized_permissions = permissions_schema.dump(permissions)
        
        # Return must always include the global fileds :
        # Field           Datatype        Default         Description             Examples
        # -----           --------        -------         -----------             --------
        # code            int             201             1xx, 2xx, 3xx, 5xx
        # description     string          Created         http code description
        # messages        array           Null            any type of messages
        # errors          array           Null            occured errors
        # warnings        array           Null            can be url format
        # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
        return make_response(jsonify({
            'status_code': 200,
            'status': 'Ok',
            'data': serialized_permissions,
            "pagination": {
                "count": db.session.query(Permission).count(),
                "limit": limit,
                "page": page
            }
        }), 200)
        

    @namespace.expect(PermissionDto.request, validate = True)
    def post(self):
        """Save data/datas to database

        ...

        Returns
        -------
            Json Dictionaries

        """
        ## MiddleWare
        #jwtAuthMiddleWare = JWTAuthMiddleWare(request)
        #auth = jwtAuthMiddleWare.authorize() 
        # If auth is false break and return response to client
        # Else jwtAuthMiddleWare holds decoded users data
        #if not auth:
        #    return jwtAuthMiddleWare.response

        ## Start by validation request fields for extra security
        ## Step 1 validation: strip payloads for empty string
        if not namespace.payload['name'].strip() or \
           not namespace.payload['key'].strip():
           raise ValueEmpty({'payload': namespace.payload})

        name = namespace.payload['name']
        key = namespace.payload['key']
        if "create" in namespace.payload:
            create = namespace.payload['create']
        else:
            create = False
        if "read" in namespace.payload:
            read = namespace.payload['read']
        else:
            read = False
        if "update" in namespace.payload:
            update = namespace.payload['update']
        else:
            update = False
        if "delete" in namespace.payload:
            delete = namespace.payload["delete"] 
        else:
            delete = False

        ## Permission model
        permission = Permission(
            name = name,
            key = key,
            create = create,
            read = read,
            update = update,
            delete = delete,
            created_by = "-1" #jwtAuthMiddleWare.user.id
        )

        ## Create database session
        db.session.add(permission)
        ## Assign new id
        db.session.flush()
        ## Presist to the database
        db.session.commit()

        return make_response(jsonify({
            'status_code': 201,
            'status': 'Created'
        }), 201)


@namespace.route('/<string:id>')
class PermissionResource(Resource):
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
        ## Open database session
        permission = db.session.query(Permission).get(id)
        ## Create schema support
        permission_schema = PermissionSchema()
        ## Object serializer
        serialized_permission = permission_schema.dump(permission)
        ## Check if content found
        if not serialized_permission:
            ## No Content Found
            return make_response(jsonify({
                "status_code": 204,
                "status": "No Content",
                "payload": {"id": id}
            }))
        else:
            ## Content Found
            return make_response(jsonify({
                "status_code": 200,
                "status": "Ok",
                "data": serialized_permission
            }))

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
        ## MiddleWare
        jwtAuthMiddleWare = JWTAuthMiddleWare(request)
        auth = jwtAuthMiddleWare.authorize() 
        # If auth is false break and return response to client
        # Else jwtAuthMiddleWare holds decoded users data
        if not auth:
            return jwtAuthMiddleWare.response
            
        ## Start by validation request fields for extra security
        ## Step 1 validation: strip payloads for empty string
        if not namespace.payload['name'].strip() or \
           not namespace.payload['key'].strip():
           raise ValueEmpty({'payload': namespace.payload})

        name = namespace.payload['name']
        key = namespace.payload['key']
        if "create" in namespace.payload:
            create = namespace.payload['create']
        else:
            create = False
        if "read" in namespace.payload:
            read = namespace.payload['read']
        else:
            read = False
        if "update" in namespace.payload:
            update = namespace.payload['update']
        else:
            update = False
        if "delete" in namespace.payload:
            delete = namespace.payload["delete"] 
        else:
            delete = False
        
        ## Update a record
        permission = db.session.query(Permission).get(id)

        if not permission:
            ## No Data found return no content
            return make_response(jsonify({
                "status_code": 204,
                "status": "No Content",
                "payload": {"id": id}
            }))
        else:
            ## Content updated
            permission.name = name
            permission.key = key
            permission.create = create
            permission.read = read
            permission.update = update
            permission.delete = delete
            ## Presist to the database
            db.session.commit()
            return make_response(jsonify({
                "status_code": 200,
                "status": "Ok"
            }))