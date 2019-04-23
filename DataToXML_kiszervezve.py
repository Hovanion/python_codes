# -*- coding: utf-8 -*-

try:
    import xml.etree.cElementTree as et
except:
    import xml.etree.ElementTree as et


def append_shop(shopDetails, parentTag):
    bolt = et.SubElement(parentTag, "shop")
    nev = et.SubElement(bolt, "name")
    tipus = et.SubElement(bolt, "type")
    cim = et.SubElement(bolt, "address")
    irsz = et.SubElement(cim, "postalcode")
    varos = et.SubElement(cim, "city")
    kozter = et.SubElement(cim, "street")
    hazszam = et.SubElement(cim, "housenumber")
    nyitva = et.SubElement(bolt, "open")
    ertekeles = et.SubElement(bolt, "rating")

    nev.text = shopDetails[0]
    tipus.text = shopDetails[5]
    irsz.text = shopDetails[1]
    varos.text = shopDetails[2]
    kozter.text = shopDetails[3]
    hazszam.text = shopDetails[4]
    nyitva.text = shopDetails[6]
    ertekeles.text = shopDetails[7]


def get_file_lines(fileName):
    lines = []
    file = open(fileName, "r", encoding="utf-8")
    for line in file:
        lines.append(line)
    file.close()
    return lines


def create_shops_xml_from_file(filename):
    lines = get_file_lines(filename)
    data = et.Element("shops")
    for line in lines:
        line = line.strip()
        shop_details = line.split('\t')
        append_shop(shop_details, data)
    return data


def write_xml_to_file(xml, file_name):
    writer = open(file_name, "w", encoding="utf-8")
    writer.write(et.tostring(xml).decode())


shop_xml = create_shops_xml_from_file("adat.txt")
write_xml_to_file(shop_xml, "hazi_xml_with_functions.xml")




