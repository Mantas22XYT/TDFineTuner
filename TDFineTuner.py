import subprocess
ver = "0.2.1"
print("TDFineTuner")
print("Version: " + ver)
print("Only enter the first 2 numbers. For example, if your version is 0.9.2, only write 0.9!")
gameVer = input("Please Enter your game version: ")
if gameVer == "0.9":
 print(gameVer + " is supported!")
elif gameVer == "0.8":
 print(gameVer + " may be supported, it may have not been tested")
else:
 print(gameVer + " is an invalid, or an unsupported version of the game.")
 exit()
renderValue = input("Renderscale (up to 200): ")
qualityValue = input("Quality (1=Low, 2=Medium, 3=High): ")
fovValue = input("FOV (up to 120): ")
gammaValue = input("Gamma: ")
dofValue = input("Depth of Field (0 = False, 1 = True): ")
barrelDistortValue = input("Barrel Distortion (0 = False, 1 = True): ")
with open('options.xml', 'w') as myfile:
    myfile.write(f'<registry version="0.9.2">\n')
    myfile.write(f'	<options>\n')
    myfile.write(f'		<display>\n')
    myfile.write(f'			<mode value="0"/>\n')
    myfile.write(f'			<resolution value="0"/>\n')
    myfile.write(f'		</display>\n')
    myfile.write(f'		<gfx>\n')
    myfile.write(f'			<renderscale value="{renderValue}"/>\n')
    myfile.write(f'			<quality value="{qualityValue}"/>\n')
    myfile.write(f'			<fov value="{fovValue}"/>\n')
    myfile.write(f'			<gamma value="{gammaValue}"/>\n')
    myfile.write(f'			<dof value="{dofValue}"/>\n')
    myfile.write(f'			<barrel value="0"/>\n')
    myfile.write(f'			<motionblur value="0"/>\n')
    myfile.write(f'			<vsync value="1"/>\n')
    myfile.write(f'		</gfx>\n')
    myfile.write(f'		<audio>\n')
    myfile.write(f'			<soundvolume value="1"/>\n')
    myfile.write(f'			<ambiencevolume value="50"/>\n')
    myfile.write(f'			<musicvolume value="1"/>\n')
    myfile.write(f'			<menumusic value="1"/>\n')
    myfile.write(f'		</audio>\n')
    myfile.write(f'		<input>\n')
    myfile.write(f'			<smoothing value="0"/>\n')
    myfile.write(f'			<sensitivity value="110"/>\n')
    myfile.write(f'			<invert value="0"/>\n')
    myfile.write(f'			<headbob value="70"/>\n')
    myfile.write(f'			<keymap>\n')
    myfile.write(f'				<forward value="w"/>\n')
    myfile.write(f'				<backward value="s"/>\n')
    myfile.write(f'				<left value="a"/>\n')
    myfile.write(f'				<right value="d"/>\n')
    myfile.write(f'				<flashlight value="f"/>\n')
    myfile.write(f'				<interact value="e"/>\n')
    myfile.write(f'				<jump value="space"/>\n')
    myfile.write(f'				<crouch value="ctrl"/>\n')
    myfile.write(f'			</keymap>\n')
    myfile.write(f'		</input>\n')
    myfile.write(f'		<game>\n')
    myfile.write(f'			<campaign>\n')
    myfile.write(f'				<ammo value="100"/>\n')
    myfile.write(f'				<health value="100"/>\n')
    myfile.write(f'			</campaign>\n')
    myfile.write(f'			<missionskipping value="1"/>\n')
    myfile.write(f'			<sandbox>\n')
    myfile.write(f'				<unlocklevels value="1"/>\n')
    myfile.write(f'				<unlocktools value="1"/>\n')
    myfile.write(f'			</sandbox>\n')
    myfile.write(f'		</game>\n')
    myfile.write(f'	</options>\n')
    myfile.write(f'</registry>\n')
    myfile.write(f'\n')
# %LOCALAPPDATA%\Teardown\ < SAVE LOCATION
subprocess.call([r'apply.bat'])
