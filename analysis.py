import openai
import pandas as pd

openai.api_key = 'oepnai_token'

# 응답을 저장할 빈 생성
responses = []

def analysis_gpt(df):
    for idx, row in df.iterrows():
        # '제목', '내용', '댓글', '대댓글' 열을 연결하여 텍스트 데이터 생성
        content = ' '.join(row[['제목', '내용', '댓글', '대댓글']].values.astype(str))
        print("content:", content)


        # GPT-3.5-turbo model을 이용하여 content의 문장을 정리
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content},
                {"role": "assistant", "content": "이 문장을 정리해줘"}
            ]
        )
        print(response['choices'][0]['message']['content'])

        # 응답을 리스트에 추가
        responses.append(response['choices'][0]['message']['content'])

        # 응답을 DataFrame으로 변환하고 엑셀 파일로 저장
        df_responses = pd.DataFrame(responses, columns=['responses'])
        df_responses.to_excel('responses.xlsx', index=False)