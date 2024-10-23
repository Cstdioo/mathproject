import random
import math

def buffons_needle(num_trials, L, a, b):
    # 격자선에 닿은 선분의 수
    hits = 0
    
    for _ in range(num_trials):
        # 선분의 중심 좌표와 각도 생성
        center_x = random.uniform(0, a / 2)  # x축 중심 좌표
        center_y = random.uniform(0, b / 2)  # y축 중심 좌표
        angle = random.uniform(0, math.pi)  # 0부터 π까지의 각도 (0~180도)

        # x축 격자선에 닿는지 확인
        if center_x <= (L / 2) * math.sin(angle):
            hits += 1
        # y축 격자선에 닿는지 확인
        elif center_y <= (L / 2) * math.cos(angle):
            hits += 1
                
    # 원주율 근사값 계산
    if hits > 0:
        pi_approx = (2 * L * num_trials) / (hits * (a + b))
    else:
        pi_approx = float('inf')  # 히트가 없으면 무한대 처리
    
    return pi_approx

def main():
    # 사용자로부터 입력 받기
    num_trials = int(input("실험 횟수를 입력하세요: "))
    L = float(input("바늘의 길이 L을 입력하세요: "))
    a = float(input("x축 간격 a를 입력하세요: "))
    b = float(input("y축 간격 b를 입력하세요: "))
    
    # 원주율 근사값 계산
    pi_approx = buffons_needle(num_trials, L, a, b)
    
    # 결과 출력
    print(f"원주율의 근사값: {pi_approx:.4f}")

if __name__ == "__main__":
    main()
