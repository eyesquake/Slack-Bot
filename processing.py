import slack_sdk
import pandas as pd

# 판다스 출력 옵션 설정
pd.set_option('display.max_rows', None)  # 행의 최대 출력 개수 설정 (None으로 설정하면 모든 행을 출력)
pd.set_option('display.max_columns', None)  # 열의 최대 출력 개수 설정 (None으로 설정하면 모든 열을 출력)
pd.set_option('display.max_colwidth', None)  # 열 너비의 최대 출력 길이 설정
#########################[데이터 처리]#########################
# 엑셀 파일 읽기
df = pd.read_excel('final.xlsx')

# NaN 값을 빈 문자열로 채우기
df['대댓글'] = df['대댓글'].fillna('')

# '내용'과 '댓글' 기준으로 데이터 그룹화
grouped = df.groupby(['내용', '댓글'])

# 그룹별로 '대댓글' 합치기
# 대댓글 사이에 '/' 추가
df['대댓글'] = grouped['대댓글'].transform(lambda x : ' / '.join(x))

# # 중복 행 제거
df = df.drop_duplicates()

print(df)
# 엑셀 파일로 저장
df.to_excel('test.xlsx', index=False)

#########################[슬랙에 메시지 보내기]#########################
# slack_token = 'xoxb-6463685886582-6491398823217-bKDbTZlx1l4h19FrkRolJ5sY'
#
# client = slack_sdk.WebClient(token=slack_token)
# client.chat_postMessage(channel='#키봇-채널', text='슬랙 테스트')