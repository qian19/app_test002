import allure
import pytest
class Test_001:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是第一个测试方法")
    def test_001(self):
        allure.attach("test_001_1","这是test_001_1的步骤描述")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是第二个测试报告")
    def test_002(self):
        allure.attach("test_001_2","这是test_001_2的步骤描述")
        assert 0


    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是第三个测试报告")
    def test_003(self):
        allure.attach("test_001_3","这是test_001_3的步骤描述")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是第四个测试报告")
    def test_004(self):
        allure.attach("test_001_4","这是test_001_4的步骤描述")
        assert 1


    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是第五个测试报告")
    def test_005(self):
        allure.attach("test_001_5","这是test_001_5的步骤描述")
        assert 0