# from atoms import http_atom
from atoms.http_atom import HttpAtom
import json


class CheckRetCode:
    def __init__(self,test_data):
        self.url = test_data["url"]
        self.request_data = json.loads(test_data["request_data"])

    def check_referral_page_ret_code(self):
        get_faqs_and_terms = HttpAtom(self.url, self.request_data)
        res = get_faqs_and_terms.http_post_request()
        assert res['ret_code'] == 0, "ret code is not 0"