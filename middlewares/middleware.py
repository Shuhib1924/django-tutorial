def CustomMiddleware(get_response):
    print("init middleware by runserver")

    def middleware(request):
        print("Before view")
        response = get_response(request)
        print("After view")
        return response

    return middleware
