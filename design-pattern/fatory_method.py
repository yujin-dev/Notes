import json
import xml.etree.ElementTree as etree
"""
    Factory Method ; input에 따라 객체 생성이 달라짐
"""

''' 여러 input( XML, JSON file ) 파싱하여 connection을 centralize '''
class JSONDataExtractor:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def dataextraction_factory(filepath):
    if filepath.endswith("json"):
        extractor = JSONDataExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDataExtractor
    else:
        raise ValueError("Cannot extract data from {}".format(filepath))
    return extractor

def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj

def main():
    sqlite_factory = extract_data_from("data/sample.sq3")
    # raise Exception

    json_factory = extract_data_from("data/movies.json")
    json_data = json_factory.parsed_data
    # return json

    xml_factory = extract_data_from("data/sample.xml")
    xml_data = xml_factory.parsed_data
    # return xml

