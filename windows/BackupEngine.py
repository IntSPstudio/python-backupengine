#|==============================================================|#
# Made by IntSPstudio
# Backup Engine
# Thank you for using this software!
# Version: 0.0.1.20161001
# ID: 980002002
#
# Twitter: @IntSPstudio
#|==============================================================|#

# USER INPUT URLS SET
# SOURCE -> DESTINATION
#
# SOURCE = FOLDER URL
# DESTINATION = BACKUP FOLDER NAME (CFD\DATE\DESTINATION)

#1
uiusBckS1name		 =""
uiusBckS1source 	 =""
uiusBckS1destination =""
#2
uiusBckS2name		 =""
uiusBckS2source 	 =""
uiusBckS2destination =""
#3
uiusBckS3name		 =""
uiusBckS3source 	 =""
uiusBckS3destination =""
#4
uiusBckS4name		 =""
uiusBckS4source 	 =""
uiusBckS4destination =""
#5
uiusBckS5name		 =""
uiusBckS5source 	 =""
uiusBckS5destination =""
#6
uiusBckS6name		 =""
uiusBckS6source 	 =""
uiusBckS6destination =""
#7
uiusBckS7name		 =""
uiusBckS7source 	 =""
uiusBckS7destination =""
#8
uiusBckS8name		 =""
uiusBckS8source 	 =""
uiusBckS8destination =""
#COM
uiusBckSCname		 =""
uiusBckSCdestination =""
uiusBckSCoptions	 ="/S"
#|==============================================================|#
#SYSTEM
import os
import sys
import time
import datetime

#DATE
clDateA = datetime.datetime.now()
clYear = clDateA.year
clMonth = clDateA.month
clDay = clDateA.day

#DMY
clDateB = str(clDay) +"."+ str(clMonth) +"."+ str(clYear)
#YMD
#clDateB = str(clYear)+"."+ str(clMonth)  +"."+ str(clDay)
#MDY
#clDateB = str(clMonth) +"."+ str(clDay) +"."+ str(clYear)

#CMD COLOR
os.system("color a")

#BACKGROUND
bgdLine = "----------------------------------------------------------------"
#BASIC VRB
continuity ="1"
mainPage ="0"
menuPage ="99"
startMainBackupPage ="9"
infoPage ="10"
exitPage ="11"
#DICTIONARY
#Start
dcnyStLineAA ="]"
dcnyStLineAB ="==" + dcnyStLineAA
dcnyStLineEA = dcnyStLineAB +" Select the number: "
dcnyStLineEI = dcnyStLineAB +" Press enter to return"
dcnyStLineEC ="Press enter to continue"
dcnyStLineEN = dcnyStLineAB +" Press enter to close"
#Selection
dcnySelectionMark ="x"
dcnySelectionClear =" "
#Activation
dcnyActivationTrue ="1"
dcnyActivationFalse ="0"
#Page title
dcnyMenuPageTitle ="Menu"
dcnyInfoPageTitle ="Info"
#Basic vrb
dcnyBasicActivations ="Activations"
dcnyBasicCode ="Code"
dcnyBasicDestination ="Destination"
dcnyBasicLog ="Log"
dcnyBasicLogs ="Logs"
dcnyBasicSource ="Source"
#SELECTION
uiusBckS1slct = dcnySelectionClear
uiusBckS2slct = dcnySelectionClear
uiusBckS3slct = dcnySelectionClear
uiusBckS4slct = dcnySelectionClear
uiusBckS5slct = dcnySelectionClear
uiusBckS6slct = dcnySelectionClear
uiusBckS7slct = dcnySelectionClear
uiusBckS8slct = dcnySelectionClear
#MENU ID
uiusBckS1mid ="1"
uiusBckS2mid ="2"
uiusBckS3mid ="3"
uiusBckS4mid ="4"
uiusBckS5mid ="5"
uiusBckS6mid ="6"
uiusBckS7mid ="7"
uiusBckS8mid ="8"
#BACKUP PERMISSION
backupPermissionTrue ="1"
backupPermissionFalse ="0"
backupPermission = backupPermissionFalse
uiusBckS1permission = backupPermissionFalse
uiusBckS2permission = backupPermissionFalse
uiusBckS3permission = backupPermissionFalse
uiusBckS4permission = backupPermissionFalse
uiusBckS5permission = backupPermissionFalse
uiusBckS6permission = backupPermissionFalse
uiusBckS7permission = backupPermissionFalse
uiusBckS8permission = backupPermissionFalse
#ACTIVATION
#1
if uiusBckS1name !="":
	uiusBckS1activation = dcnyActivationTrue
else:
	uiusBckS1activation = dcnyActivationFalse
#2
if uiusBckS2name !="":
	uiusBckS2activation = dcnyActivationTrue
else:
	uiusBckS2activation = dcnyActivationFalse
#3
if uiusBckS3name !="":
	uiusBckS3activation = dcnyActivationTrue
else:
	uiusBckS3activation = dcnyActivationFalse
#4
if uiusBckS4name !="":
	uiusBckS4activation = dcnyActivationTrue
else:
	uiusBckS4activation = dcnyActivationFalse
#5
if uiusBckS5name !="":
	uiusBckS5activation = dcnyActivationTrue
else:
	uiusBckS5activation = dcnyActivationFalse
#6
if uiusBckS6name !="":
	uiusBckS6activation = dcnyActivationTrue
else:
	uiusBckS6activation = dcnyActivationFalse
#7
if uiusBckS7name !="":
	uiusBckS7activation = dcnyActivationTrue
else:
	uiusBckS7activation = dcnyActivationFalse
#8
if uiusBckS8name !="":
	uiusBckS8activation = dcnyActivationTrue
else:
	uiusBckS8activation = dcnyActivationFalse
uiusBckSCactivation = uiusBckS1activation + uiusBckS2activation + uiusBckS3activation + uiusBckS4activation + uiusBckS5activation + uiusBckS6activation + uiusBckS7activation + uiusBckS8activation
#DESTINATION
#Date
#1
if uiusBckS1activation == dcnyActivationTrue:
	uiusBckS1destination = clDateB +"\\"+ uiusBckS1destination
#2
if uiusBckS2activation == dcnyActivationTrue:
	uiusBckS2destination = clDateB +"\\"+ uiusBckS2destination
#3
if uiusBckS3activation == dcnyActivationTrue:
	uiusBckS3destination = clDateB +"\\"+ uiusBckS3destination
#4
if uiusBckS4activation == dcnyActivationTrue:
	uiusBckS4destination = clDateB +"\\"+ uiusBckS4destination
#5
if uiusBckS5activation == dcnyActivationTrue:
	uiusBckS5destination = clDateB +"\\"+ uiusBckS5destination
#6
if uiusBckS6activation == dcnyActivationTrue:
	uiusBckS6destination = clDateB +"\\"+ uiusBckS6destination
#7
if uiusBckS7activation == dcnyActivationTrue:
	uiusBckS7destination = clDateB +"\\"+ uiusBckS7destination
#8
if uiusBckS8activation == dcnyActivationTrue:
	uiusBckS8destination = clDateB +"\\"+ uiusBckS8destination
#Com destination
if uiusBckSCdestination !="":
	#1
	if uiusBckS1activation == dcnyActivationTrue:
		uiusBckS1destination = uiusBckSCdestination +"\\"+ uiusBckS1destination
	#2
	if uiusBckS2activation == dcnyActivationTrue:
		uiusBckS2destination = uiusBckSCdestination +"\\"+ uiusBckS2destination
	#3
	if uiusBckS3activation == dcnyActivationTrue:
		uiusBckS3destination = uiusBckSCdestination +"\\"+ uiusBckS3destination
	#4
	if uiusBckS4activation == dcnyActivationTrue:
		uiusBckS4destination = uiusBckSCdestination +"\\"+ uiusBckS4destination
	#5
	if uiusBckS5activation == dcnyActivationTrue:
		uiusBckS5destination = uiusBckSCdestination +"\\"+ uiusBckS5destination
	#6
	if uiusBckS6activation == dcnyActivationTrue:
		uiusBckS6destination = uiusBckSCdestination +"\\"+ uiusBckS6destination
	#7
	if uiusBckS7activation == dcnyActivationTrue:
		uiusBckS7destination = uiusBckSCdestination +"\\"+ uiusBckS7destination
	#8
	if uiusBckS8activation == dcnyActivationTrue:
		uiusBckS8destination = uiusBckSCdestination +"\\"+ uiusBckS8destination
#CODE
dcnyCodeSTMA ="robocopy"
dcnyCodeLOGMA ="/LOG:"
dcnyCodeLOGFF =".txt"
uiusBckS1code =""
uiusBckS2code =""
uiusBckS3code =""
uiusBckS4code =""
uiusBckS5code =""
uiusBckS6code =""
uiusBckS7code =""
uiusBckS8code =""
#MAIN FOLDER
clMainFDurl = uiusBckSCdestination +"\\"+ clDateB
clMainFDcmd = "md "+ clMainFDurl
#LOG FOLDER
clLogFDurl = uiusBckSCdestination +"\\"+ "logs"
clLogFDcmd = "md "+ clLogFDurl
uiusBckS1logurl = clLogFDurl +"\\"+ uiusBckS1name + dcnyCodeLOGFF
uiusBckS2logurl = clLogFDurl +"\\"+ uiusBckS2name + dcnyCodeLOGFF
uiusBckS3logurl = clLogFDurl +"\\"+ uiusBckS3name + dcnyCodeLOGFF
uiusBckS4logurl = clLogFDurl +"\\"+ uiusBckS4name + dcnyCodeLOGFF
uiusBckS5logurl = clLogFDurl +"\\"+ uiusBckS5name + dcnyCodeLOGFF
uiusBckS6logurl = clLogFDurl +"\\"+ uiusBckS6name + dcnyCodeLOGFF
uiusBckS7logurl = clLogFDurl +"\\"+ uiusBckS7name + dcnyCodeLOGFF
uiusBckS8logurl = clLogFDurl +"\\"+ uiusBckS8name + dcnyCodeLOGFF
#INFO SCREEN
infoSampleCode = dcnyCodeSTMA +" "+ dcnyBasicSource +" "+ dcnyBasicDestination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ dcnyBasicLog + dcnyCodeLOGFF +'"'
#MENU LOOP
while continuity == "1":
	#SLOT 1
	if mainPage == uiusBckS1mid:
		if uiusBckS1activation == dcnyActivationTrue:
			if uiusBckS1slct != dcnySelectionClear:
				uiusBckS1slct = dcnySelectionClear
			else:
				uiusBckS1slct = dcnySelectionMark
		else:
			uiusBckS1slct = dcnySelectionClear
		mainPage = menuPage
	#SLOT 2
	elif mainPage == uiusBckS2mid:
		if uiusBckS2activation == dcnyActivationTrue:
			if uiusBckS2slct != dcnySelectionClear:
				uiusBckS2slct = dcnySelectionClear
			else:
				uiusBckS2slct = dcnySelectionMark
		else:
			uiusBckS2slct = dcnySelectionClear
		mainPage = menuPage
	#SLOT 3
	elif mainPage == uiusBckS3mid:
		if uiusBckS3activation == dcnyActivationTrue:
			if uiusBckS3slct != dcnySelectionClear:
				uiusBckS3slct = dcnySelectionClear
			else:
				uiusBckS3slct = dcnySelectionMark
		else:
			uiusBckS3slct = dcnySelectionClear
		mainPage = menuPage
	#SLOT 4
	elif mainPage == uiusBckS4mid:
		if uiusBckS4activation == dcnyActivationTrue:
			if uiusBckS4slct != dcnySelectionClear:
				uiusBckS4slct = dcnySelectionClear
			else:
				uiusBckS4slct = dcnySelectionMark
		else:
			uiusBckS4slct = dcnySelectionClear
		mainPage = menuPage
	#SLOT 5
	elif mainPage == uiusBckS5mid:
		if uiusBckS5activation == dcnyActivationTrue:
			if uiusBckS5slct != dcnySelectionClear:
				uiusBckS5slct = dcnySelectionClear
			else:
				uiusBckS5slct = dcnySelectionMark
		else:
			uiusBckS5slct = dcnySelectionClear
		mainPage = menuPage
	#SLOT 6
	elif mainPage == uiusBckS6mid:
		if uiusBckS6activation == dcnyActivationTrue:
			if uiusBckS6slct != dcnySelectionClear:
				uiusBckS6slct = dcnySelectionClear
			else:
				uiusBckS6slct = dcnySelectionMark
		else:
			uiusBckS6slct = dcnySelectionClear
		mainPage = menuPage
	#SLOT 7
	elif mainPage == uiusBckS7mid:
		if uiusBckS7activation == dcnyActivationTrue:
			if uiusBckS7slct != dcnySelectionClear:
				uiusBckS7slct = dcnySelectionClear
			else:
				uiusBckS7slct = dcnySelectionMark
		else:
			uiusBckS7slct = dcnySelectionClear
		mainPage = menuPage
	#SLOT 8
	elif mainPage == uiusBckS8mid:
		if uiusBckS8activation == dcnyActivationTrue:
			if uiusBckS8slct != dcnySelectionClear:
				uiusBckS8slct = dcnySelectionClear
			else:
				uiusBckS8slct = dcnySelectionMark
		else:
			uiusBckS8slct = dcnySelectionClear
		mainPage = menuPage


	#START BACKUP
	elif mainPage == startMainBackupPage:
		#TA
		os.system("cls")
		#TB
		if uiusBckS1activation == dcnyActivationTrue:
			if uiusBckS1slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS1permission = backupPermissionTrue
		if uiusBckS2activation == dcnyActivationTrue:
			if uiusBckS2slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS2permission = backupPermissionTrue
		if uiusBckS3activation == dcnyActivationTrue:
			if uiusBckS3slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS3permission = backupPermissionTrue
		if uiusBckS4activation == dcnyActivationTrue:
			if uiusBckS4slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS4permission = backupPermissionTrue
		if uiusBckS5activation == dcnyActivationTrue:
			if uiusBckS5slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS5permission = backupPermissionTrue
		if uiusBckS6activation == dcnyActivationTrue:
			if uiusBckS6slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS6permission = backupPermissionTrue
		if uiusBckS7activation == dcnyActivationTrue:
			if uiusBckS7slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS7permission = backupPermissionTrue
		if uiusBckS8activation == dcnyActivationTrue:
			if uiusBckS8slct == dcnySelectionMark:
				backupPermission = backupPermissionTrue
				uiusBckS8permission = backupPermissionTrue
		#TC
		if backupPermission == backupPermissionTrue:
			#TA
			print(bgdLine)
			#TB
			#1
			if uiusBckS1permission == backupPermissionTrue:
				uiusBckS1code = dcnyCodeSTMA +" "+ uiusBckS1source +" "+ uiusBckS1destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS1logurl +'"'
				print(uiusBckS1code)
			#2
			if uiusBckS2permission == backupPermissionTrue:
				uiusBckS2code = dcnyCodeSTMA +" "+ uiusBckS2source +" "+ uiusBckS2destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS2logurl +'"'
				print(uiusBckS2code)
			#3
			if uiusBckS3permission == backupPermissionTrue:
				uiusBckS3code = dcnyCodeSTMA +" "+ uiusBckS3source +" "+ uiusBckS3destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS3logurl +'"'
				print(uiusBckS3code)
			#4
			if uiusBckS4permission == backupPermissionTrue:
				uiusBckS4code = dcnyCodeSTMA +" "+ uiusBckS4source +" "+ uiusBckS4destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS4logurl +'"'
				print(uiusBckS4code)
			#5
			if uiusBckS5permission == backupPermissionTrue:
				uiusBckS5code = dcnyCodeSTMA +" "+ uiusBckS5source +" "+ uiusBckS5destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS5logurl +'"'
				print(uiusBckS5code)
			#6
			if uiusBckS6permission == backupPermissionTrue:
				uiusBckS6code = dcnyCodeSTMA +" "+ uiusBckS6source +" "+ uiusBckS6destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS6logurl +'"'
				print(uiusBckS6code)
			#7
			if uiusBckS7permission == backupPermissionTrue:
				uiusBckS7code = dcnyCodeSTMA +" "+ uiusBckS7source +" "+ uiusBckS7destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS7logurl +'"'
				print(uiusBckS7code)
			#8
			if uiusBckS8permission == backupPermissionTrue:
				uiusBckS8code = dcnyCodeSTMA +" "+ uiusBckS8source +" "+ uiusBckS8destination +" "+ uiusBckSCoptions +" "+ dcnyCodeLOGMA +'"'+ uiusBckS8logurl +'"'
				print(uiusBckS8code)
			#TC
			#Continue
			wtmn =input(dcnyStLineEC)
			backupStartTime = datetime.datetime.now()
			#Main folders
			os.system(clMainFDcmd)
			os.system(clLogFDcmd)
			#TD
			#1
			if uiusBckS1permission == backupPermissionTrue:
				#print(uiusBckS1name)
				os.system(uiusBckS1code)
			#2
			if uiusBckS2permission == backupPermissionTrue:
				#print(uiusBckS2name)
				os.system(uiusBckS2code)
			#3
			if uiusBckS3permission == backupPermissionTrue:
				#print(uiusBckS3name)
				os.system(uiusBckS3code)
			#4
			if uiusBckS4permission == backupPermissionTrue:
				#print(uiusBckS4name)
				os.system(uiusBckS4code)
			#5
			if uiusBckS5permission == backupPermissionTrue:
				#print(uiusBckS5name)
				os.system(uiusBckS5code)
			#6
			if uiusBckS6permission == backupPermissionTrue:
				#print(uiusBckS6name)
				os.system(uiusBckS6code)
			#7
			if uiusBckS7permission == backupPermissionTrue:
				#print(uiusBckS7name)
				os.system(uiusBckS7code)
			#8
			if uiusBckS8permission == backupPermissionTrue:
				#print(uiusBckS8name)
				os.system(uiusBckS8code)
			#TE
			backupStopTime = datetime.datetime.now()
			backupDuration = backupStopTime - backupStartTime
			StA = str(backupStartTime.hour)
			StB = str(backupStartTime.minute)
			SpA = str(backupStopTime.hour)
			SpB = str(backupStopTime.minute)
			time.sleep(1)
			os.system("cls")
			#TF
			print(bgdLine)
			print(dcnyStLineAB)
			print("  "+ dcnyStLineAA)
			print("  "+ dcnyStLineAA, "Start:", StA +":"+ StB)
			print("  "+ dcnyStLineAA, "Stop:", SpA +":"+ SpB)
			print("  "+ dcnyStLineAA, "Duration:", backupDuration)
			print("  "+ dcnyStLineAA)
			#TG
			wtmn =input(dcnyStLineEN)
		else:
			#TA
			print(bgdLine)
			print(dcnyStLineAB)
			print("  "+ dcnyStLineAA)
			print("  "+ dcnyStLineAA, "Check the settings")
			print("  "+ dcnyStLineAA)
			print(dcnyStLineAB)
			time.sleep(2)
		#TD
		continuity ="0"
	#INFO
	elif mainPage == infoPage:
		#TA
		os.system("cls")
		#TB
		print(bgdLine)
		print(dcnyStLineAB, dcnyInfoPageTitle)
		print("  "+ dcnyStLineAA)
		print("  "+ dcnyStLineAA, dcnyBasicDestination +":", clMainFDurl)
		print("  "+ dcnyStLineAA, dcnyBasicLogs +":", clLogFDurl)
		print("  "+ dcnyStLineAA, dcnyBasicCode +":", infoSampleCode)
		print("  "+ dcnyStLineAA, dcnyBasicActivations +":", uiusBckSCactivation)
		print("  "+ dcnyStLineAA)
		#1
		if uiusBckS1activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS1name +":")
			print("  "+ dcnyStLineAA, uiusBckS1source)
			print("  "+ dcnyStLineAA, uiusBckS1destination)
		#2
		if uiusBckS2activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS2name +":")
			print("  "+ dcnyStLineAA, uiusBckS2source)
			print("  "+ dcnyStLineAA, uiusBckS2destination)
		#3
		if uiusBckS3activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS3name +":")
			print("  "+ dcnyStLineAA, uiusBckS3source)
			print("  "+ dcnyStLineAA, uiusBckS3destination)
		#4
		if uiusBckS4activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS4name +":")
			print("  "+ dcnyStLineAA, uiusBckS4source)
			print("  "+ dcnyStLineAA, uiusBckS4destination)
		#5
		if uiusBckS5activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS5name +":")
			print("  "+ dcnyStLineAA, uiusBckS5source)
			print("  "+ dcnyStLineAA, uiusBckS5destination)
		#6
		if uiusBckS6activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS6name +":")
			print("  "+ dcnyStLineAA, uiusBckS6source)
			print("  "+ dcnyStLineAA, uiusBckS6destination)
		#7
		if uiusBckS7activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS7name +":")
			print("  "+ dcnyStLineAA, uiusBckS7source)
			print("  "+ dcnyStLineAA, uiusBckS7destination)
		#8
		if uiusBckS8activation == dcnyActivationTrue:
			print("  "+ dcnyStLineAA, uiusBckS8name +":")
			print("  "+ dcnyStLineAA, uiusBckS8source)
			print("  "+ dcnyStLineAA, uiusBckS8destination)
		print("  "+ dcnyStLineAA)
		#TC
		wtmn =input(dcnyStLineEI)
		mainPage = menuPage
	#EXIT
	elif mainPage == exitPage:
		#TA
		#os.system("cls")
		#TB
		continuity ="0"
	#MENU
	else:
		#TA
		os.system("cls")
		#TB
		print(bgdLine)
		print(dcnyStLineAB, dcnyMenuPageTitle, "-", clDateB)
		print("  "+ dcnyStLineAA)
		print(" 1"+dcnyStLineAA, uiusBckS1name, uiusBckS1slct)
		print(" 2"+dcnyStLineAA, uiusBckS2name, uiusBckS2slct)
		print(" 3"+dcnyStLineAA, uiusBckS3name, uiusBckS3slct)
		print(" 4"+dcnyStLineAA, uiusBckS4name, uiusBckS4slct)
		print(" 5"+dcnyStLineAA, uiusBckS5name, uiusBckS5slct)
		print(" 6"+dcnyStLineAA, uiusBckS6name, uiusBckS6slct)
		print(" 7"+dcnyStLineAA, uiusBckS7name, uiusBckS7slct)
		print(" 8"+dcnyStLineAA, uiusBckS8name, uiusBckS8slct)
		print("", startMainBackupPage + dcnyStLineAA, "Start backup")
		print(infoPage + dcnyStLineAA, "Info")
		print(exitPage + dcnyStLineAA, "Exit")
		print("  "+ dcnyStLineAA)
		#TC
		mainPage =input(dcnyStLineEA)
#END OF MENU LOOP

#TA
os.system("cls")