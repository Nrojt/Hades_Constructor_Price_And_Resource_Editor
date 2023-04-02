"""
This script can replace the resource type and cost of the contractor. It does this by editing the ConditionalItemData.lua in the script's folder.
Please make a backup of the original file before running this script.
-Made by Nrojt
"""


def apply_changes(hades_directory, change_resource_value, change_resource_type, resource_input_value, resource_input_type):
    read_conditional_item_data = open(hades_directory + "\Content\Scripts\ConditionalItemData.lua", mode="r")
    conditional_item_data_list = read_conditional_item_data.readlines()
    if change_resource_value:
        for x in range(134, len(conditional_item_data_list)):
            if "ResourceCost" in conditional_item_data_list[x]:
                conditional_item_data_list[x] = "ResourceCost = " + str(resource_input_value) + ", \n"

    if change_resource_type:
        for x in range(134, len(conditional_item_data_list)):
            if "ResourceName" in conditional_item_data_list[x]:
                conditional_item_data_list[x] = "ResourceName = \"" + resource_input_type + "\", \n"

    read_conditional_item_data.close()

    writeConditionalItemData = open(hades_directory + "\Content\Scripts\ConditionalItemData.lua", mode="w")
    newFileContents = "".join(conditional_item_data_list)
    writeConditionalItemData.write(newFileContents)
    writeConditionalItemData.close()
    print("Succes")

    return None
