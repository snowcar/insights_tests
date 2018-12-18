from . import AssessmentsTest


class TestAssessmentCombine(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentCompareCourses(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentCompareRuns(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentCompareProp(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentCompareUsers(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentPropCombine(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentPropCompareCourses(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentPropCompareRuns(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentPropCompareProp(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentPropCompareUsers(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "47505"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAssessmentUserCombine(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserCompareCourses(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserCompareRuns(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserCompareProp(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserCompareUsers(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {},
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserPropCombine(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserPropCompareCourses(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserPropCompareRuns(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserPropCompareProp(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }


class TestAssessmentUserPropCompareUsers(AssessmentsTest):
    @classmethod
    def body(cls):
        return {
            "filters": {
                "org": [
                    "9655"
                ],
                "assessment": {},
                "assessmentRaw": [],
                "properties": {
                    "course_section": [
                        "66624"
                    ]
                },
                "course": [],
                "coursesRaw": [],
                "run": [],
                "viewBy": "assessments",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }
