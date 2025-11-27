class Helpers:
    @staticmethod
    def check_json_contains_template(json, template):
        for key, value in template.items():
            if not(key in json): return False
            if not(json[key] == value): return False
        return True