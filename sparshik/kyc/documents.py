#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: documents.py
Description: Documents section of the Sparshik KYC API.
"""

from .utils import request


def parse_doc(file_path, attributes=None, doc_type=None, user_request_id=None, image_crops=None, delete_at=None,
			  image_url=None, data_uri=None):
	""" Identify or Parse KYC Documents such as Aadhaar, Pan, Passport and Voter ID.
	Args:
		file_path : Path to File or Image or Data URL
		attributes : [Optional] type to identify document type, mask to mask number in aadhaar. 
			Supported attribute include type,mask
		doc_type : [Optional] Supported doc-type include aadhaar, pan, or passport
		user_request_id : [Optional] user request id, supplied with response 
		image_crops : [Optional] image crops of original document. 
			Supported image_crops include front, front_top, front_bottom, back, qr_code, photo
		delete_at : [Optional] when to delete record, Ex, 14-07-2020
		image_url : [Optional] data_uri or image_url or file_path ( one of them is required)
		data_uri : [Optional] data_uri or image_url or file_path ( one of them is required)
	
	Returns:
		returns parsed information and HTTP status code.
	"""

	url = "documents/"

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	# create only one data field dict
	json = {'doc_type': doc_type, 'attributes': attributes, 'user_request_id': user_request_id,
			'image_crops': image_crops, 'delete_at': delete_at}

	if image_url:
		json["image_url"] = image_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, json=json)
	return response


def offline_aadhaar(file_path, share_code, user_request_id=None, image_url=None, data_uri=None):
	""" Verify Aadhaar offline with Share code.
	Args:
		file_path : Path to File or Image or Data URL
		share_code : 4 digit share code.
		user_request_id : [Optional] user request id, supplied with response
		image_url : [Optional] data_uri or image_url or file_path ( one of them is required)
		data_uri : [Optional] data_uri or image_url or file_path ( one of them is required)
	
	Returns:
		returns HTTP status code.
	"""

	url = "documents/offline"

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	# create only one data field dict
	json = {'share_code': share_code, 'user_request_id': user_request_id}

	if image_url:
		json["image_url"] = image_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, data=json)
	return response

