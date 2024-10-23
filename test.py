import random
import math

def buffons_needle(num_trials, L, a, b):
    hits = 0
    
    for _ in range(num_trials):
        # 선분의 중심 좌표와 각도 생성
        center_x = random.uniform(0, a / 2)
        angle = random.uniform(0, math.pi)  # 0부터 π까지의 각도

        # 선분의 끝점이 격자선에 닿는지 확인
        delta_x = (L / 2) * math.cos(angle)
        
        alpha_x = (L / 2) * math.sin(angle)
        
        # 닿는지 확인
        if center_x <= delta_x or center_x <=alpha_x :
            hits += 1
        else :
            continue
                
    # 원주율 근사값 계산 (격자선 간격을 a로 설정)
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
