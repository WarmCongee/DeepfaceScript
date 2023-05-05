from deepface import DeepFace
import json
import cv2

class JsonStringOperations:
    @staticmethod
    def print_formatted_result(result):
        if isinstance(result, str):
            parsed = json.loads(result)
            print(json.dumps(parsed, indent=4, sort_keys=True))
        else:
            print(json.dumps(result, indent=4, sort_keys=True))

    @staticmethod
    def get_json_target_value(dic_json, target_key):
        # dic = {}
        if isinstance(dic_json, str):
            temp = json.loads(dic_json)
        if isinstance(dic_json, dict):
            temp = dic_json
        for key in temp:
            if key == target_key:
                return temp[key]
            if isinstance(temp[key], dict):
                JsonStringOperations.get_json_target_value(temp[key])
                # dic[key] = temp[key]
            # else:
            # dic[key] = temp[key]


class Analyze:
    @staticmethod
    def analyze_age(url):
        return DeepFace.analyze(img_path=url, actions=["age"])

    @staticmethod
    def analyze_gender(url):
        return DeepFace.analyze(img_path=url, actions=["gender"])

    @staticmethod
    def analyze_emotion(url):
        return DeepFace.analyze(img_path=url, actions=["emotion"])

    @staticmethod
    def analyze_race(url):
        return DeepFace.analyze(img_path=url, actions=["race"])

    @staticmethod
    def analyze_all(url):
        return DeepFace.analyze(img_path=url, actions=["age", "gender", "emotion", "race"])
