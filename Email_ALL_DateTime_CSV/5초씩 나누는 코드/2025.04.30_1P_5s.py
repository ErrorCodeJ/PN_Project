from pathlib import Path
import pandas as pd

# 입력/출력 디렉토리 설정
input_dir  = Path(r'C:\Users\LG\Desktop\PN_Project\Email_ALL_DateTime_CSV\2025.04.30')
output_dir = input_dir / '1차가공'
output_dir.mkdir(parents=True, exist_ok=True)

# '_out.csv' 파일 묶음 처리
for csv_file in input_dir.glob('*_out.csv'):
    # 1) CSV 로드 및 DateTime 파싱
    df = pd.read_csv(csv_file, parse_dates=['DateTime'])
    
    # 2) 초 단위 그룹화 → 평균 → 소수점 2자리 반올림
    avg_df = (
        df.assign(Second=df['DateTime'].dt.floor('S'))
          .groupby('Second')[['PackVolt', 'Current']]
          .mean()
          .round(2)
          .reset_index()
    )
    
    # 3) 저장
    out_file = output_dir / f"{csv_file.stem}_초단위_평균.csv"
    avg_df.to_csv(out_file, index=False, encoding='utf-8-sig')
    print(f"Saved: {out_file}")
