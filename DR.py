import random,math

def buffons_needle(num_trials, L, b, d):
    hits = 0  # 바늘이 격자선에 닿은 횟수
    howmanydlines = int(b/d)+1

    for _ in range(num_trials):
        # 바늘의 중심 좌표를 무작위로 설정 (x축, y축 격자 사이)
        center_y = random.uniform(0, b)
        
        # 바늘의 각도를 무작위로 설정 (0부터 π까지)
        angle = random.uniform(0,math.pi)
        
        # 바늘의 끝점들
        delta_x = (L/2) * math.sin(angle)
        delta_y = (L/2) * math.cos(angle)
        
        for i in range(0,howmanydlines+1):
            if center_y-L*math.sin(angle)/2 <= i*d <= center_y+L*math.sin(angle)/2:
                hits += 1
    
    # 원주율 근사값 계산 (x축 간격 a와 y축 간격 b를 모두 고려)
    pi_approx = (2*L*num_trials) / (d*hits)
    return pi_approx

def main():
    # 사용자로부터 입력 받기
    num_trials = int(input("실험 횟수를 입력하세요: "))
    L = float(input("선분의 길이 L을 입력하세요: "))
    b = 100 # float(input("y값의 범위 b를 입력하세요: "))
    d = float(input("격자 사이의 간격 d를 입력하세요(L값 이상,10 이하): "))
    
    # 원주율 근사값 계산
    pi_approx = buffons_needle(num_trials, L, b, d)
    
    # 결과 출력
    print("원주율의 근사값:{0}".format(pi_approx))

if __name__ == "__main__":
    main()
    