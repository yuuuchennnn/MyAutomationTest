from atoms import http_atom


def check_referral_page_ret_code():
    http_atom.http_post_request(test_data.url,test_data.request_data)