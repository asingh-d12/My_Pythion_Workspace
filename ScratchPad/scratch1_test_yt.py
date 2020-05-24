import requests

the_url = "https://www.youtube.com/watch?v=ci-KJ1x5Qh8"
with open("a_test_yt", 'w') as a_test:
    a_test.write(requests.get(the_url).text)
