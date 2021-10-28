EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr B 17000 11000
encoding utf-8
Sheet 1 1
Title "Air Hockey Robot Control Board"
Date "2021-10-27"
Rev "A"
Comp "Olin College of Engineering"
Comment1 "Designer: Wesley Soo-Hoo"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
NoConn ~ 14650 1350
Text Label 14550 1200 1    60   ~ 0
IOREF
Text Label 14200 1200 1    60   ~ 0
Vin
Text Label 14200 2450 0    60   ~ 0
A0
Text Label 14200 2550 0    60   ~ 0
A1
Text Label 14200 2650 0    60   ~ 0
A2
Text Label 14200 2750 0    60   ~ 0
A3
Text Label 14200 2850 0    60   ~ 0
A4
Text Label 14200 2950 0    60   ~ 0
A5
Text Label 14200 3050 0    60   ~ 0
A6
Text Label 14200 3150 0    60   ~ 0
A7
Text Label 14200 3400 0    60   ~ 0
A8
Text Label 14200 3500 0    60   ~ 0
A9
Text Label 14200 3600 0    60   ~ 0
A10
Text Label 14200 3700 0    60   ~ 0
A11
Text Label 14200 3800 0    60   ~ 0
A12
Text Label 14200 3900 0    60   ~ 0
A13
Text Label 14200 4000 0    60   ~ 0
A14
Text Label 14200 4100 0    60   ~ 0
A15
Text Label 15800 4650 1    60   ~ 0
22
Text Label 15700 4650 1    60   ~ 0
24
Text Label 15600 4650 1    60   ~ 0
26
Text Label 15500 4650 1    60   ~ 0
28
Text Label 15400 4650 1    60   ~ 0
30
Text Label 15300 4650 1    60   ~ 0
32
Text Label 15200 4650 1    60   ~ 0
34
Text Label 15100 4650 1    60   ~ 0
36
Text Label 15000 4650 1    60   ~ 0
38
Text Label 14900 4650 1    60   ~ 0
40
Text Label 14800 4650 1    60   ~ 0
42
Text Label 14700 4650 1    60   ~ 0
44
Text Label 14600 4650 1    60   ~ 0
46
Text Label 14500 4650 1    60   ~ 0
48
Text Label 14400 4650 1    60   ~ 0
50(MISO)
Text Label 14300 4650 1    60   ~ 0
52(SCK)
Text Label 15800 5650 1    60   ~ 0
23
Text Label 15700 5650 1    60   ~ 0
25
Text Label 15600 5650 1    60   ~ 0
27
Text Label 15400 5650 1    60   ~ 0
31
Text Label 15500 5650 1    60   ~ 0
29
Text Label 15300 5650 1    60   ~ 0
33
Text Label 15200 5650 1    60   ~ 0
35
Text Label 15100 5650 1    60   ~ 0
37
Text Label 15000 5650 1    60   ~ 0
39
Text Label 14900 5650 1    60   ~ 0
41
Text Label 14800 5650 1    60   ~ 0
43
Text Label 14700 5650 1    60   ~ 0
45
Text Label 14600 5650 1    60   ~ 0
47
Text Label 14500 5650 1    60   ~ 0
49
Text Label 14400 5750 1    60   ~ 0
51(MOSI)
Text Label 14300 5750 1    60   ~ 0
53(SS)
Text Label 15700 4100 0    60   ~ 0
21(SCL)
Text Label 15700 4000 0    60   ~ 0
20(SDA)
Text Label 15700 3900 0    60   ~ 0
19(Rx1)
Text Label 15700 3800 0    60   ~ 0
18(Tx1)
Text Label 15700 3700 0    60   ~ 0
17(Rx2)
Text Label 15700 3600 0    60   ~ 0
16(Tx2)
Text Label 15700 3500 0    60   ~ 0
15(Rx3)
Text Label 15700 3400 0    60   ~ 0
14(Tx3)
Text Label 15700 1550 0    60   ~ 0
13(**)
Text Label 15700 1650 0    60   ~ 0
12(**)
Text Label 15700 1750 0    60   ~ 0
11(**)
Text Label 15700 1850 0    60   ~ 0
10(**)
Text Label 15700 1950 0    60   ~ 0
9(**)
Text Label 15700 2050 0    60   ~ 0
8(**)
Text Label 15700 2450 0    60   ~ 0
7(**)
Text Label 15700 2550 0    60   ~ 0
6(**)
Text Label 15700 2650 0    60   ~ 0
5(**)
Text Label 15700 2750 0    60   ~ 0
4(**)
Text Label 15700 2850 0    60   ~ 0
3(**)
Text Label 15700 2950 0    60   ~ 0
2(**)
Text Label 15700 3050 0    60   ~ 0
1(Tx0)
Text Label 15700 3150 0    60   ~ 0
0(Rx0)
Text Label 15700 1250 0    60   ~ 0
SDA
Text Label 15700 1150 0    60   ~ 0
SCL
Text Label 15700 1350 0    60   ~ 0
AREF
Text Notes 13675 575  0    60   ~ 0
Shield for Arduino Mega Rev 3
Text Notes 16000 1000 0    60   ~ 0
Holes
$Comp
L Connector_Generic:Conn_01x01 P8
U 1 1 56D70B71
P 15900 650
F 0 "P8" V 16000 650 31  0000 C CNN
F 1 "CONN_01X01" V 16000 650 50  0001 C CNN
F 2 "Socket_Arduino_Mega:Arduino_1pin" H 15900 650 50  0001 C CNN
F 3 "" H 15900 650 50  0000 C CNN
	1    15900 650 
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x01 P9
U 1 1 56D70C9B
P 16000 650
F 0 "P9" V 16100 650 31  0000 C CNN
F 1 "CONN_01X01" V 16100 650 50  0001 C CNN
F 2 "Socket_Arduino_Mega:Arduino_1pin" H 16000 650 50  0001 C CNN
F 3 "" H 16000 650 50  0000 C CNN
	1    16000 650 
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x01 P10
U 1 1 56D70CE6
P 16100 650
F 0 "P10" V 16200 650 31  0000 C CNN
F 1 "CONN_01X01" V 16200 650 50  0001 C CNN
F 2 "Socket_Arduino_Mega:Arduino_1pin" H 16100 650 50  0001 C CNN
F 3 "" H 16100 650 50  0000 C CNN
	1    16100 650 
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x01 P11
U 1 1 56D70D2C
P 16200 650
F 0 "P11" V 16300 650 31  0000 C CNN
F 1 "CONN_01X01" V 16300 650 50  0001 C CNN
F 2 "Socket_Arduino_Mega:Arduino_1pin" H 16200 650 50  0001 C CNN
F 3 "" H 16200 650 50  0000 C CNN
	1    16200 650 
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x01 P12
U 1 1 56D711A2
P 16300 650
F 0 "P12" V 16400 650 31  0000 C CNN
F 1 "CONN_01X01" V 16400 650 50  0001 C CNN
F 2 "Socket_Arduino_Mega:Arduino_1pin" H 16300 650 50  0001 C CNN
F 3 "" H 16300 650 50  0000 C CNN
	1    16300 650 
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x01 P13
U 1 1 56D711F0
P 16400 650
F 0 "P13" V 16500 650 31  0000 C CNN
F 1 "CONN_01X01" V 16500 650 50  0001 C CNN
F 2 "Socket_Arduino_Mega:Arduino_1pin" H 16400 650 50  0001 C CNN
F 3 "" H 16400 650 50  0000 C CNN
	1    16400 650 
	0    -1   -1   0   
$EndComp
NoConn ~ 15900 850 
NoConn ~ 16000 850 
NoConn ~ 16100 850 
NoConn ~ 16200 850 
NoConn ~ 16300 850 
NoConn ~ 16400 850 
$Comp
L Connector_Generic:Conn_01x08 P2
U 1 1 56D71773
P 14850 1650
F 0 "P2" H 14850 2050 50  0000 C CNN
F 1 "Power" V 14950 1650 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 14850 1650 50  0001 C CNN
F 3 "" H 14850 1650 50  0000 C CNN
	1    14850 1650
	1    0    0    -1  
$EndComp
Text Notes 14950 1350 0    60   ~ 0
1
$Comp
L power:+3V3 #PWR01
U 1 1 56D71AA9
P 14400 1200
F 0 "#PWR01" H 14400 1050 50  0001 C CNN
F 1 "+3.3V" V 14400 1450 50  0000 C CNN
F 2 "" H 14400 1200 50  0000 C CNN
F 3 "" H 14400 1200 50  0000 C CNN
	1    14400 1200
	1    0    0    -1  
$EndComp
Text Label 13900 1550 0    60   ~ 0
Reset
$Comp
L power:+5V #PWR02
U 1 1 56D71D10
P 14300 1050
F 0 "#PWR02" H 14300 900 50  0001 C CNN
F 1 "+5V" V 14300 1250 50  0000 C CNN
F 2 "" H 14300 1050 50  0000 C CNN
F 3 "" H 14300 1050 50  0000 C CNN
	1    14300 1050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR03
U 1 1 56D721E6
P 14550 2150
F 0 "#PWR03" H 14550 1900 50  0001 C CNN
F 1 "GND" H 14550 2000 50  0000 C CNN
F 2 "" H 14550 2150 50  0000 C CNN
F 3 "" H 14550 2150 50  0000 C CNN
	1    14550 2150
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x10 P5
U 1 1 56D72368
P 15250 1550
F 0 "P5" H 15250 2050 50  0000 C CNN
F 1 "PWM" V 15350 1550 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x10" H 15250 1550 50  0001 C CNN
F 3 "" H 15250 1550 50  0000 C CNN
	1    15250 1550
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR04
U 1 1 56D72A3D
P 15550 2150
F 0 "#PWR04" H 15550 1900 50  0001 C CNN
F 1 "GND" H 15550 2000 50  0000 C CNN
F 2 "" H 15550 2150 50  0000 C CNN
F 3 "" H 15550 2150 50  0000 C CNN
	1    15550 2150
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P3
U 1 1 56D72F1C
P 14850 2750
F 0 "P3" H 14850 3150 50  0000 C CNN
F 1 "Analog" V 14950 2750 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 14850 2750 50  0001 C CNN
F 3 "" H 14850 2750 50  0000 C CNN
	1    14850 2750
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P6
U 1 1 56D734D0
P 15250 2750
F 0 "P6" H 15250 3150 50  0000 C CNN
F 1 "PWM" V 15350 2750 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 15250 2750 50  0001 C CNN
F 3 "" H 15250 2750 50  0000 C CNN
	1    15250 2750
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P4
U 1 1 56D73A0E
P 14850 3700
F 0 "P4" H 14850 4100 50  0000 C CNN
F 1 "Analog" V 14950 3700 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 14850 3700 50  0001 C CNN
F 3 "" H 14850 3700 50  0000 C CNN
	1    14850 3700
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 P7
U 1 1 56D73F2C
P 15250 3700
F 0 "P7" H 15250 4100 50  0000 C CNN
F 1 "Communication" V 15350 3700 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_1x08" H 15250 3700 50  0001 C CNN
F 3 "" H 15250 3700 50  0000 C CNN
	1    15250 3700
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x18_Odd_Even P1
U 1 1 56D743B5
P 15000 5050
F 0 "P1" H 15000 6000 50  0000 C CNN
F 1 "Digital" V 15000 5050 50  0000 C CNN
F 2 "Socket_Arduino_Mega:Socket_Strip_Arduino_2x18" H 15000 4000 50  0001 C CNN
F 3 "" H 15000 4000 50  0000 C CNN
	1    15000 5050
	0    -1   1    0   
$EndComp
Wire Wire Line
	14400 1200 14400 1650
Wire Wire Line
	14550 1450 14550 1200
Wire Wire Line
	14650 1450 14550 1450
Wire Notes Line
	15750 1000 15750 500 
Wire Notes Line
	16500 1000 15750 1000
Wire Notes Line
	15150 650  15150 475 
Wire Notes Line
	13650 650  15150 650 
Wire Wire Line
	14400 1650 14650 1650
Wire Wire Line
	14300 1050 14300 1750
Wire Wire Line
	14300 1750 14650 1750
Wire Wire Line
	14650 2050 14200 2050
Wire Wire Line
	14200 2050 14200 1200
Wire Wire Line
	13900 1550 14650 1550
Wire Wire Line
	14650 1850 14550 1850
Wire Wire Line
	14550 1850 14550 1950
Wire Wire Line
	14550 1950 14550 2150
Wire Wire Line
	14650 1950 14550 1950
Connection ~ 14550 1950
Wire Wire Line
	15450 1150 15700 1150
Wire Wire Line
	15700 1250 15450 1250
Wire Wire Line
	15450 1350 15700 1350
Wire Wire Line
	15450 1550 15700 1550
Wire Wire Line
	15700 1650 15450 1650
Wire Wire Line
	15450 1750 15700 1750
Wire Wire Line
	15450 1850 15700 1850
Wire Wire Line
	15700 1950 15450 1950
Wire Wire Line
	15450 2050 15700 2050
Wire Wire Line
	15550 2150 15550 1450
Wire Wire Line
	15550 1450 15450 1450
Wire Wire Line
	14650 2450 14200 2450
Wire Wire Line
	14200 2550 14650 2550
Wire Wire Line
	14650 2650 14200 2650
Wire Wire Line
	14200 2750 14650 2750
Wire Wire Line
	14650 2850 14200 2850
Wire Wire Line
	14200 2950 14650 2950
Wire Wire Line
	14650 3050 14200 3050
Wire Wire Line
	14200 3150 14650 3150
Wire Wire Line
	15700 2450 15450 2450
Wire Wire Line
	15450 2550 15700 2550
Wire Wire Line
	15700 2650 15450 2650
Wire Wire Line
	15450 2750 15700 2750
Wire Wire Line
	15700 2850 15450 2850
Wire Wire Line
	15450 2950 15700 2950
Wire Wire Line
	15700 3050 15450 3050
Wire Wire Line
	15450 3150 15700 3150
Wire Wire Line
	14650 3400 14200 3400
Wire Wire Line
	14200 3500 14650 3500
Wire Wire Line
	14650 3600 14200 3600
Wire Wire Line
	14200 3700 14650 3700
Wire Wire Line
	14650 3800 14200 3800
Wire Wire Line
	14200 3900 14650 3900
Wire Wire Line
	14650 4000 14200 4000
Wire Wire Line
	14200 4100 14650 4100
Wire Wire Line
	15700 3400 15450 3400
Wire Wire Line
	15450 3500 15700 3500
Wire Wire Line
	15700 3600 15450 3600
Wire Wire Line
	15450 3700 15700 3700
Wire Wire Line
	15700 3800 15450 3800
Wire Wire Line
	15450 3900 15700 3900
Wire Wire Line
	15700 4000 15450 4000
Wire Wire Line
	15450 4100 15700 4100
Wire Wire Line
	15800 4850 15800 4650
Wire Wire Line
	15700 4850 15700 4650
Wire Wire Line
	15600 4850 15600 4650
Wire Wire Line
	15500 4850 15500 4650
Wire Wire Line
	15400 4850 15400 4650
Wire Wire Line
	15300 4850 15300 4650
Wire Wire Line
	15200 4850 15200 4650
Wire Wire Line
	15100 4850 15100 4650
Wire Wire Line
	15000 4850 15000 4650
Wire Wire Line
	14900 4850 14900 4650
Wire Wire Line
	14800 4850 14800 4650
Wire Wire Line
	14700 4850 14700 4650
Wire Wire Line
	14600 4850 14600 4650
Wire Wire Line
	14500 4850 14500 4650
Wire Wire Line
	14400 4850 14400 4650
Wire Wire Line
	14300 4850 14300 4650
Wire Wire Line
	15800 5350 15800 5650
Wire Wire Line
	15700 5350 15700 5650
Wire Wire Line
	15600 5350 15600 5650
Wire Wire Line
	15500 5350 15500 5650
Wire Wire Line
	15400 5350 15400 5650
Wire Wire Line
	15300 5350 15300 5650
Wire Wire Line
	15200 5350 15200 5650
Wire Wire Line
	15100 5350 15100 5650
Wire Wire Line
	15000 5350 15000 5650
Wire Wire Line
	14900 5350 14900 5650
Wire Wire Line
	14800 5350 14800 5650
Wire Wire Line
	14700 5350 14700 5650
Wire Wire Line
	14600 5350 14600 5650
Wire Wire Line
	14500 5350 14500 5650
Wire Wire Line
	14400 5350 14400 5750
Wire Wire Line
	14300 5350 14300 5750
Wire Wire Line
	14200 4850 13950 4850
$Comp
L power:GND #PWR05
U 1 1 56D758F6
P 13950 5750
F 0 "#PWR05" H 13950 5500 50  0001 C CNN
F 1 "GND" H 13950 5600 50  0000 C CNN
F 2 "" H 13950 5750 50  0000 C CNN
F 3 "" H 13950 5750 50  0000 C CNN
	1    13950 5750
	1    0    0    -1  
$EndComp
Wire Wire Line
	14200 5350 13950 5350
Connection ~ 13950 5350
Wire Wire Line
	16050 5350 15900 5350
Wire Wire Line
	16050 4850 15900 4850
$Comp
L power:+5V #PWR06
U 1 1 56D75AB8
P 16050 4550
F 0 "#PWR06" H 16050 4400 50  0001 C CNN
F 1 "+5V" H 16050 4690 50  0000 C CNN
F 2 "" H 16050 4550 50  0000 C CNN
F 3 "" H 16050 4550 50  0000 C CNN
	1    16050 4550
	1    0    0    -1  
$EndComp
Connection ~ 16050 4850
Wire Wire Line
	16050 4550 16050 4850
Wire Wire Line
	16050 4850 16050 5350
Wire Wire Line
	13950 4850 13950 5350
Wire Wire Line
	13950 5350 13950 5750
Wire Notes Line
	16500 6050 13650 6050
Wire Notes Line
	13650 6050 13650 500 
$EndSCHEMATC
