#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: applicants.py
Description: Applicants section of the Sparshik KYC API.
"""

from .utils import request


def create_applicant(first_name, file_path=None, last_name=None, email=None, phone=None, dob=None, id_numbers=None,
					 addresses=None, user_request_id=None, image_url=None, data_uri=None):
	""" Create an applicant in the database.
	Args:
		first_name : Firstname of the applicant
		file_path : [Optional] data_uri or image_url or file_path
		last_name : [Optional] Surname of the applicant
		email : [Optional] Name.Surname@domain.com
		phone : [Optional] +911234567890
		dob : [Optional] 1995-04-29
		id_numbers : [Optional] can store aadhaar, pan, passport 
		addresses : [Optional] can store flat_number, building_number, building_name, street, sub_street, city, state, 
			postcode, line, line1, line2, line3 (optional)
		user_request_id : [Optional] user request id, supplied with response
		image_url : [Optional] data_uri or image_url or file_path
		data_uri : [Optional] data_uri or image_url or file_path

	Returns:
		create applicant in the database and returns HTTP status code
	"""
	url = "applicants/"

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	# create only one data field dict
	json = {'first_name': first_name, 'last_name': last_name, 'email': email,
			'phone': phone, 'dob': dob, 'id_numbers': id_numbers, 'addresses': addresses,
			'user_request_id': user_request_id}

	if image_url:
		json["image_url"] = image_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, data=json)
	return response


def get_applicant(applicant_id=None):
	""" Get applicant data given an applicant id OR Get all applicant data if applicant id is not provided.
	Args:
		applicant_id : [Optional] if given, will return data for that applicant. 
			If not given, will return data of all applicants related to user.
			For ex, 3898cd8c-54ef-4b19-a5fd-2f0b8581c72c

	Returns:
		applicant data from the database and returns HTTP status code
	"""
	url = "applicants/"
	json = {'applicant_id': applicant_id}
	files = None

	# call internal abstract API function
	response = request('GET', url, files=files, json=json)
	return response


def delete_applicant(applicant_id):
	""" Delete an applicant from the database.

	Args:
		applicant_id : if given, will delete data for that applicant. 
			For ex, 3898cd8c-54ef-4b19-a5fd-2f0b8581c72c

	Returns:
		returns HTTP status code
	"""
	url = "applicants/"
	json = {'applicant_id': applicant_id}
	files = None

	# call internal abstract API function
	response = request('DELETE', url, files=files, json=json)
	return response


def modify_applicant(applicant_id, first_name, file_path=None, last_name=None, email=None, phone=None, dob=None,
					 id_numbers=None, addresses=None, user_request_id=None, image_url=None, data_uri=None):
	""" Modify an applicant from the database.

	Args:
		applicant_id : if given, will delete data for that applicant. 
			For ex, 3898cd8c-54ef-4b19-a5fd-2f0b8581c72c
		first_name : Firstname of the applicant
		file_path : [Optional] data_uri or image_url or file_path
		last_name : [Optional] Surname of the applicant
		email : [Optional] Name.Surname@domain.com
		phone : [Optional] +911234567890
		dob : [Optional] 1995-04-29
		id_numbers : [Optional] can store aadhaar, pan, passport 
		addresses : [Optional] can store flat_number, building_number, building_name, street, sub_street, city, state, 
			postcode, line, line1, line2, line3 (optional)
		user_request_id : [Optional] user request id, supplied with response
		image_url : [Optional] data_uri or image_url or file_path
		data_uri : [Optional] data_uri or image_url or file_path

	Returns:
		returns HTTP status code
	"""
	url = "applicants/"

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	# create only one data field dict
	json = {'applicant_id': applicant_id, 'first_name': first_name, 'last_name': last_name, 'email': email,
			'phone': phone, 'dob': dob, 'id_numbers': id_numbers, 'addresses': addresses,
			'user_request_id': user_request_id}

	if image_url:
		json["image_url"] = image_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('PUT', url, files=files, data=json, json=json)
	return response

