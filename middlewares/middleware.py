class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("init middleware once by runserver")

    def __call__(self, request):
        print("Before view")
        # if request.path == "/middlewares/":
        #     print(f"middleware block - {request.path}")
        if "middle" or "ware" in request.path:
            print(f"middleware block - {request.path}")
        response = self.get_response(request)
        print("After view")
        return response
