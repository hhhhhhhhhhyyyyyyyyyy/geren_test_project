import pytest
import allure

@allure.feature("我的第一个Allure测试")
@allure.story("验证环境配置")
def test_environment():
    with allure.step("检查Java环境"):
        assert True, "Java环境已就绪"
    with allure.step("检查Allure环境"):
        assert True, "Allure环境已就绪"