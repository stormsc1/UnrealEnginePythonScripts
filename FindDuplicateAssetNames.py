import unreal
import os

editorAssetLibraryPtr = unreal.EditorAssetLibrary()
assetPathList = editorAssetLibraryPtr.list_assets("/Game/", True, False)
assetNameList = [os.path.split(assetPath)[1] for assetPath in assetPathList]
assetDuplicateList = []
ignoreList = []

for assetName in assetNameList:
    if assetName in ignoreList:
        continue
    indices = [index for index, element in enumerate(assetNameList) if element == assetName]
    if len(indices) > 1:
        assetDuplicateList += [indices]
    for i in indices:
        ignoreList += assetNameList[i]
        
for assetDuplicates in assetDuplicateList:
    print("Asset duplicates found:")
    for assetIndex in assetDuplicates:
        assetPath = assetPathList[assetIndex]
        referenceCount = len(editorAssetLibraryPtr.find_package_referencers_for_asset(assetPath, False))
        print(' - [References: {referenceCount}] {assetPath}'.format(referenceCount = referenceCount, assetPath=assetPath))