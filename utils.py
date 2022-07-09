import json


def load_candidates():
    """загрузит данные из файла candidates.json
    :return list[dict]"""

    with open("candidates.json", encoding="UTF-8") as file:
        candidates = json.load(file)
    return candidates


candidat = load_candidates()


def get_all(candidat):
    """покажет всех кандидатов"""

    result = "<pre>"
    for i in candidat:
        result += f"""Имя кандидата:{i['name']}\n
Позиция кандидата:{i['position']}\n
Навыки:{i['skills']}\n
"""
    result += "</pre>"
    return result


def get_by_pk(pk):
    """вернет кандидата по pk"""

    result = "<pre>"
    for i in candidat:
        if pk == i["pk"]:
            result += f"""<img src='{i['picture']}'>\n
Имя кандидата:{i['name']}\n
Позиция кандидата:{i['position']}\n
Навыки:{i['skills']}\n
            """
            result += "</pre>"
            return result


def get_by_skill(skill_name):
    """вернет кандидатов по навыку"""

    result = "<pre>"
    for i in candidat:
        if skill_name.lower() in i["skills"].lower():
            result += f"""Имя кандидата:{i['name']}\n
Позиция кандидата:{i['position']}\n
Навыки:{i['skills']}\n

"""
    result += "</pre>"
    return result
