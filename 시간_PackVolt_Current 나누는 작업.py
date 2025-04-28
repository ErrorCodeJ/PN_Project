import pandas as pd

# 원본 CSV 파일 경로
file_path = r'C:\Users\admin\Desktop\2025. 04.25 PN\20250318140938_CW_out.csv'
# 추출된 데이터를 저장할 경로
output_path = r'C:\Users\admin\Desktop\2025. 04.25 PN\Edit.csv'

# 1. CSV 파일 읽기 (DateTime 컬럼을 datetime 타입으로 파싱)
df = pd.read_csv(file_path, parse_dates=['DateTime'])

# 2. 필요한 컬럼만 추출하고 컬럼명 변경
df_subset = df[['DateTime', 'PackVolt', 'Current']].rename(columns={'DateTime': 'time'})

# 3. 결과 확인 (첫 5행 출력)
print(df_subset.head())

# 4. 추출된 데이터 CSV로 저장
df_subset.to_csv(output_path, index=False)
print(f"Saved subset to: {output_path}")
