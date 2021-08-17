import requests
import pytest
import allure
import os


# 请求网易新闻列表
req = requests.get("https://api.apiopen.top/getWangYiNews")
# 打印响应码
# print("响应码：", req.status_code)


# 使用pytest管理测试用例、allure生成测试报告
@allure.feature("测试获取网易新闻的API")
class TestWangyinews:
    @allure.story("判断状态码是否为200")
    # Pytest可识别的样式：以test_开头的函数或方法、以Test开头的类
    def test_status_code(self):
        # 使用assert语句判断响应码是否符合预期
        assert req.status_code == 200

    @allure.story("判断返回的message是否为成功")
    def test_resp_message(self):
        assert req.json()["message"] == "成功!"


if __name__ == '__main__':
    # 执行用例并生成测试报告
    pytest.main(['--alluredir', 'report/result', 'apitest.py'])
    # 渲染并打开测试报告
    os.system('allure serve report/result')
