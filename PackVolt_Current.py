import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로드
df = pd.read_csv(r'C:\Users\admin\Desktop\2025. 04.25 PN\Edit.csv')

# 'time' 컬럼(MM:SS.s) → 총 초(second)로 변환
time_split = df['time'].str.split(':', expand=True)
minutes = time_split[0].astype(float)
seconds = time_split[1].astype(float)
df['total_seconds'] = minutes * 60 + seconds

# 시작 시점을 0초로 맞추기 위해 첫 데이터의 초값 활용
start_time = df['total_seconds'].iloc[0]
df['rel_seconds'] = df['total_seconds'] - start_time

# 1초부터 100초 구간만 필터링 및 복사
df_filtered = df[(df['rel_seconds'] >= 1) & (df['rel_seconds'] <= 100)].copy()

# 5초 단위로 구간 나누기
bins = list(range(1, 102, 5))  # 1, 6, 11, ..., 101
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]
df_filtered['interval'] = pd.cut(df_filtered['rel_seconds'], bins=bins, labels=labels, include_lowest=True)

# 구간별 평균 PackVolt 및 Current 계산
grouped = df_filtered.groupby('interval')[['PackVolt', 'Current']].mean()

# 꺾은선 그래프로 시각화 (양측 값 동일 축)
plt.figure()
plt.plot(grouped.index, grouped['PackVolt'], marker='o', label='Average PackVolt')
plt.plot(grouped.index, grouped['Current'], marker='s', label='Average Current')
plt.xlabel('Time Interval (s)')
plt.ylabel('Value')
plt.title('Average PackVolt and Current per 5-Second Interval (1s to 100s)')
plt.ylim(min(grouped.min()) - 10, max(grouped.max()) + 10)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
