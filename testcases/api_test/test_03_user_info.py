import pytest
import allure
import requests

from testcases.conftest import api_data
from common.logger import logger
from operation.user import login_user, get_one_user_info


@allure.step("步骤1 ==>> 用户登录")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户ID：{}".format(username))


@allure.step("步骤2 ==>> 用户查看个人信息")
def step_2(cookie):
    logger.info("步骤2 ==>> 登录成功 ==>> 返回的 cookie 为：{}".format(requests.utils.dict_from_cookiejar(cookie)))


@allure.step("步骤3 ==>> 获取到用户的信息")
def step_3(userinfo):
    logger.info(
        "步骤3 ==>> 结果为: 用户id: {} 用户名字: {} 班级: {} 学院: {} 昵称: {} 邮箱: {}".format(
            userinfo['username'],
            userinfo['name'],
            userinfo['class'],
            userinfo['school'],
            userinfo['nickname'],
            userinfo['email']))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户查看个人信息测试")
class TestUserInfo(object):

    @allure.story("用例--查看用户信息")
    @allure.description("该用例是针对获取用户个人信息的接口的测试")
    @allure.issue("https://blog.csdn.net/zhouchen1998", name="点击跳转到对应的缺陷管理地址")
    @allure.testcase("https://blog.csdn.net/zhouchen1998", name="点击跳转到测试用例地址")
    @allure.title("测试数据: [{username}, {password}]")
    @pytest.mark.signle
    @pytest.mark.parametrize("username, password, usertype, expect_code, expect_msg", api_data['test_user_info'])
    def test_userinfo(self, username, password, usertype, expect_code, expect_msg):
        logger.info("*************** 开始执行用例 ***************")
        step_1(username)
        result = login_user(username, password, usertype)
        assert result.success is True, result.msg
        cookie = result.response.cookies
        step_2(cookie)
        result = get_one_user_info(cookie)
        assert result.success is True
        step_3(result.json)
        logger.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_user_info.py"])


