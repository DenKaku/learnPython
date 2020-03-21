#------------------------
# Liberary
#------------------------
import os, json, yaml, glob

#------------------------
# Get yaml file path
#------------------------

currentPath = os.path.dirname( __file__ )

inputYamlFilePath = currentPath + "/model/input/test.yaml"
outputJsonFilePath = currentPath + "/model/output/test.json"

with open ( inputYamlFilePath, mode = "r", encoding = "utf-8" ) as file:
    yamlFile = yaml.safe_load( file )


if __name__ == "__main__":

    def parse( parseJson ):

        jsonMode = { "Test" : None }

        if "test" in parseJson:
            jsonMode["Test"] = parseJson["test"]
        else:
            jsonMode["Test"] = parseJson

        return jsonMode

    jsonFile = parse( yamlFile )

    #print ( jsonDump )
    with open ( outputJsonFilePath, mode = "w", encoding = "utf-8" ) as file:
        json.dump( jsonFile, file, indent = 4 )
        file.flush()




