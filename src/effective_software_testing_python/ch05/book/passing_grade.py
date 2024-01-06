"""PassingGrade class."""


class PassingGrade:
    @staticmethod
    def passed(grade):
        if grade < 1 or grade > 10:
            raise ValueError()
        return grade >= 5
