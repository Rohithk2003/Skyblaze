import cx_Freeze

executables = [cx_Freeze.Executable("aircraft.py")]

cx_Freeze.setup(
    name="Jet Fighter",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["back.png","background.png","bullet.png","bullet1.png","cloud.png","cloud1.png","enemy.png","gameover.png","player.png","BUTTON.wav","crash.wav","Electro Fight - Kwon.mp3"]}},
    executables = executables

    )
