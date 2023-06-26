
import cx_Freeze
executables = [
    cx_Freeze.Executable(script="main.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "SpaceMaker",
    options = {
        "build_exe":{
            "packages": ["main"],
            "include_files":["bg.jpg",
                            "space.png",
                            "Space_Machine_Power.mp3"]
        }
    } , executables = executables
    
) 
# python geraSetup.py build
# python geraSetup.py bdist_msi