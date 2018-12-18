from . import LOTest


class TestLOCombine(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOCompareCourses(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOCompareRuns(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOCompareProp(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOCompareUsers(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOPropCombine(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "American-Public-University-System"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "CourseSection"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "assessments",
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOPropCompareCourses(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "American-Public-University-System"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "CourseSection"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOPropCompareRuns(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "American-Public-University-System"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "CourseSection"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOPropCompareProp(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "American-Public-University-System"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "CourseSection"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOPropCompareUsers(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "American-Public-University-System"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "CourseSection"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestLOUserCombine(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "assessments",
                "chartFormat": "combine",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserCompareCourses(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserCompareRuns(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserCompareProp(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserCompareUsers(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {},
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserPropCombine(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "7723393"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "assessments",
                "chartFormat": "combine",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserPropCompareCourses(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "7723393"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserPropCompareRuns(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "7723393"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserPropCompareProp(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "7723393"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }


class TestLOUserPropCompareUsers(LOTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "Alaska-Christian-College"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "tag": [],
                "properties": {
                    "course_section": [
                        "7723393"
                    ]
                },
                "course": [],
                "run": [],
                "viewBy": "assessments",
                "reportType": "learningOutcomes",
                "reportBy": "learningOutcomes",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [
                    "1084476"
                ],
                "user_search": None
            }
        }
