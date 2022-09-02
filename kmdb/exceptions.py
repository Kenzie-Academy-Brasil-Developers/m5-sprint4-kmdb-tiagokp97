from rest_framework import status
from rest_framework.exceptions import APIException


class UniqueException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "This value need to be unique."
