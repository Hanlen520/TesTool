import pytest
import allure
from operation.user import login_user
from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 登录用户")
def step_1(username):

    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.step("步骤2 ==>> 登录返回")
def step_2(message):
    logger.info("步骤2 ==>> 返回消息：{}".format(message))


@allure.step("步骤3")
def step_3(success):
    logger.info("步骤2 ==>> 断言是否成功：{}".format(success))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")

class TestUserLogin:

    @allure.story("用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {username}，{password}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username, password, usertype, expect_code", api_data['login'])
    def test_login_user(self, username, password, usertype, expect_code):
        logger.info("*************** 开始执行用例 ***************")
        step_1(username)
        result = login_user(username, password, usertype)
        step_2(result.msg)
        assert result.code == int(expect_code)
        step_3(result.code == int(expect_code))
        # assert result.success == except_result, result.error
        assert result.response.status_code == 200
        # assert result.success == except_result, result.error
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        # assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_user_login.py"])
