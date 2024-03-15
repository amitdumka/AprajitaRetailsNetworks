#File-IO Ultilities
#Amit Kumar
#Date: 13/02/2024

import pandas as pd

#File IO Helper
class FileIOHelper:

    def __init__(self):
        pass

    def excelToJson(self, excelFile, sheetName):
        data = pd.read_excel(excelFile, sheet_name=sheetName)
        json_data = data.to_json(orient="records")
        return json_data
    def saveExcelToJson(self, excelFile, sheetName, jsonFile):
        data = pd.read_excel(excelFile, sheet_name=sheetName)
        json_data = data.to_json(orient="records")
        #Save Json_data to file 
        with open(jsonFile, "w") as file:
            file.write(json_data)

    def saveJsonToExcel(self, jsonFile, excelFile, sheetName):
        with open(jsonFile, "r") as file:
            json_data = file.read()
        data = pd.read_json(json_data)
        data.to_excel (excelFile, sheet_name=sheetName, index=False)


# if __name__ == "__main__":
#     fileIOHelper = FileIOHelper()
#     json_data = fileIOHelper.excelToJson("002.xlsx", "MasterData")
#     print(json_data)
#     fileIOHelper.saveExcelToJson("002.xlsx", "MasterData", "output.json")
#     fileIOHelper.saveJsonToExcel("output.json", "002.xlsx", "MasterData")