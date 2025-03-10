from django.http import HttpResponse


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

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("call process_view")
        print(f"request.method - {request.method}")
        print(f"request.path - {request.path}")
        print(f"view_func.__name__  -.{view_func.__name__}")
        print(f"view_func.__module__  -.{view_func.__module__}")
        print(f"view_args - {view_args}")
        print(f"view_kwargs - {view_kwargs}")
        return None

    def process_exception(self, request, exception):
        print("call process_exception")
        print(exception)
        return None
        # return HttpResponse("response from prcoess_exception")

    def process_template_response(self, request, response):
        print("call process_template_response")
        response.context_data["process_context"] = "context from template_response"
        response.context_data["content"] = "content from middleware"
        return response
