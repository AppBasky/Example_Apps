from blog.settings import APP_NAME


def general_information(request):
    return {
        'APP_NAME': APP_NAME
    }