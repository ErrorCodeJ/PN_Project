import pandas as pd
import numpy as np
import glob
import os

# 경로 설정
input_dir = r'C:/Users/LG/Desktop/PN_Project/Email_ALL_DateTime_CSV/2025.04.30/1차가공'
output_dir = r'C:/Users/LG/Desktop/PN_Project/Email_ALL_DateTime_CSV/2025.04.30/2차가공'
os.makedirs(output_dir, exist_ok=True)

# '_out_초단위_평균.csv' 패턴의 모든 파일 처리
pattern = os.path.join(input_dir, '*_out_초단위_평균.csv')
for filepath in glob.glob(pattern):
    df = pd.read_csv(filepath, encoding='cp949')
    
    # 데이터 준비
    v = df['PackVolt'].round(2).values
    c = df['Current'].round(2).values
    n = min(len(v), len(c)) // 5
    
    # 5개 단위로 reshape 및 결합
    v = v[:n*5].reshape(n, 5)
    c = c[:n*5].reshape(n, 5)
    combined = np.hstack([v, c])
    
    # 결과 DataFrame 생성 및 빈 A열 삽입
    result = pd.DataFrame(combined)
    result.insert(0, '', '')
    
    # 출력 파일명 생성 및 저장
    name = os.path.splitext(os.path.basename(filepath))[0]
    out_path = os.path.join(output_dir, f"{name}_grouped_with_blankA.csv")
    result.to_csv(out_path, index=False, header=False)
    print(f"Saved: {out_path}")

print("모든 파일 처리가 완료되었습니다.")
