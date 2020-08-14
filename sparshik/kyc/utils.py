#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: utils.py
Description: Shared utilities for the Python SDK of the Sparshik KYC API.
"""
import os.path
import requests

DEFAULT_BASE_URL = os.environ.get('KYC_ENDPOINT', "https://api.kyc.sparshik.com")


class KYCException(Exception):
	"""Custom Exception for the python SDK of the Sparshik KYC API.
	Attributes:
		status_code: HTTP response status code.
		type: error type.
		message: error message string
	"""

	def __init__(self, status_code, type, message):
		super(KYCException, self).__init__()
		self.status_code = status_code
		self.type = type
		self.message = message

	def __str__(self):
		return ('Error when calling Sparshik KYC API:\n'
				'\tstatus_code: {}\n'
				'\ttype: {}\n'
				'\tmessage: {}\n').format(self.status_code, self.type, self.message)


class Key(object):
	"""Manage API Token Key."""

	@classmethod
	def set(cls, Token):
		"""Set the API Token Key."""
		cls.Token = Token

	@classmethod
	def get(cls):
		"""Get the API Token Key."""
		if not hasattr(cls, 'Token'):
			cls.Token = None
		return cls.Token


class BaseUrl(object):
	"""Manage Base URL Key."""

	@classmethod
	def set(cls, base_url):
		"""Set the Base URL."""
		if not base_url.endswith('/'):
			base_url += '/'
		cls.base_url = base_url

	@classmethod
	def get(cls):
		"""Get the Base URL."""
		if not hasattr(cls, 'base_url') or not cls.base_url:
			cls.base_url = DEFAULT_BASE_URL
		return cls.base_url


def request(method, url, files=None, json=None, data=None, headers=None):
	""" Interface for request.
	Args:
		method : Type of HTTP method - GET, POST, DEL or PUT
		url : url for different components
		files : File path or Image path or Data URL
		json : Dict including parameters required for API call

	Returns:
		returns HTTP status code.
	"""

	"""Universal interface for request."""

	# Make it possible to call only with short name (without BaseUrl).
	if not url.startswith('https://'):
		url = BaseUrl.get() + url

	# Setup the headers with default Content-Type and Subscription Key.
	headers = headers or {}
	headers['Authorization'] = "Token {}".format(Key.get())

	if files is not None and len(files.keys()) == 0:
		if data is not None:
			json = data
			data = None

	response = requests.request(method, data=data, json=json, url=url, files=files, headers=headers)

	# Handle result and raise custom exception when something wrong.

	if response.status_code not in [200, 201, 202, 204]:
		try:
			error_msg = response.json()["error"]
		except:
			raise KYCException(response.status_code, response.status_code, response.text)

		raise KYCException(response.status_code, error_msg["type"], error_msg["message"])

	# Prevent `response.json()` complains about empty response.
	if response.text:
		result = response.json()
	else:
		result = dict()

	return result
