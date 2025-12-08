from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date as d
import requests
import json
import os


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_horoscope(request):
    API_KEY = os.getenv('OPENROUTER_API_KEY')

    today = d.today()
    user = request.user
    birthday = user.date
    if not birthday:
        birthday = today

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "tngtech/deepseek-r1t2-chimera:free",
            "messages": [
                {
                    "role": "user",
                    "content":f"Generate a horoscope prediction for {today} for me if I was born {birthday}."
                              f"Output ONLY the prediction text. "
                              f"Do not include the date, or any introductory phrases."
                }
            ]
        })
    )
    if response.status_code == 200:
        data = response.json()
        horoscope_text = data['choices'][0]['message']['content']
        return Response({"horoscope": horoscope_text})
    else:
        return Response({"horoscope": "Stars are not talkative today, but you got this!"})