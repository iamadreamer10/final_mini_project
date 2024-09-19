from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
        # url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={exchange_rates_api_key}&searchdate=20231122&data=AP01'

import requests

from datetime import datetime

# 현재 날짜를 YYYYMMDD 형식의 문자열로 가져오기
current_date = datetime.now().strftime("%Y%m%d")
exchange_rates_api_key = settings.EXCHANGE_RATES_API_KEY

@api_view(['GET'])
def exchange_rates(request):
    if request.method == 'GET':
        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={exchange_rates_api_key}&searchdate={current_date}&data=AP01'

        response = requests.get(url).json()

        exchange_rates = []

        # unit(외국단위)당 bkpr원
        for obj in response:
            if '100' in obj['cur_unit']:
                # 단위가 1단위 -> 1 / 100단위 -> 100
                unit = 100
                
            else:
                unit = 1
            bkpr = obj['bkpr'].replace(',', '')
            # print(bkpr)
            cur_nm = obj['cur_nm']
            cur_unit = obj['cur_unit']
            cur_info = f'{cur_nm}({cur_unit})'
            exchange_rate = {
                'cur_info': cur_info,
                'unit' : unit,
                'bkpr' : int(bkpr),
            }
            print(exchange_rate)
            exchange_rates.append(exchange_rate)
        
        return Response(exchange_rates)