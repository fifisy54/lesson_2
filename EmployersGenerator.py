class EmployersGenerator:

    def run(self):
        with open('Names.txt', 'r') as file:
            strings = file.readlines()
        for string in strings:
            name, age = string.split(', ')
            dict = {'Name': name, 'Age': age}
            yield dict


class Company:

    def get_employers(self):
        employers_generator = EmployersGenerator()
        for employer in employers_generator.run():
            print(employer["Name"], employer["Age"])

    @staticmethod
    def get_company_name():
        company_name = input()
        return company_name


company = Company()
company.get_employers()
company.get_company_name()