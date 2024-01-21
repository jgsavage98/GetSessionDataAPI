
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parse name-value pairs from the request
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        name = req_body.get('name')

    if name:
        # Return a predefined URL
        return func.HttpResponse(f"The URL for {name} is: http://example.com")
    else:
        return func.HttpResponse(
             "Please pass a name in the request body",
             status_code=400
        )
