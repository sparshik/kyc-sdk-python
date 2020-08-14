#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: reports.py
Description: Report section of the Sparshik KYC API.
"""

from .utils import request


def video_challenge(challenge_id, file_path, video_url=None, data_uri=None, user_request_id=None, intervals=None):
	""" Used to verify if video supplied by user has cleared challenges.

	Args:
		challenge_id : For ex, 63672fb8-c2bd-4160-aeed-7c2d5951f63b
		file_path : Path to File or Image or Data URL
		video_url : [Optional] data_uri or video_url or file_path ( one of them is required)
		data_uri : [Optional] data_uri or video_url or file_path ( one of them is required)
		user_request_id : [Optional] user request id, supplied with response
		intervals : [Optional] intervals in seconds that contains durations of challenge sections. 
			In example, first challenge runs from 0-5 seconds, second challenge from 5-10 seconds.

	Returns:
		video verification results and returns HTTP status code
	"""
	url = "reports/video_challenge"

	json = {'challenge_id': challenge_id, 'intervals': intervals, 'user_request_id': user_request_id}

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	if video_url:
		json["video_url"] = video_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, data=json)
	return response


def document_face_similarity(document_id, file_path, data_uri=None, image_url=None, user_request_id=None):
	""" Compare face from an image against face from document stored in database.

	Args:
		document_id : For ex, 46d82a45-e8ff-474f-98dd-489f2ecdd683
		file_path : [Optional] data_uri or image_url or file_path
		data_uri : [Optional] data_uri or image_url or file_path ( one of them is required)
		image_url : [Optional] data_uri or image_url or file_path ( one of them is required)
		user_request_id : [Optional] user request id, supplied with response
		
	Returns:
		document and face verification results and returns HTTP status code
	"""
	url = "reports/facial_similarity_photo/document/"

	json = {'document_id': document_id, 'user_request_id': user_request_id}

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	if image_url:
		json["image_url"] = image_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, data=json)
	return response


def image_similarity(file_path_1=None, data_uri_1=None, image_url_1=None, 
	file_path_2=None, data_uri_2=None, image_url_2=None, user_request_id=None):
	""" Compare two faces from file_path or data_uri or image_url.

	Args:
		file_path_1 : [Optional] Path to File or Image or Data URL
		data_uri_1 : [Optional] data_uri or image_url or file_path ( one of them is required)
		image_url_1 : [Optional] data_uri or image_url or file_path ( one of them is required)
		file_path_2 : [Optional] Path to File or Image or Data URL
		data_uri_2 : [Optional] data_uri or image_url or file_path ( one of them is required)
		image_url_2 : [Optional] data_uri or image_url or file_path ( one of them is required)
		user_request_id : [Optional] user request id, supplied with response
		
	Returns:
		face verification results and returns HTTP status code
	"""
	url = "reports/facial_similarity_photo/"

	json = {'user_request_id': user_request_id}

	if file_path_1 and file_path_2:
		files = {'file_path_1': open(file_path_1, 'rb') , 'file_path_2':open(file_path_2, 'rb')}
	else:
		files = {}

	if image_url_1 or image_url_2:
		json["image_url_1"] = image_url_1
		json["image_url_2"] = image_url_2
	elif data_uri_1 or data_uri_2:
		json["data_uri_1"] = data_uri_1
		json["data_uri_2"] = data_uri_2

	# call internal abstract API function
	response = request('POST', url, files=files, data=json)
	return response


def face_attributes(attributes, file_path=None, data_uri=None, image_url=None):
	""" Generate a report on specified attributes in faces.

	Args:
		attributes : specify which face attributes to receive.
			For ex, age,gender, smoker, alcohol,bmi, ethnicity, resident, 
			region, marital, education
		file_path : [Optional] data_uri or image_url or file_path ( one of them is required)
		data_uri : [Optional] data_uri or image_url or file_path ( one of them is required)
		image_url : [Optional] data_uri or image_url or file_path ( one of them is required)
		
	Returns:
		face attributes results and returns HTTP status code
	"""
	url = "reports/face_attributes"

	json = {"attributes": attributes}

	if file_path:
		files = {'file_path': open(file_path, 'rb')}
	else:
		files = {}

	if image_url:
		json["image_url"] = image_url
	elif data_uri:
		json["data_uri"] = data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, data=json)
	return response


def video_image_similarity(video_file_path=None, video_data_uri=None, video_url=None, 
	image_file_path=None, image_data_uri=None, image_url=None, user_request_id=None, 
	interval=None):
	""" Compare face from a video and image.
	Args:
		video_file_path : [Optional] video_file_path or video_data_uri or video_url ( one of them is required)
		video_data_uri : [Optional] video_file_path or video_data_uri or video_url ( one of them is required)
		video_url : [Optional] video_file_path or video_data_uri or video_url ( one of them is required)
		image_file_path : [Optional] data_uri or image_url or file_path ( one of them is required)
		image_data_uri : [Optional] data_uri or image_url or file_path ( one of them is required)
		image_url : [Optional] data_uri or image_url or file_path ( one of them is required)
		user_request_id : [Optional] user request id, supplied with response
		interval : [Optional] interval in seconds that contains durations of challenge sections. 
			In example, first challenge runs from 0-5 seconds, second challenge from 5-10 seconds.
		
	Returns:
		comparison results from video and face with HTTP status code
	"""
	url = "reports/verify_face_similarity/"

	json = {'interval': interval , 'user_request_id': user_request_id}

	if video_file_path and image_file_path:
		files = {'video_file_path': open(video_file_path, 'rb'), 'image_file_path': open(image_file_path, 'rb')}
	else:
		files = {}

	if video_url or image_url:
		json["image_url"] = image_url
		json["video_url"] = video_url

	elif video_data_uri or image_data_uri:
		json["video_data_uri"] = video_data_uri
		json["image_data_uri"] = image_data_uri

	# call internal abstract API function
	response = request('POST', url, files=files, json=None)
	return response


def applicant_document_comparison(applicant_id, document_id, user_request_id=None):
	""" Can directly compare data filled in by applicant and document in database.

	Args:
		applicant_id : For ex, 3898cd8c-54ef-4b19-a5fd-2f0b8581c72c
		document_id : For ex, 46d82a45-e8ff-474f-98dd-489f2ecdd683
		user_request_id : [Optional] user request id, supplied with response
		
	Returns:
		applicant and document verification results and returns HTTP status code
	"""
	
	url = "reports/compare_applicant_document"
	files = None
	json = {'applicant_id': applicant_id , 'document_id': document_id, 'user_request_id': user_request_id}

	# call internal abstract API function
	response = request('POST', url, files=files, json=json)
	return response
