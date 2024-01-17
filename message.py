import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# 소켓모드로 사용하기 위해 토큰 설정
## 각자 환경변수에 bot token과 app token 설정해주기!
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# 과목 질문 (과목/과정 이 들어간 문장만 캐치)
@app.message(re.compile("(과목|과정)"))
def message_subject(message, say):
    # 답변
    say(f"카카오 엔터프라이즈의 수강 과목으로는 '웹 애플리케이션 개발 Lab1', '데이터관리기술 Lab1', '시스템아키텍쳐 Lab1'이 있습니다.")

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()