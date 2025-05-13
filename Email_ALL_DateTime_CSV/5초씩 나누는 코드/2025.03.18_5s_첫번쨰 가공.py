import pandas as pd

# 처리할 파일 목록 (입력 경로, 출력 경로)
files = [
    (r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\20250318140111_CW_12_out.csv', r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\5초씩 데이터 가공\첫번쨰 가공\20250318140111_CW_12_out_PC1.csv'),
    (r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\20250318140938_CW_out.csv', r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\5초씩 데이터 가공\첫번쨰 가공\20250318140938_CW_out_PC1.csv'),
    (r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\20250318142457_NoLabel_out.csv', r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\5초씩 데이터 가공\첫번쨰 가공\20250318142457_NoLabel_out_PC1.csv'),
    (r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\20250318144344_CW_out.csv', r'C:\Users\LG\Desktop\PN_Project\PN_Project\Email_ALL_DateTime_CSV\2025.03.18\로더\5초씩 데이터 가공\첫번쨰 가공\20250318144344_CW_out_PC1.csv'),
]

for input_path, output_path in files:
    # CSV 읽기 및 DateTime을 인덱스로 설정
    df = pd.read_csv(input_path, parse_dates=['DateTime'])
    df.set_index('DateTime', inplace=True)
    
    # 1초 단위 리샘플링 후 평균 계산
    agg = df[['PackVolt', 'Current']].resample('S').mean()
    
    # 결과 저장
    agg.to_csv(output_path)
    
    # 미리보기 출력
    print(f"=== {input_path.split('/')[-1]} 결과 미리보기 ===")
    print(agg.head(), "\n")
