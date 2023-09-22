import random

while(1):
    print("========================================================================")
    print("1. 배수의 합계")
    print("2. 구구단 출력")
    print("3. 숫자 맞추기 게임")
    print("4. 종료")
    number = int(input("작업번호 입력=>"))
    if (number == 1):
        start = int(input("시작 값을 입력하세요:"))
        end = int(input("끝 값을 입력하세요:"))
        baesu = int(input("배수를 입력하세요:"))
        sum = 0

        for i in range(start, end+1):
            if i % baesu == 0:
                sum = sum + i

        print(str(start)+" 에서 "+str(end)+" 까지 "+str(baesu)+" 의 배수의 합은 "+str(sum)+" 입니다.")

    elif (number == 2):
        i=1
        while(i<10):
            j=2
            while(j<10):
                print(str(j)+"X"+str(i)+"="+str(i*j), end='\t')
                j = j+1
            print()    
            i = i+1


    elif (number == 3):
        num = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
        print("정답:", num)
        strike = 0
        trycount = 0
    
        while(strike<3):
            strike = 0
            ball = 0
            input_num = []
            for i in range(3):
                num = int(input(str(i+1)+"번째 수 입력=>"))
                input_num.append(num)
            trycount += 1
            print(str(input_num))

            for j in range(0, 3):
                for k in range(0, 3):
                    if(num[j] == input_num[k] and j == k):
                        strike = strike + 1
                    elif(num[j] == input_num[k] and j != k):
                        ball = strike + 1              
            print(str(strike)+" 스트라이크 "+str(ball)+" 볼")
            
        print(str(trycount)+"번 만에 맞추었습니다.")
        
    elif (number == 4):
        print("프로그램을 종료합니다...")
        print("Bye Bye~")
        print("========================================================================")
        exit()

    else:
        print("숫자를 잘못 입력했습니다. 다시 입력하세요.")

        