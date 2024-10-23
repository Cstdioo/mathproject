import random,math

def buffons_needle(num_trials, L, a, b):
    hits = 0  # 바늘이 격자선에 닿은 횟수

    for _ in range(num_trials):
        # 바늘의 중심 좌표를 무작위로 설정 (x축, y축 격자 사이)
        center_x = random.uniform(0, a / 2)
        center_y = random.uniform(0, b / 2)
        
        # 바늘의 각도를 무작위로 설정 (0부터 π까지)
        angle = random.uniform(0, math.pi)
        
        # 바늘의 끝점이 x축 격자선에 닿는지 확인
        delta_x = (L / 2) * math.sin(angle)
        delta_y = (L / 2) * math.cos(angle)
        
        # x축 및 y축에 닿았는지 계산
        if center_x <= delta_x or center_y <= delta_y:
            hits += 1  # 닿으면 hits 증가
    
    # 원주율 근사값 계산 (x축 간격 a와 y축 간격 b를 모두 고려)
    pi_approx = (2 * L * num_trials) / (hits * (a + b))
    return pi_approx

def main():
    # 사용자로부터 입력 받기
    num_trials = int(input("실험 횟수를 입력하세요: "))
    L = float(input("선분의 길이 L을 입력하세요: "))
    a = float(input("x축 사이의 간격 a를 입력하세요: "))
    b = float(input("y축 사이의 간격 b를 입력하세요: "))
    
    # 원주율 근사값 계산
    pi_approx = buffons_needle(num_trials, L, a, b)
    
    # 결과 출력
    print(f"원주율의 근사값: {pi_approx:.4f}")

if __name__ == "__main__":
    main()
