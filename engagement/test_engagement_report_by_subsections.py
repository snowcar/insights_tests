from . import EngagementTest


class TestEngagementCombine(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementCompareCourses(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementCompareUsers(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "users",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementCompareProp(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "course_section",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementCompareRuns(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "runs",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementPropCombine(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementPropCompareCourses(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementPropCompareProp(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementPropCompareUsers(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementPropCompareRuns(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [],
                "user_search": None,
                "org_details": []
            }
        }


class TestEngagementUserCombine(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserCompareCourses(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserCompareProp(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserCompareUsers(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserCompareRuns(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
                "org": [
                    "9655"
                ],
                "properties": {},
                "course": [],
                "run": [],
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserPropCombine(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserPropCompareCourses(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserPropCompareProp(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserPropCompareUsers(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }


class TestEngagementUserPropCompareRuns(EngagementTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "reportType": "engagement",
                "reportBy": "subsections",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "chartDimension": "usage",
                "browserTzOffset": 180,
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
                "section": [],
                "user_ids": [
                    "1105854"
                ],
                "user_search": None,
                "org_details": [
                    {
                        "org": "9655",
                        "enable_page_level_engagement": False
                    }
                ]
            }
        }
