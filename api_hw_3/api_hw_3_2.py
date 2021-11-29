from pprint import pprint
import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def __get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def __get_upload_link(self, disk_file_path):
        upload_link = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.__get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_link, params=params, headers=headers)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.__get_upload_link(disk_file_path).get("href", -1)
        response = requests.put(href, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            return "Success"


if __name__ == "__main__":
    pc_path_to_file = input("Enter path to the file: ")
    token = ""
    uploader = YaUploader(token)
    print(uploader.upload_file_to_disk("test_file.txt", pc_path_to_file))