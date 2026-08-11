class User:
    def __init__(
        self,
        age,
        gender,
        income,
        utilities,
        entertainment,
        school_fees,
        shopping,
        healthcare
    ):
        self.age = age
        self.gender = gender
        self.income = income
        self.utilities = utilities
        self.entertainment = entertainment
        self.school_fees = school_fees
        self.shopping = shopping
        self.healthcare = healthcare

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "income": self.income,
            "utilities": self.utilities,
            "entertainment": self.entertainment,
            "school_fees": self.school_fees,
            "shopping": self.shopping,
            "healthcare": self.healthcare
        }