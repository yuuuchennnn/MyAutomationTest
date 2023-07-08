import requests

def http_post_request(url, request_data):
    # url = "https://api2.bybit.com/s1/campaign/referral/commission/get_faqs_and_terms"
    # request_data = {"lang":"en-US"}
    response = requests.post(url,json=request_data)


# Print the response
response_json = response.json()
print(response)
print(response_json)


