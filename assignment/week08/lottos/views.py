from django.shortcuts import render
import random

# Create your views here.

# Basic Mission
def lotto(request):
    lotto_number = list()
    for _ in range(7):
        lotto_number.append(random.randint(1, 45))
        
    return render(request, 'lotto.html', {'lotto_number' : lotto_number})

# Challenge Mission
def lotto_index(request): # 입력창 함수
    return render(request, 'lotto_index.html')

def lotto_result(request): # 출력창 함수
    lotto_number = list()
    game = request.GET.get('game', 1) # html의 값인 game 변수 값이 없으면 1
    pull_number = [index for index in range(1, 46)] # list compression
    
    for _ in range(int(game)): # game 수만큼
        lotto_number.append(random.sample(pull_number, 6)) # sample 함수는 pull_number에서 6개 숫자를 뽑음
        
    return render(request, 'lotto_result.html', {'lotto_number': lotto_number, 'game' : game})