EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 3 5
Title "Airhockey Control Board"
Date "2021-11-05"
Rev "A"
Comp "Olin Electric Motorsports"
Comment1 "Designer: Wesley Soo-Hoo"
Comment2 "Principles of Integrated Engineering"
Comment3 ""
Comment4 ""
$EndDescr
NoConn ~ 2650 2600
Text Label 2550 2450 1    60   ~ 0
IOREF
Text Label 2200 2450 1    60   ~ 0
Vin
Text Label 2200 3700 0    60   ~ 0
A0
Text Label 2200 3800 0    60   ~ 0
A1
Text Label 2200 3900 0    60   ~ 0
A2
Text Label 2200 4000 0    60   ~ 0
A3
Text Label 2200 4100 0    60   ~ 0
A4
Text Label 2200 4200 0    60   ~ 0
A5
Text Label 2200 4300 0    60   ~ 0
A6
Text Label 2200 4400 0    60   ~ 0
A7
Text Label 2200 4650 0    60   ~ 0
A8
Text Label 2200 4750 0    60   ~ 0
A9
Text Label 2200 4850 0    60   ~ 0
A10
Text Label 2200 4950 0    60   ~ 0
A11
Text Label 2200 5050 0    60   ~ 0
A12
Text Label 2200 5150 0    60   ~ 0
A13
Text Label 2200 5250 0    60   ~ 0
A14
Text Label 2200 5350 0    60   ~ 0
A15
Text Label 9000 2700 1    60   ~ 0
22
Text Label 8900 2700 1    60   ~ 0
24
Text Label 8800 2700 1    60   ~ 0
26
Text Label 8700 2700 1    60   ~ 0
28
Text Label 8600 2700 1    60   ~ 0
30
Text Label 8500 2700 1    60   ~ 0
32
Text Label 8400 2700 1    60   ~ 0
34
Text Label 8300 2700 1    60   ~ 0
36
Text Label 8200 2700 1    60   ~ 0
38
Text Label 8100 2700 1    60   ~ 0
40
Text Label 8000 2700 1    60   ~ 0
42
Text Label 7900 2700 1    60   ~ 0
44
Text Label 7800 2700 1    60   ~ 0
46
Text Label 7700 2700 1    60   ~ 0
48
Text Label 7600 2700 1    60   ~ 0
50(MISO)
Text Label 7500 2700 1    60   ~ 0
52(SCK)
Text Label 9000 3700 1    60   ~ 0
23
Text Label 8900 3700 1    60   ~ 0
25
Text Label 8800 3700 1    60   ~ 0
27
Text Label 8600 3700 1    60   ~ 0
31
Text Label 8700 3700 1    60   ~ 0
29
Text Label 8500 3700 1    60   ~ 0
33
Text Label 8400 3700 1    60   ~ 0
35
Text Label 8300 3700 1    60   ~ 0
37
Text Label 8200 3700 1    60   ~ 0
39
Text Label 8100 3700 1    60   ~ 0
41
Text Label 8000 3700 1    60   ~ 0
43
Text Label 7900 3700 1    60   ~ 0
45
Text Label 7800 3700 1    60   ~ 0
47
Text Label 7700 3700 1    60   ~ 0
49
Text Label 7600 3800 1    60   ~ 0
51(MOSI)
Text Label 7500 3800 1    60   ~ 0
53(SS)
Text Label 4050 5350 0    60   ~ 0
21(SCL)
Text Label 4050 5250 0    60   ~ 0
20(SDA)
Text Label 4050 5150 0    60   ~ 0
19(Rx1)
Text Label 4050 5050 0    60   ~ 0
18(Tx1)
Text Label 4050 4950 0    60   ~ 0
17(Rx2)
Text Label 4050 4850 0    60   ~ 0
16(Tx2)
Text Label 4050 4750 0    60   ~ 0
15(Rx3)
Text Label 4050 4650 0    60   ~ 0
14(Tx3)
Text Label 4050 2800 0    60   ~ 0
13(**)
Text Label 4050 2900 0    60   ~ 0
12(**)
Text Label 4050 3000 0    60   ~ 0
11(**)
Text Label 4050 3100 0    60   ~ 0
10(**)
Text Label 4050 3200 0    60   ~ 0
9(**)
Text Label 4050 3300 0    60   ~ 0
8(**)
Text Label 4050 3700 0    60   ~ 0
7(**)
Text Label 4050 3800 0    60   ~ 0
6(**)
Text Label 4050 3900 0    60   ~ 0
5(**)
Text Label 4050 4000 0    60   ~ 0
4(**)
Text Label 4050 4100 0    60   ~ 0
3(**)
Text Label 4050 4200 0    60   ~ 0
2(**)
Text Label 4050 4300 0    60   ~ 0
1(Tx0)
Text Label 4050 4400 0    60   ~ 0
0(Rx0)
Text Label 4050 2500 0    60   ~ 0
SDA
Text Label 4050 2400 0    60   ~ 0
SCL
Text Label 4050 2600 0    60   ~ 0
AREF
Text Notes 1675 1825 0    60   ~ 0
Shield for Arduino Mega Rev 3
$Comp
L Connector_Generic:Conn_01x08 P?
U 1 1 618913BE
P 2850 2900
AR Path="/618913BE" Ref="P?"  Part="1" 
AR Path="/6187679E/618913BE" Ref="P2"  Part="1" 
F 0 "P2" H 2850 3300 50  0000 C CNN
F 1 "Power" V 2950 2900 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 2850 2900 50  0001 C CNN
F 3 "" H 2850 2900 50  0000 C CNN
	1    2850 2900
	1    0    0    -1  
$EndComp
Text Notes 2950 2600 0    60   ~ 0
1
$Comp
L power:+3V3 #PWR?
U 1 1 618913C5
P 2400 2450
AR Path="/618913C5" Ref="#PWR?"  Part="1" 
AR Path="/6187679E/618913C5" Ref="#PWR022"  Part="1" 
F 0 "#PWR022" H 2400 2300 50  0001 C CNN
F 1 "+3.3V" V 2400 2700 50  0000 C CNN
F 2 "" H 2400 2450 50  0000 C CNN
F 3 "" H 2400 2450 50  0000 C CNN
	1    2400 2450
	1    0    0    -1  
$EndComp
Text Label 1900 2800 0    60   ~ 0
Reset
$Comp
L power:+5V #PWR?
U 1 1 618913CC
P 2300 2300
AR Path="/618913CC" Ref="#PWR?"  Part="1" 
AR Path="/6187679E/618913CC" Ref="#PWR021"  Part="1" 
F 0 "#PWR021" H 2300 2150 50  0001 C CNN
F 1 "+5V" V 2300 2500 50  0000 C CNN
F 2 "" H 2300 2300 50  0000 C CNN
F 3 "" H 2300 2300 50  0000 C CNN
	1    2300 2300
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 618913D2
P 2550 3400
AR Path="/618913D2" Ref="#PWR?"  Part="1" 
AR Path="/6187679E/618913D2" Ref="#PWR023"  Part="1" 
F 0 "#PWR023" H 2550 3150 50  0001 C CNN
F 1 "GND" H 2550 3250 50  0000 C CNN
F 2 "" H 2550 3400 50  0000 C CNN
F 3 "" H 2550 3400 50  0000 C CNN
	1    2550 3400
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x10 P?
U 1 1 618913D8
P 3600 2800
AR Path="/618913D8" Ref="P?"  Part="1" 
AR Path="/6187679E/618913D8" Ref="P5"  Part="1" 
F 0 "P5" H 3600 3300 50  0000 C CNN
F 1 "PWM" V 3700 2800 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x10" H 3600 2800 50  0001 C CNN
F 3 "" H 3600 2800 50  0000 C CNN
	1    3600 2800
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 618913DE
P 3900 3400
AR Path="/618913DE" Ref="#PWR?"  Part="1" 
AR Path="/6187679E/618913DE" Ref="#PWR024"  Part="1" 
F 0 "#PWR024" H 3900 3150 50  0001 C CNN
F 1 "GND" H 3900 3250 50  0000 C CNN
F 2 "" H 3900 3400 50  0000 C CNN
F 3 "" H 3900 3400 50  0000 C CNN
	1    3900 3400
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P?
U 1 1 618913E4
P 2850 4000
AR Path="/618913E4" Ref="P?"  Part="1" 
AR Path="/6187679E/618913E4" Ref="P3"  Part="1" 
F 0 "P3" H 2850 4400 50  0000 C CNN
F 1 "Analog" V 2950 4000 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 2850 4000 50  0001 C CNN
F 3 "" H 2850 4000 50  0000 C CNN
	1    2850 4000
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P?
U 1 1 618913EA
P 3600 4000
AR Path="/618913EA" Ref="P?"  Part="1" 
AR Path="/6187679E/618913EA" Ref="P6"  Part="1" 
F 0 "P6" H 3600 4400 50  0000 C CNN
F 1 "PWM" V 3700 4000 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 3600 4000 50  0001 C CNN
F 3 "" H 3600 4000 50  0000 C CNN
	1    3600 4000
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P?
U 1 1 618913F0
P 2850 4950
AR Path="/618913F0" Ref="P?"  Part="1" 
AR Path="/6187679E/618913F0" Ref="P4"  Part="1" 
F 0 "P4" H 2850 5350 50  0000 C CNN
F 1 "Analog" V 2950 4950 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 2850 4950 50  0001 C CNN
F 3 "" H 2850 4950 50  0000 C CNN
	1    2850 4950
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P?
U 1 1 618913F6
P 3600 4950
AR Path="/618913F6" Ref="P?"  Part="1" 
AR Path="/6187679E/618913F6" Ref="P7"  Part="1" 
F 0 "P7" H 3600 5350 50  0000 C CNN
F 1 "Communication" V 3700 4950 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 3600 4950 50  0001 C CNN
F 3 "" H 3600 4950 50  0000 C CNN
	1    3600 4950
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x18_Odd_Even P?
U 1 1 618913FC
P 8200 3100
AR Path="/618913FC" Ref="P?"  Part="1" 
AR Path="/6187679E/618913FC" Ref="P1"  Part="1" 
F 0 "P1" H 8200 4050 50  0000 C CNN
F 1 "Digital" V 8200 3100 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_2x18" H 8200 2050 50  0001 C CNN
F 3 "" H 8200 2050 50  0000 C CNN
	1    8200 3100
	0    -1   1    0   
$EndComp
Wire Wire Line
	2400 2450 2400 2900
Wire Wire Line
	2550 2700 2550 2450
Wire Wire Line
	2650 2700 2550 2700
Wire Wire Line
	2400 2900 2650 2900
Wire Wire Line
	2300 2300 2300 3000
Wire Wire Line
	2300 3000 2650 3000
Wire Wire Line
	2650 3300 2200 3300
Wire Wire Line
	2200 3300 2200 2450
Wire Wire Line
	1900 2800 2650 2800
Wire Wire Line
	2650 3100 2550 3100
Wire Wire Line
	2550 3100 2550 3200
Wire Wire Line
	2550 3200 2550 3400
Wire Wire Line
	2650 3200 2550 3200
Connection ~ 2550 3200
Wire Wire Line
	3800 2400 4050 2400
Wire Wire Line
	4050 2500 3800 2500
Wire Wire Line
	3800 2600 4050 2600
Wire Wire Line
	3900 3400 3900 2700
Wire Wire Line
	3900 2700 3800 2700
Wire Wire Line
	2650 3700 2200 3700
Wire Wire Line
	2200 3800 2650 3800
Wire Wire Line
	2650 3900 2200 3900
Wire Wire Line
	2200 4000 2650 4000
Wire Wire Line
	2650 4100 2200 4100
Wire Wire Line
	2200 4200 2650 4200
Wire Wire Line
	2650 4300 2200 4300
Wire Wire Line
	2200 4400 2650 4400
Wire Wire Line
	4050 4300 3800 4300
Wire Wire Line
	3800 4400 4050 4400
Wire Wire Line
	2650 4650 2200 4650
Wire Wire Line
	2200 4750 2650 4750
Wire Wire Line
	2650 4850 2200 4850
Wire Wire Line
	2200 4950 2650 4950
Wire Wire Line
	2650 5050 2200 5050
Wire Wire Line
	2200 5150 2650 5150
Wire Wire Line
	2650 5250 2200 5250
Wire Wire Line
	2200 5350 2650 5350
Wire Wire Line
	4050 4650 3800 4650
Wire Wire Line
	3800 4750 4050 4750
Wire Wire Line
	4050 4850 3800 4850
Wire Wire Line
	3800 4950 4050 4950
Wire Wire Line
	4050 5050 3800 5050
Wire Wire Line
	3800 5150 4050 5150
Wire Wire Line
	4050 5250 3800 5250
Wire Wire Line
	3800 5350 4050 5350
Wire Wire Line
	7800 2900 7800 2700
Wire Wire Line
	7700 2900 7700 2700
Wire Wire Line
	7600 2900 7600 2700
Wire Wire Line
	7500 2900 7500 2700
Wire Wire Line
	7800 3400 7800 3700
Wire Wire Line
	7700 3400 7700 3700
Wire Wire Line
	7600 3400 7600 3800
Wire Wire Line
	7500 3400 7500 3800
Wire Wire Line
	7400 2900 7150 2900
$Comp
L power:GND #PWR?
U 1 1 61891460
P 7150 3800
AR Path="/61891460" Ref="#PWR?"  Part="1" 
AR Path="/6187679E/61891460" Ref="#PWR025"  Part="1" 
F 0 "#PWR025" H 7150 3550 50  0001 C CNN
F 1 "GND" H 7150 3650 50  0000 C CNN
F 2 "" H 7150 3800 50  0000 C CNN
F 3 "" H 7150 3800 50  0000 C CNN
	1    7150 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	7400 3400 7150 3400
Connection ~ 7150 3400
Wire Wire Line
	9250 3400 9100 3400
Wire Wire Line
	9250 2900 9100 2900
$Comp
L power:+5V #PWR?
U 1 1 6189146A
P 9250 2600
AR Path="/6189146A" Ref="#PWR?"  Part="1" 
AR Path="/6187679E/6189146A" Ref="#PWR026"  Part="1" 
F 0 "#PWR026" H 9250 2450 50  0001 C CNN
F 1 "+5V" H 9250 2740 50  0000 C CNN
F 2 "" H 9250 2600 50  0000 C CNN
F 3 "" H 9250 2600 50  0000 C CNN
	1    9250 2600
	1    0    0    -1  
$EndComp
Connection ~ 9250 2900
Wire Wire Line
	9250 2600 9250 2900
Wire Wire Line
	9250 2900 9250 3400
Wire Wire Line
	7150 2900 7150 3400
Wire Wire Line
	7150 3400 7150 3800
Text GLabel 9000 2250 1    40   Input ~ 0
~MOT0_EN
Text GLabel 8900 2250 1    50   Input ~ 0
MOT0_STEP
Text GLabel 8800 2250 1    50   Input ~ 0
MOT0_DIR
Text GLabel 8700 2250 1    50   Input ~ 0
MOT0_MS1
Text GLabel 8600 2250 1    50   Input ~ 0
MOT0_MS2
Text GLabel 8500 2250 1    50   Input ~ 0
MOT0_MS3
Text GLabel 8400 2250 1    40   Input ~ 0
~MOT1_EN
Text GLabel 8300 2250 1    50   Input ~ 0
MOT1_STEP
Text GLabel 8200 2250 1    50   Input ~ 0
MOT1_DIR
Text GLabel 8100 2250 1    50   Input ~ 0
MOT1_MS1
Text GLabel 8000 2250 1    50   Input ~ 0
MOT1_MS2
Text GLabel 7900 2250 1    50   Input ~ 0
MOT1_MS3
Text GLabel 8500 3800 3    40   Input ~ 0
~MOT2_EN
Text GLabel 8600 3800 3    50   Input ~ 0
MOT2_STEP
Text GLabel 8700 3800 3    50   Input ~ 0
MOT2_DIR
Text GLabel 8800 3800 3    50   Input ~ 0
MOT2_MS1
Text GLabel 8900 3800 3    50   Input ~ 0
MOT2_MS2
Text GLabel 9000 3800 3    50   Input ~ 0
MOT2_MS3
Wire Wire Line
	9000 2250 9000 2900
Wire Wire Line
	8900 2250 8900 2900
Wire Wire Line
	8800 2250 8800 2900
Wire Wire Line
	8700 2250 8700 2900
Wire Wire Line
	8600 2250 8600 2900
Wire Wire Line
	8500 2250 8500 2900
Wire Wire Line
	8400 2250 8400 2900
Wire Wire Line
	8300 2250 8300 2900
Wire Wire Line
	8200 2250 8200 2900
Wire Wire Line
	8100 2250 8100 2900
Wire Wire Line
	8000 2250 8000 2900
Wire Wire Line
	7900 2250 7900 2900
Text GLabel 7900 3800 3    40   Input ~ 0
~MOT3_EN
Text GLabel 8000 3800 3    50   Input ~ 0
MOT3_STEP
Text GLabel 8100 3800 3    50   Input ~ 0
MOT3_DIR
Text GLabel 8200 3800 3    50   Input ~ 0
MOT3_MS1
Text GLabel 8300 3800 3    50   Input ~ 0
MOT3_MS2
Text GLabel 8400 3800 3    50   Input ~ 0
MOT3_MS3
Wire Wire Line
	8100 3400 8100 3800
Wire Wire Line
	8000 3400 8000 3800
Wire Wire Line
	7900 3400 7900 3800
Wire Wire Line
	8200 3400 8200 3800
Wire Wire Line
	8300 3400 8300 3800
Wire Wire Line
	8400 3400 8400 3800
Wire Wire Line
	8500 3400 8500 3800
Wire Wire Line
	8600 3400 8600 3800
Wire Wire Line
	8700 3400 8700 3800
Wire Wire Line
	8800 3400 8800 3800
Wire Wire Line
	8900 3400 8900 3800
Wire Wire Line
	9000 3400 9000 3800
Text GLabel 4400 4200 2    50   Input ~ 0
MOT0_SWITCH_FW
Text GLabel 4400 4000 2    50   Input ~ 0
MOT1_SWITCH_FW
Text GLabel 4400 3800 2    50   Input ~ 0
MOT2_SWITCH_FW
Text GLabel 4400 3300 2    50   Input ~ 0
MOT3_SWITCH_FW
Text GLabel 4400 4100 2    50   Input ~ 0
MOT0_SWITCH_BW
Text GLabel 4400 3900 2    50   Input ~ 0
MOT1_SWITCH_BW
Text GLabel 4400 3700 2    50   Input ~ 0
MOT2_SWITCH_BW
Text GLabel 4400 3200 2    50   Input ~ 0
MOT3_SWITCH_BW
Wire Wire Line
	3800 3200 4400 3200
Wire Wire Line
	3800 3300 4400 3300
Wire Wire Line
	3800 3700 4400 3700
Wire Wire Line
	3800 3800 4400 3800
Wire Wire Line
	3800 3900 4400 3900
Wire Wire Line
	3800 4000 4400 4000
Wire Wire Line
	3800 4100 4400 4100
Text GLabel 4400 3100 2    50   Input ~ 0
PWR_SW
Wire Wire Line
	3800 3100 4400 3100
Text GLabel 4400 3000 2    50   Input ~ 0
PWR_ON_OUTPUT
Wire Wire Line
	3800 3000 4400 3000
Wire Wire Line
	3800 4200 4400 4200
Text GLabel 4400 2900 2    50   Input ~ 0
UI_SWITCH_0
Text GLabel 4400 2800 2    50   Input ~ 0
UI_SWITCH_1
Wire Wire Line
	3800 2800 4400 2800
Wire Wire Line
	3800 2900 4400 2900
$EndSCHEMATC
