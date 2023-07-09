import pytest
from tools.data_loader import yaml_data_loader
import yaml
from components import referral_check_success
from components.referral_check_success import CheckRetCode


class TestClass:
    @pytest.mark.parametrize("test_data", yaml_data_loader("referral_text.yaml"))
    def test_referral_page_text(self, test_data: dict):
        checker = CheckRetCode(test_data)
        checker.check_referral_page_ret_code()


