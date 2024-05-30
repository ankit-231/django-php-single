from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Custom request processing logic here
        # print("CustomMiddleware: process_request")
        # Add a custom header to the request
        request.META['CUSTOM_HEADER'] = 'CustomHeaderValue'
        return None

    def process_response(self, request, response):
        # Custom response processing logic here
        # print("CustomMiddleware: process_response")
        # Add a custom header to the response
        response['Custom-Header'] = 'CustomHeaderValue'
        return response

    def process_exception(self, request, exception):
        # Handle exceptions
        print(f"Exception occurred: {exception}")
        # Return an HttpResponse if you want to handle the exception
        return None