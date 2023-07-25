import pytest
from tools.data_loader import yaml_data_loader
import yaml
from components import referral_check_success
from components.referral_check_success import CheckRetCode
from loguru import logger

class TestClass:
    @pytest.mark.parametrize("testData", yaml_data_loader("referral_text.yaml"))
    def test_referral_page_text(self, testData: dict):
        logger.info(testData)
        checker = CheckRetCode(testData)
        checker.check_referral_page_ret_code()


