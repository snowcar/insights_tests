from . import AssessmentsTest


class TestAnswerCombine(AssessmentsTest):
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
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerCompareCourses(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerCompareRuns(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerCompareProps(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerCompareUsers(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerPropsCombine(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerPropsCompareCourses(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerPropsCompareRuns(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerPropsCompareProps(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerPropsCompareUsers(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestAnswerUserCombine(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAnswerUserCompareCourses(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAnswerUserCompareRuns(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAnswerUserCompareProps(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAnswerUserCompareUsers(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestAnswerUserPropsCombine(AssessmentsTest):
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
                "viewBy": "answers",
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


class TestAnswerUserPropsCompareCourses(AssessmentsTest):
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
                "viewBy": "answers",
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


class TestAnswerUserPropsCompareRuns(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "combine",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }


class TestAnswerUserPropsCompareProps(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "combine",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }


class TestAnswerUserPropsCompareUsers(AssessmentsTest):
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
                "viewBy": "answers",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "combine",
                "user_ids": [
                    "1105968",
                    "1101732"
                ],
                "user_search": None
            }
        }
