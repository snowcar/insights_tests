from tools import InsightTest


class EnrollmentTest(InsightTest):
    @classmethod
    def url(cls):
        return "{}/api/report/enrollment/".format(cls.instance_url())
