from tools import InsightTest


class LOTest(InsightTest):
    @classmethod
    def url(cls):
        return "{}/api/report/performance/".format(cls.instance_url())
