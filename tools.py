import requests
import json


class InsightTest:
    @classmethod
    def send_request(cls):
        url = cls.url()
        body = json.dumps(cls.body())
        headers = {
            "Content-Type": "application/json",
            "Cookie": cls.cookie()
        }

        cls.result = requests.post(url, data=body, headers=headers)
        print("time={}".format(cls.result.elapsed.total_seconds()))


    @classmethod
    def instance_url(cls):
        return "https://credo-insights.test.credocourseware.com"

    def test_success_result(self):
        assert self.result.status_code == 200

    def test_not_empty_content(self):
        resp = json.loads(self.result.content)
        is_empty = len(resp['content']) == 0 and resp['meta']['error_code'] != "too_many_values_in_result"
        assert not is_empty

    def test_not_empty_properties(self):
        resp = json.loads(self.result.content)
        assert len(resp['filters']['properties']) != 0

    def test_not_empty_users(self):
        resp = json.loads(self.result.content)
        is_empty = len(resp['filters']['user_ids']) == 0 and not resp['filters']['user_search']
        assert not is_empty

    @classmethod
    def body(cls):
        raise NotImplementedError()

    @classmethod
    def url(cls):
        raise NotImplementedError()

    @classmethod
    def cookie(cls):
        return 'DJANGO_SESSION=mfmztodpw09gkzpi7gly3tqt3hv7o591'