from enum import Enum

class ResponseSignal(Enum):

    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds limit"
    FILE_UPLOADED_SUCCESS= "File uploaded successfully"
    FILE_UPLOADED_FAILED= "File upload failed"
    FILE_VALIDATED_SUCCESS= "File validated successfully"