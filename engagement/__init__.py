from tools import InsightTest


class EngagementTest(InsightTest):
    @classmethod
    def url(cls):
        return "{}/api/report/engagement/".format(cls.instance_url())
