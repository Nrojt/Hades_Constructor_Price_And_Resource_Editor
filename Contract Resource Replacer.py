from math import *
'''
This script can replace the resource type and cost of the contractor. It does this by editing the ConditionalItemData.lua in the scripts folder.
Please make a backup of the original file before running this script.
-Made by Nrojt
'''
resourceInputValue = 0
changeResourceValue = False


hadesDirectory = str(input("Hades directory (for example C:\Program Files (x86)\Steam\steamapps\common\Hades): "))

changeResourceValue = str(input("Do you want to overwrite resource values?: "))

if changeResourceValue.lower() == "yes" or changeResourceValue.lower() == "y" or changeResourceValue.lower() == "true":
    changeResourceValue = True
    resourceInputValue = abs(int(input("Value to change the ResourceCost with: ")))
else:
    changeResourceValue = False

resourceTypes = {"Gems", "SuperGems", "MetaPoints", "GiftPoints", "LockKeys", "SuperLockKeys", "SuperGiftPoints"}
resourceInputType = "Gems"
changeResourceType = str(input("Overwrite resource types?: "))
if changeResourceType.lower() == "yes" or changeResourceType.lower() == "y" or changeResourceType.lower() == "true":
    changeResourceType = True
    resourceInputType = str(input(
        "Resource type, choose from [Gems SuperGems MetaPoints GiftPoints LockKeys SuperLockKeys SuperGiftPoints]: "))
    while resourceInputType not in resourceTypes:
        resourceInputType = str(
            input("Choose from [Gems SuperGems MetaPoints GiftPoints LockKeys SuperLockKeys SuperGiftPoints]: "))
else:
    changeResourceType = False

readConditionalItemData = open(hadesDirectory + "\Content\Scripts\ConditionalItemData.lua", mode="r")
conditionalItemDataList = readConditionalItemData.readlines()
if changeResourceValue:
    for x in range(134, len(conditionalItemDataList)):
        if "ResourceCost" in conditionalItemDataList[x]:
            conditionalItemDataList[x] = "ResourceCost = " + str(resourceInputValue) + ", \n"

if changeResourceType:
    for x in range(134, len(conditionalItemDataList)):
        if "ResourceName" in conditionalItemDataList[x]:
            conditionalItemDataList[x] = "ResourceName = \"" + resourceInputType + "\", \n"

readConditionalItemData.close()

writeConditionalItemData = open(hadesDirectory + "\Content\Scripts\ConditionalItemData.lua", mode="w")
newFileContents = "".join(conditionalItemDataList)
writeConditionalItemData.write(newFileContents)
writeConditionalItemData.close()
print("Succes")