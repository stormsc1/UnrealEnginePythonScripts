import unreal

editorAssetLibraryPtr = unreal.EditorAssetLibrary()
assetList = editorAssetLibraryPtr.list_assets("/Game/", True, False)

for asset in assetList:
    references = editorAssetLibraryPtr.find_package_referencers_for_asset(asset, False)
    if len(references) == 0:
        print('Unused asset found: {path}'.format(path=asset))