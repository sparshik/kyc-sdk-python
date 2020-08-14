#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: challenge.py
Description: Challenge section of the Sparshik KYC API.
"""

from .utils import request


def create_challenge(applicant_id, document_id=None, user_request_id=None, delete_at=None):
	""" Creates a list of challenges for the user to tackle for verification purposes.

	Args:
		applicant_id : [Atleast one] document_id or applicant_id
		document_id : [Atleast one] document_id or applicant_id
		user_request_id : [Optional] user request id, supplied with response
		delete_at : [Optional] when to delete record, Ex, 14-07-2020

	Returns:
		applicant data from the database and returns HTTP status code
	"""
	url = "video/create_challenge/"
	files = None

	json = {'applicant_id': applicant_id, 'document_id': document_id,
			'user_request_id': user_request_id, 'delete_at': delete_at}

	# call internal abstract API function
	response = request('POST', url, files=files, json=json)
	return response
