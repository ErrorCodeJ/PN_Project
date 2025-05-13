import pandas as pd
from pathlib import Path

# 기본 경로 설정
input_dir = Path(r'C:/Users/LG/Desktop/PN_Project/PN_Project/Email_ALL_DateTime_CSV/2025.03.18/로더')
output_dir = input_dir / '5초씩 데이터 가공'
output_dir.mkdir(exist_ok=True)

# CSV 파일 자동 처리
for csv_path in input_dir.glob('*.csv'):
    # 데이터 로드 및 PackVolt, Current 추출
    df = pd.read_csv(csv_path)
    arr = df[['PackVolt', 'Current']].values

    # 5개 단위로 묶고 첫 행 제거
    n = (len(arr) // 5) * 5
    arr5 = arr[:n].reshape(-1, 10)[1:]

    # DataFrame 생성 후 빈 첫 칼럼 삽입
    out_df = pd.DataFrame(arr5)
    out_df.insert(0, '', '')

    # 저장 (헤더 및 인덱스 제외)
    out_df.to_csv(output_dir / f"{csv_path.stem}_5s.csv", index=False, header=False)
    print(f"Saved: {csv_path.name}")
