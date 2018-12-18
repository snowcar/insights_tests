from . import EnrollmentTest


class TestEnrollmentCombine(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentCompareRuns(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentCompareProps(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentCompareUsers(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentPropCombine(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentPropCompareRuns(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentPropCompareProps(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentPropCompareUsers(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [],
                "user_search": None
            }
        }


class TestEnrollmentUserCombine(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }


class TestEnrollmentUserCompareRuns(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }


class TestEnrollmentUserCompareProps(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }


class TestEnrollmentUserCompareUsers(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }


class TestEnrollmentUserPropCombine(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }


class TestEnrollmentUserPropCompareRuns(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }


class TestEnrollmentUserPropCompareProps(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }


class TestEnrollmentUserPropCompareUsers(EnrollmentTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "enrollment",
                "reportBy": "runs",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "org": [
                    "9655"
                ],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "run": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None
            }
        }
