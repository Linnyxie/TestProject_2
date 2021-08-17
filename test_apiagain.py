import requests


# 请求网易新闻列表
req = requests.get("https://api.apiopen.top/getWangYiNews")


class TestWangyinews:
    def test_status_code(self):
        # 使用assert语句判断响应码是否符合预期
        assert req.status_code == 200

    def test_resp_message(self):
        assert req.json()["message"] == "成功!"
