import random
import math

def buffons_needle(num_trials, L, d):
    # 격자선에 닿은 선분의 수
    hits = 0
    
    for _ in range(num_trials):
        # 선분의 중심 좌표와 각도 생성
        center_x = random.uniform(0, d / 2)
        angle = random.uniform(0, math.pi / 2)  # 0부터 π/2까지의 각도
        
        # 선분의 끝점이 격자선에 닿는지 확인
        if center_x <= (L / 2) * math.sin(angle):
            hits += 1
            
    # 원주율 근사값 계산
    pi_approx = (2 * L * num_trials) / (hits * d)
    return pi_approx

def main():
    # 사용자로부터 입력 받기
    num_trials = int(input("실험 횟수를 입력하세요: "))
    L = float(input("선분의 길이 L을 입력하세요: "))
    d = float(input("격자의 간격 d를 입력하세요: "))
    
    # 원주율 근사값 계산
    pi_approx = buffons_needle(num_trials, L, d)
    
    # 결과 출력
    print(f"원주율의 근사값: {pi_approx:.4f}")

if __name__ == "__main__":
    main()
