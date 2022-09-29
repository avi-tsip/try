from datetime import datetime
from json import JSONDecodeError
from pathlib import Path
import json
import re


class InterviewDemo:
    """

    """

    def __init__(self, json_path: Path):
        self.date_length = 19
        for file in json_path.iterdir():
            if file.name == 'data.json':
                with open(file) as f:
                    try:
                        self.json_file = json.load(f)
                    except Exception:
                        raise json.JSONDecodeError('Bad Input', 'data.json', 1)

    def refactor_json(self):
        """
        This helper method modifies the json initiated on the class level according to instructions:
        if string -> remove whitespace
        if list -> remove duplicates
        if time stamp -> change year to 2001
        after modification it saves the result in a new json file

        """
        for key, value in self.json_file.items():
            if type(value) == list:
                self.remove_duplicates(key, value)
            else:
                is_date, value = self.validate_date_string(key, value)
                if is_date:
                    self.remove_replace_year(key, value)
                else:
                    self.remove_white_spaces(key, value)
        self.save_new_file()

    def remove_replace_year(self, key, value):
        """
        This helper method modifies the year in a timestamp string
        """
        year = value[0: 4]
        if year != "2001":
            modified_date = value.replace(year, '2001')
            self.json_file[key] = str(modified_date)

        # previous attempt to use datetime for this application

        # date = datetime.strptime(value, '%Y/%m/%d %H:%M:%S')
        # modified_date = date.replace(year=2001)
        # self.json_file[key] = str(modified_date)

    def remove_white_spaces(self, key, value):
        """
        This helper method removes whitespace from the string
        """
        modified_string = value.replace(" ","")
        self.json_file[key] = modified_string

    def remove_duplicates(self, key, value):
        """
        This helper method removes duplicate entries from the list
        """
        result = []
        [result.append(x) for x in value if x not in result]
        self.json_file[key] = result

    def save_new_file(self):
        """
        This helper method saves the modified json in a new file
        """
        with open('updated_file.json', 'w') as f:
            f.write(json.dumps(self.json_file))

    def validate_date_string(self, key, value):
        """
        This helper method verifies that the string is a time stamp and returns true of false accordingly
        """
        pattern = r"\d{4}/\d{2}/\d{2}\s\d{2}:\d{2}:\d{2}(.|$)"
        if re.match(pattern, value):
            if len(value) > self.date_length:
                value = value[0: self.date_length]
            is_date = True
        else:
            is_date = False
        return is_date, value

        # previous attempt to use datetime for this application

        # try:
        #     datetime.strptime(value, '%Y/%m/%d %H:%M:%S')
        #     is_date = True
        # except ValueError:
        #     print(f"Couldn't convert to date time with ValueError")
        #     is_date = False
        # return is_date


# demo = InterviewDemo(Path.cwd())
# demo.refactor_json()
