from tools import InsightTest


class AssessmentsTest(InsightTest):
    @classmethod
    def url(cls):
        return "{}/api/report/assessments/".format(cls.instance_url())
