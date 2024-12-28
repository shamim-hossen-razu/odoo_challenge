# -*- coding: utf-8 -*-
from odoo import api, http, modules
from odoo.http import request
import jwt
import datetime


class CustomAuth(http.Controller):
    @http.route('/web/api/signin', type='json', auth="none", csrf=False, website=False, cors='*', methods=['POST'])
    def signin(self, **kw):
        try:
            # Attempt to authenticate the user
            user_id = request.session.authenticate("odoo-16-ee", request.params['login'],
                                                   request.params['password'])

            if not user_id:
                return {'success': False, 'message': 'Authentication failed: Invalid login or password.'}

            # Create JWT token
            payload = {
                'user_id': user_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=240)  # Token expiration time
            }
            secret_key = 'your_secret_key'  # Replace with your actual secret key
            token = jwt.encode(payload, secret_key, algorithm='HS256')

            return {
                'success': True,
                'message': 'Sign in successful!',
                'id': user_id,
                'result': {
                    'token': token
                }
            }

        except Exception as e:
            # In case of an error, return a message
            return {'success': False, 'message': str(e)}






