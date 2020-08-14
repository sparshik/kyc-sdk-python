#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: mask.py
Description: Mask section of the Sparshik KYC API.
"""

from .utils import request


def mask_aadhaar(file_path=None, image_url=None, data_uri=None):
	""" Mask aadhaar data.

	Args:
		file_path : [Optional] Path to File or Image or Data URL
		image_url : [Optional] data_uri or image_url or file_path ( one of them is required)
		data_uri : [Optional] data_uri or image_url or file_path ( one of them is required)

	Returns:
		masked data and returns HTTP status code
	"""
	url = "aadhaar/mask"
	json = {}

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	if image_url:
		json["image_url"] = image_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, json=json)
	return response
