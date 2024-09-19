from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer
from rest_framework.response import Response
import requests

# Create your views here.

financial_products_api_key = settings.FINANCIAL_PRODUCTS_API_KEY

# 예금 상품 목록 저장
def save_deposits(request):
    url=f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={financial_products_api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 예금 상품 목록
    for li in response.get('result').get('baseList'):
        deposit_products = {
        'fin_prdt_cd' : li.get('fin_prdt_cd'),
        #  금융회사 명
        'kor_co_nm' : li.get('kor_co_nm'),
        # 금융 상품 명
        'fin_prdt_nm' : li.get('fin_prdt_nm'),
        # 기타 유의사항 (전체조회 시 출력 x, 상세 조회 시에만 출력)
        'etc_note' : li.get('etc_note'),
        # 가입 대상
        'join_member' : li.get('join_member'),
        # 가입 방법 (전체조회 시 출력 x, 상세 조회 시에만 출력)
        'join_way' : li.get('join_way'),
        #  우대조건 (전체조회 시 출력 x, 상세 조회 시에만 출력)
        'spcl_cnd' : li.get('spcl_cnd'),
        # option key를 만들고
        }
    
        serializer = DepositProductsSerializer(data=deposit_products)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        # deposit_options을 product.options.append를 할지? 
        deposit_options = {
        'fin_prdt_cd': fin_prdt_cd,
        # # 은행 이름
        # 'bank_name': product.kor_co_nm,
        # # 상품 이름
        # 'product_name': product.fin_prdt_nm,
        # 저축 기간
        'save_trm': li.get('save_trm'),
        # 저축 금리 유형명
        'intr_rate_type_nm': li.get('intr_rate_type_nm'),
        # 저축 금리
        'intr_rate': li.get('intr_rate'),
        # 최고 우대금리
        'intr_rate2': li.get('intr_rate2')
        }

        serializer = DepositOptionsSerializer(data=deposit_options)

        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)  

# 예금 상품 목록 조회
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def deposit_list(request):
    if request.method == 'GET':
        deposits = get_list_or_404(DepositProducts)
        # print(deposits)
        serializer = DepositProductsSerializer(deposits, many=True)
        return Response(serializer.data)
@api_view(['GET'])  
def deposit_option_list(request):
    if request.method == 'GET':
        deposits = get_list_or_404(DepositOptions)
        serializer = DepositOptionsSerializer(deposits, many=True)
        return Response(serializer.data)


# 적금 상품 목록 저장
def save_savings(request):
    url=f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={financial_products_api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 예금 상품 목록
    for li in response.get('result').get('baseList'):
        saving_products = {
        'fin_prdt_cd' : li.get('fin_prdt_cd'),
        #  금융회사 명
        'kor_co_nm' : li.get('kor_co_nm'),
        # 금융 상품 명
        'fin_prdt_nm' : li.get('fin_prdt_nm'),
        # 기타 유의사항 (전체조회 시 출력 x, 상세 조회 시에만 출력)
        'etc_note' : li.get('etc_note'),
        # 가입 대상
        'join_member' : li.get('join_member'),
        # 가입 방법 (전체조회 시 출력 x, 상세 조회 시에만 출력)
        'join_way' : li.get('join_way'),
        #  우대조건 (전체조회 시 출력 x, 상세 조회 시에만 출력)
        'spcl_cnd' : li.get('spcl_cnd'),
        # option key를 만들고
        }
    
        serializer = SavingProductsSerializer(data=saving_products)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        # saving_options을 product.options.append를 할지? 
        saving_options = {
        'fin_prdt_cd': fin_prdt_cd,
        # # 은행 이름
        # 'bank_name': product.kor_co_nm,
        # # 상품 이름
        # 'product_name': product.fin_prdt_nm,
        # 저축 기간
        'save_trm': li.get('save_trm'),
        # 저축 금리 유형명
        'intr_rate_type_nm': li.get('intr_rate_type_nm'),
        # 저축 금리
        'intr_rate': li.get('intr_rate'),
        # 최고 우대금리
        'intr_rate2': li.get('intr_rate2') 
        }

        serializer = SavingOptionsSerializer(data=saving_options)

        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)  



# 적금 상품 목록 조회
@api_view(['GET'])
def saving_list(request):
    if request.method == 'GET':
        savings = get_list_or_404(SavingProducts)
        # print(savings)
        serializer = SavingProductsSerializer(savings, many=True)
        return Response(serializer.data)


# 적금 상품 옵션 목록 조회
@api_view(['GET'])
def saving_option_list(request):
    if request.method == 'GET':
        savings = get_list_or_404(SavingOptions)
        # print(savings)
        serializer = SavingOptionsSerializer(savings, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_product_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        product1 = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)
        product2 = SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)
        if product1.exists():
            product = product1.first()
            serializer = DepositProductsSerializer(product)
            # print(serializer.data)
            return Response(serializer.data)
        elif product2.exists():
            product = product2.first()
            serializer = SavingProductsSerializer(product)
            # print(serializer.data)
            return Response(serializer.data)
        
        else:
            return Response({'error': 'Product not found'}, status=404)

@api_view(['PUT'])
def put_product(request):
    print(request.data)
    data = request.data['financial_products']
    if request.method == 'PUT':
        user = get_object_or_404(get_user_model(), username=request.user.username)
        financial_products = user.financial_products
        # print('상품목록:',financial_products)
        if financial_products == None:
            financial_products_list = [data]
            
        else:
            financial_products_list = financial_products.strip(',').split(',')
            # print('문자열을 리스트로 바꿈 : ', financial_products_list)
            # 이미 있는 값 -> 삭제 PUT
            if data in financial_products_list:
                financial_products_list.remove(data)
            else:
                financial_products_list.append(data)
        if financial_products_list == []:
            user.financial_products = None
        else:
            user.financial_products = ','.join(financial_products_list)
        print(user.financial_products)
        # user.financial_products = ','.join(financial_products_list)
        user.save()
        return Response(status=status.HTTP_201_CREATED)
        # print(type(user.financial_products))
    

deposits_product_list = list(DepositProducts.objects.values_list('fin_prdt_cd', flat=True))
savings_product_list = list(SavingProducts.objects.values_list('fin_prdt_cd', flat=True))
fin_prdt_list = deposits_product_list + savings_product_list
# print(fin_prdt_list)


def find_name(code):
    product1 = DepositProducts.objects.filter(fin_prdt_cd=code).first()
    product2 = SavingProducts.objects.filter(fin_prdt_cd=code).first()
    if product1:
        return product1.fin_prdt_nm
    elif product2:
        return product2.fin_prdt_nm

@api_view(['GET'])
def recommend_age(request):
    user = get_object_or_404(get_user_model(), username=request.user.username)
    # print(user)
    age = user.age

    users_age = get_user_model().objects.filter(age__gte=age-3, age__lte=age+3)
    
    age_recommend = {}

    for user in users_age:
        if user.financial_products != None:
            # print(user.financial_products.strip(',').split(','))
            financial_products_list = user.financial_products.strip(',').split(',')
            if financial_products_list != ['']:
                for financial_product in financial_products_list:
                    # print(type(financial_product))
                    if financial_product in fin_prdt_list:
                        if financial_product in age_recommend.keys():
                            age_recommend[financial_product] += 1
                        else:
                            age_recommend[financial_product] = 1

    # print(sorted(age_recommend.items(), key=lambda item: item[1], reverse=True)[:5])
    top_five_recommendations = dict(sorted(age_recommend.items(), key=lambda item: item[1], reverse=True)[:5])

    # return_dict = {}
    # for item in top_five_recommendations:
    #     code = item[0]
    #     cnt = item[1]
    #     return_dict[code] = [find_name[code], cnt]
    # print('hi',return_dict)
    # return Response(return_dict)
    return Response(top_five_recommendations)



@api_view(['GET'])
def recommend_money(request):
    user = get_object_or_404(get_user_model(), username=request.user.username)
    # print(user)
    # money가 뭘까요?
    money = user.money
    lower_bound = int(money * 0.95)
    upper_bound = int(money * 1.05)
    # users_money = get_user_model().objects.filter(money__gte=money-3, money__lte=money+3) 범위 수정하기

    users_money = get_user_model().objects.filter(money__gte=lower_bound, money__lte=upper_bound)
    
    money_recommend = {}

    for user in users_money:
        if user.financial_products != None:
            # print(user.financial_products.strip(',').split(','))
            financial_products_list = user.financial_products.strip(',').split(',')
            if financial_products_list != ['']:
                for financial_product in financial_products_list:
                    if financial_product in fin_prdt_list:
                        if financial_product in money_recommend.keys():
                            money_recommend[financial_product] += 1
                        else:
                            money_recommend[financial_product] = 1
                   
    top_five_recommendations = dict(sorted(money_recommend.items(), key=lambda item: item[1], reverse=True)[:5])
    # return_dict = {}
    # for item in top_five_recommendations:
    #     code = item[0]
    #     cnt = item[1]
    #     return_dict[code] = [find_name[code], cnt]
    # print('hi',return_dict)
    # return Response(return_dict)

    return Response(top_five_recommendations)
    


@api_view(['GET'])
def recommend_salary(request):
    user = get_object_or_404(get_user_model(), username=request.user.username)
    # print(user)
    salary = user.salary
    # 본인의 연봉 기준 -5% ~ +5%
    lower_bound = int(salary * 0.95)
    upper_bound = int(salary * 1.05)
    '''
    users_salary = get_user_model().objects.filter(salary__gte=salary-3, salary__lte=salary+3) 범위 수정하기
    '''
    users_salary = get_user_model().objects.filter(salary__gte=lower_bound, salary__lte=upper_bound)
    

    salary_recommend = {}

    for user in users_salary:
        if user.financial_products != None:
            # print(user.financial_products.strip(',').split(','))
            financial_products_list = user.financial_products.strip(',').split(',')
            if financial_products_list != ['']:
                for financial_product in financial_products_list:
                    # print(type(financial_product))
                    if financial_product in fin_prdt_list:
                        if financial_product in salary_recommend.keys():
                            salary_recommend[financial_product] += 1
                        else:
                            salary_recommend[financial_product] = 1
                    
    top_five_recommendations = dict(sorted(salary_recommend.items(), key=lambda item: item[1], reverse=True)[:5])
    # return_dict = {}
    # for item in top_five_recommendations:
    #     code = item[0]
    #     cnt = item[1]
    #     return_dict[code] = [find_name[code], cnt]
    # print('hi',return_dict)
    # return Response(return_dict)
    
    return Response(top_five_recommendations)



