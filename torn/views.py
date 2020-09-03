from ussd.core import  UssdRequest,UssdEngine
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json



@csrf_exempt
def post(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    phoneNumber=body['phoneNumber']
    sessionId=body['sessionId']
    serviceCode=body['serviceCode']
    text=body['text']

    ussd_request=UssdRequest(sessionId,
                                phoneNumber,
                                text,
                                'en',
                                journey_name="myownscreen",
                                         journey_version=None)

    ussd_engine=UssdEngine(ussd_request)

    ussd_response=ussd_engine.ussd_dispatcher()
    ussd_response_text=ussd_response.dumps()
    if ussd_response.status:
        http_text = 'CON' + ' ' + ussd_response_text
        phoneresponse = HttpResponse(http_text)
    else:
        http_text = 'END' + ' ' + ussd_response_text
        phoneresponse = HttpResponse(http_text)
    return phoneresponse

