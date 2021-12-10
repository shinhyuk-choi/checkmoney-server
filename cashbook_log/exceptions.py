from rest_framework.exceptions import APIException


class DeletedLogException(APIException):
    status_code = 400
    default_detail = "Restore First"