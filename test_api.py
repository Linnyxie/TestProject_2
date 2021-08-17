"""
    test CODING
"""


class TestCoding:
    def test_status_code(self):
        # 使用assert语句判断响应码是否符合预期
        # assert req.status_code == 200
        assert 1 + 2 == 3

    def test_resp_message(self):
        # assert req.json()["message"] == "成功!"
        assert 1 + 3 == 3
