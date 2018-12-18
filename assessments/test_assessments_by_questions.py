from . import AssessmentsTest


class TestQuestionsCombine(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsCompareCourses(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsCompareRuns(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsCompareProperty(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsCompareLearners(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsPropertyCombine(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsPropertyCompareCourses(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsPropertyCompareRuns(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsPropertyCompareProperty(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "course_section",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsPropertyCompareLearners(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [],
                "user_search": None
            }
        }


class TestQuestionsUserCombine(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "combine",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestQuestionsUserCompareCourses(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestQuestionsUserCompareRuns(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "runs",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestQuestionsUserCompareProps(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "courses",
                "chartFormat": "course_section",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestQuestionsUserCompareLearners(AssessmentsTest):
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
                "viewBy": "questions",
                "reportBy": "assessments",
                "reportCompareBy": "users",
                "chartFormat": "compare",
                "user_ids": [
                    "1105968"
                ],
                "user_search": None
            }
        }


class TestQuestionsUserPropertyCombine(AssessmentsTest):
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
                "viewBy": "questions",
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


class TestQuestionsUserPropertyCompareCourses(AssessmentsTest):
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
                "viewBy": "questions",
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


class TestQuestionsUserPropertyCompareCourses(AssessmentsTest):
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
                "viewBy": "questions",
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


class TestQuestionsUserPropertyCompareRuns(AssessmentsTest):
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
                "viewBy": "questions",
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


class TestQuestionsUserPropertyCompareProps(AssessmentsTest):
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
                "viewBy": "questions",
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


class TestQuestionsUserPropertyCompareUsers(AssessmentsTest):
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
                "viewBy": "questions",
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
