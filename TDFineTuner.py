import subprocess
ver = "0.1.0_b1"
print("TDFineTuner DEMO")
print("Version: " + ver)
print("")
print("Warning! This is an early version and has a lot of limitations!"
print("Currently it only applies the lowest in-game settings."
print("Only enter the first 2 numbers. For example, if your version is 0.9.2, only write 0.9!")
gameVer = input("Please Enter your game version: ")
if gameVer == "0.9":
 print(gameVer + " is supported!")
elif gameVer == "0.8":
 print(gameVer + " may be supported, it may have not been tested")
else:
 print(gameVer + " is an invalid, or an unsupported version of the game.")
 exit()
# %LOCALAPPDATA%\Teardown\ < SAVE LOCATION
subprocess.call([r'apply.bat'])
