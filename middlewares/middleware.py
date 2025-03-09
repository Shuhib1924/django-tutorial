class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("init middleware once by runserver")

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response
