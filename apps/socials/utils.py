import os
from datetime import datetime


# - - - - - - - - - - - - - - - - - UPLOAD PATHS - - - - - - - - - - - - -

def user_image_upload_path(instance, filename):
    return os.path.join('users/avatar/', datetime.now().date().strftime("%Y/%m/%d"), filename)


def user_company_image_upload_path(instance, filename):
    return os.path.join('users/avatar/', datetime.now().date().strftime("%Y/%m/%d"), filename)

