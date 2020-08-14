# Sparshik KYC API: Python SDK & Sample

[![PyPi Version](https://img.shields.io/pypi/v/sparshik_kyc.svg)](https://pypi.org/project/sparshik_kyc/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/sparshik/kyc-sdk-python/blob/master/LICENSE.md)

## About
The Sparshik API is based on REST principles. It uses standard HTTP response codes and verbs, and token-based authentication. You should use a Content-Type: application/json header with all PUT and POST requests except when uploading documents or live photos. For these requests, use a Content-Type: multipart/form-data header.

Responses return JSON with a consistent structure.

You must make all your requests to the API over HTTPS, with Server Name Indication enabled. Any requests made over HTTP will fail. Text fields support UTF-8.

* [Learn about the Sparshik](https://www.sparshik.com/about/)

## Getting started

## Installation:

```
pip install sparshik-kyc
```

For Direct API Usage and Documentation, please refer :
* [Learn about the Sparshik KYC API](https://documenter.getpostman.com/view/11880132/T17CEqEE?version=latest#intro)


### Example

The example used below is used to create an applicant in the database.

```
import sparshik as sk

TOKEN="Your Authentication Token"
URL="https://api.kyc.sparshik.com/v3/"

sk.BaseUrl.set(URL)
sk.Key.set(TOKEN)

response = sk.applicants.create_applicant(first_name="FIRST NAME", last_name="LAST NAME", email="name.surname@domain.com, phone="+91123456789", dob="1997-03-03", file_path="test.jpg")

print("CREATE APPLICANT RESPONSE : ", "\n", response.json())
```

## Contributing

We welcome contributions. Feel free to file issues and pull requests on the repo and we'll address them as we can. 

You can reach out to us anytime with questions and suggestions using our communities below:
 - **Support questions:** [Support](support@sparshik.com)
 - **Github Issues:** [Issues](https://github.com/sparshik/kyc-sdk-python/issues)
