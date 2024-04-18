#
#	OAuth.py
#
#	(c) 2021 by Andreas Kraft
#	License: BSD 3-Clause License. See the LICENSE file for further details.
#
#	This module implements OAuth token retrieval.
#

from __future__ import annotations
import collections, time
import requests

Token = collections.namedtuple('Token', 'token expiration')
_expirationLeeway:float	= 5.0		# 5 seconds leeway for token expiration


def getOAuthToken(serverURL:str, clientID:str, clientSecret:str, token:Token=None, kind:str='keycloak') -> Token|None:
	"""	Retrieve and return a oauth2 token. If there is a provided token that is still valid, then that token
		is returned.

		This function returns a new named tuple Token(token, expiration), or None in case of an error. The expiration 
		is in epoch seconds.
	"""
	if not token:
		token = Token(token=None, expiration=0.0)

	# Return the old token, if it exists and is not expired
	if token.expiration > time.time() and token.token:
		return token

	# Retrieve a new token
	if kind == 'keycloak':
		headers = {
			'contentType' 	: 'application/x-www-form-urlencoded',
		}
		formData = {
			'grant_type' 	: 'client_credentials',
			'client_secret'	: clientSecret,
			'client_id'		: clientID,
		}
		try:
			if (response := requests.post(serverURL, data=formData, headers=headers)).status_code == 200:
				data = response.json()
				if not data or 'access_token' not in data or 'expires_in' not in data:
					return None
			return	Token(token	= data['access_token'],
						expiration = time.time() + data['expires_in'] - _expirationLeeway
					)
		except Exception as e:
			pass
	return None