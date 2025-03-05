"""
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення
значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

import xml.etree.ElementTree as ET
import logging

def xml_search(file_name, log_file='system_log.log'):
    tree = ET.parse(file_name)
    root = tree.getroot()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                logger.info(f"Number: {group.find('number').text}, incoming: {incoming.text}")
            else:
                logger.info(f"Number: {group.find('number').text}, incoming: відсутній")

#xml_search('groups.xml', 'xml_search.log')