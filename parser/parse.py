"""
    Parser script to parse the XML files given in the actions folder
"""
import xml.etree.ElementTree as ET

"""
    @method parse_xml_file(filename: str) -> zip
        @param filename: The filename of the underlying SSBD+ XML file to be parsed.

        @note: The function returns an iterable that can be used as follows:
        ```
            v = parse_xml_file(filename = ...)
            for t,c in v:
                ...
                # t contains a ":" separated string of start and end timestamps of the actions (in seconds)
                # c contains the category string of the corresponding actions
        ```
"""
def parse_xml_file(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    all_time_stamps = []
    all_categories = []

    for child in root:
        for index in child:
            if index.tag == "behaviour":
                all_time_stamps.append(index[0].text)
                all_categories.append(index[1].text)

    return zip(all_time_stamps, all_categories)