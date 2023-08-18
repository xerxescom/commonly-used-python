import base64
import json


def encode_xml_to_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            xml_data = file.read()
            encoded_data = base64.b64encode(xml_data)
            return encoded_data.decode(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


if __name__ == '__main__':
    xml_file_path = 'exp.xml'
    encoded_xml = encode_xml_to_base64(xml_file_path)
    if encoded_xml:
        # 将编码后的数据写入JSON文件
        json_data = {"data": encoded_xml}
        output_json_file_path = 'result.json'
        with open(output_json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)
        print("Base64 Encoded XML has been written to the JSON file.")
