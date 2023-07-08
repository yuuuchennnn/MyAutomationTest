import requests


class HttpAtom:
    def __init__(self, url, request_data):
        self.url = url
        self.request_data = request_data

    def http_post_request(self):
        # self.url = "https://api2.bybit.com/s1/campaign/referral/commission/get_faqs_and_terms"
        # self.request_data = {"lang":"en-US"}
        # print(type(self.request_data), self.request_data)
        response = requests.post(self.url,json=self.request_data)
        return response.json()

# Print the response
# response_json = response.json()
# print(response)
# print(response_json)


