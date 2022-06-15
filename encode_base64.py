import base64


def encode_binary_to_base64():

    with open(".docx FILE GOES HERE", "rb") as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_code = base64_encoded_data.decode('utf-8')
        print(base64_code)

    base64_bytes = base64_code.encode('utf-8')
    with open('decoded_file.txt', "wb") as file_to_save:
        decoded_data = base64.decodebytes(base64_bytes)
        file_to_save.write(decoded_data)
        print(decoded_data)


if __name__ == '__main__':
    encode_binary_to_base64()
