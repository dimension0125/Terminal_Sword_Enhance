from random import *
import os

status = '-'
per = [100,100,95,90,90,85,85,80,80,70,60,50,40,30,20,10,5]
gPerLevel = [100, 300, 1000, 1500, 2000, 2500, 4000, 6000, 9000, 15000, 27000, 50000, 120000, 170000, 250000, 500000, 1000000]
sPerLevel = [0, 50, 500, 1000, 3000, 10000, 50000, 100000, 170000, 270000, 450000, 900000, 2200000, 6000000, 100000000, 30000000, 676767676767]
gold = 1000000
level = 0
name = ['나뭇가지','나무 단검','나무로 된 조금 긴 검','쓸만한 나무 검','단단한 나무 검','돌 검','불타는 나무 검(손잡이도 탐)','얼음 검','양날 검','마력 검','형광 검','불타는 나무 쌍검(손잡이 안 탐)','불꽃 마검','마검 아포피스','공기 검','식칼','빵칼']
inventory = {'파괴 보호석':0,'주문서':0}
gStatus = '-'

########################### 프린트 함수 ############################
def out():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-'*50+f'\n|   [인벤토리]\n|   파괴 보호석: {inventory["파괴 보호석"]}\n|   확률 두배 주문서: {inventory["주문서"]}\n'+'-'*50)

  if status == '성공': print('|   강화 성공!')
  elif status == '2단 승급': print('|   강화 대성공! (검이 2단계 좋아졌습니다.)')
  elif status == '실패': print('|   강화 실패! (검이 파괴되었습니다.)')
  elif status == '보호석': print('|   보호석으로 검을 지켰습니다.')
  elif status == '판매됨': print('|   검을 판매했습니다.')

  print(f'|   [Lv. {level}]')
  print(f'|   {name[level]}\n|   다음 강화 성공 확률: {per[level+1]}%\n'+'-'*50)
  print(f'|   다음 강화 비용: {gPerLevel[level]}\n|   판매 가격: {sPerLevel[level]}')
  print(f'|   보유 골드: {gold:,}개\n'+'-'*50)
########################### 프린트 함수 ############################

while True:
  out()
  print('|   1. 강화하기\n|   2. 판매하기\n|   3. 상점\n|   4. 주문서로 강화하기\n'+'-'*50)
  if gStatus == '부족':
    print('|   골드가 부족합니다.\n'+'-'*50)
    gStatus = '-'

  ans = input('➜  숫자 입력: ')
  if ans == '1':
    if gold < gPerLevel[level]:
      gStatus = '부족'
      continue
    gold -= gPerLevel[level]
    if randint(1, 100) > per[level+1]:
      status = '실패'
      if inventory['파괴 보호석'] > 0:
        out()
        print('|   강화 실패! 검이 파괴될 위기입니다.')
        stoneAns = input('|   파괴 보호석을 사용하시겠습니까?(예/아니오): ')
        if stoneAns == '예':
          inventory['파괴 보호석'] -= 1
          status = '보호석'
        else:
          level = 0
      else:
        level = 0
    else:
      level += 1
      status = '성공'
      if randint(1, 100) <= 10 and level <= 15:
        level += 2
        status = '2단 승급'

  elif ans == '2':
    gold += sPerLevel[level]
    level = 0
    status = '판매됨'

  elif ans == '3':
    print('-'*50+f'\n| ⬇ 아이템 목록 ⬇')
    print('|   1. 파괴 보호석 × 1 (800,000 골드)\n|   2. 파괴 보호석 × 3 (2,000,000 골드)\n|   3. 확률 두배 주문서 × 1 (500,000 골드)\n|   4. 확률 두배 주문서 × 3 (1,200,000 골드)\n'+'-'*50)
    shopAns = input('➜  구매번호 입력: ')
    if shopAns == '1' and gold >= 800000:
      inventory['파괴 보호석'] += 1
      gold -= 800000
    elif shopAns == '2' and gold >= 2000000:
      inventory['파괴 보호석'] += 3
      gold -= 2000000
    elif shopAns == '3' and gold >= 500000:
      inventory['주문서'] += 1
      gold -= 500000
    elif shopAns == '4' and gold >= 1200000:
      inventory['주문서'] += 3
      gold -= 1200000
    else:
      gStatus = '부족'

  elif ans == '4':
    if gold < gPerLevel[level]:
      gStatus = '부족'
      continue
    if inventory['주문서'] > 0:
      gold -= gPerLevel[level]
      if randint(1, 100) > per[level+1]*2:
        status = '실패'
        inventory['주문서'] -= 1
        if inventory['파괴 보호석'] > 0:
          out()
          print('|   강화 실패! 검이 파괴될 위기입니다.')
          stoneAns = input('|   파괴 보호석을 사용하시겠습니까?(예/아니오): ')
          if stoneAns == '예':
            inventory['파괴 보호석'] -= 1
            status = '보호석'
          else:
            level = 0
        else:
          level = 0
      else:
        level += 1

        status = '성공'
        inventory['주문서'] -= 1
    else:
      status = '주문서 부족'
      continue