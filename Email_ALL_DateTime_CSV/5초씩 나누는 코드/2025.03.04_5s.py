import pandas as pd
import numpy as np
from pathlib import Path

# 디렉토리 설정
input_dir = Path(r'C:/Users/LG/Desktop/PN_Project/PN_Project/Email_ALL_DateTime_CSV/2025.03.04')
output_dir = input_dir / '5초씩 데이터 가공'
output_dir.mkdir(exist_ok=True)

# 모든 CSV 파일 처리
for csv_path in input_dir.glob('*.csv'):
    # 데이터 로드
    df = pd.read_csv(csv_path)

    # PackVolt와 Current만 추출하여 2열 배열 생성
    arr = df[['PackVolt', 'Current']].to_numpy()
    # 5개 단위로 자를 수 있는 길이 계산
    n = (len(arr) // 5) * 5
    # (n,2) 배열을 (n/5, 10) 배열로 변환
    arr5 = arr[:n].reshape(-1, 10)

    # 빈 첫 열 추가 및 DataFrame 생성
    out_df = pd.DataFrame(arr5)
    out_df.insert(0, '', '')

    # 첫 행 제거 및 인덱스 재설정
    out_df = out_df.iloc[1:].reset_index(drop=True)

    # CSV 저장 (헤더 없이)
    out_path = output_dir / f"{csv_path.stem}_5s.csv"
    out_df.to_csv(out_path, index=False, header=False)
    print(f"Saved: {out_path}")
