import pytest
import allure
import requests.cookies

from operation.user import register_user, login_user, get_one_user_info
from common.logger import logger



@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.step("步骤2 ==>> 获取某个用户信息")
def step_2(username):
    logger.info("步骤3 ==>> 获取某个用户信息：{}".format(username))


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户登录-查看用户信息")
class TestUserInfo(object):

    def setup_class(self):
        self.cookie = None

    def teardown_class(self):
        print("teardown class")

    def assignment(self, kwargs):
        for k, v in kwargs.items():
            if type(v) is dict:
                self.assignment(v)
            else:
                if v:
                    pass
                else:
                    kwargs[k] = getattr(self, k)
        return kwargs

    @allure.story("用例--注册/登录/查看--预期成功")
    @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户注册登录查看-预期成功")
    @pytest.mark.multiple
    def test_user_login_userinfo(self, testcase_data):
        username = testcase_data['username']
        password = testcase_data['password']
        usertype = testcase_data['usertype']
        result = login_user(username, password, usertype)
        assert result.success is True, result.msg
        self.cookie = result.response.cookies
        result = get_one_user_info(self.cookie)
        assert result.success is True, result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_user_info.py"])