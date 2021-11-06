EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 2 5
Title "Airhockey Control Board"
Date "2021-11-05"
Rev "A"
Comp "Olin Electric Motorsports"
Comment1 "Designer: Wesley Soo-Hoo"
Comment2 "Principles of Integrated Engineering"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Driver_Motor:Pololu_Breakout_A4988 A1
U 1 1 6190B452
P 2300 3600
F 0 "A1" H 2050 4250 50  0000 C CNN
F 1 "Pololu_Breakout_A4988" H 3050 2850 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 2575 2850 50  0001 L CNN
F 3 "https://www.pololu.com/product/2980/pictures" H 2400 3300 50  0001 C CNN
	1    2300 3600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR01
U 1 1 6191A2DB
P 2300 2600
F 0 "#PWR01" H 2300 2450 50  0001 C CNN
F 1 "+5V" H 2315 2773 50  0000 C CNN
F 2 "" H 2300 2600 50  0001 C CNN
F 3 "" H 2300 2600 50  0001 C CNN
	1    2300 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 2600 2300 2900
$Comp
L power:+12V #PWR03
U 1 1 6191D07A
P 2500 2600
F 0 "#PWR03" H 2500 2450 50  0001 C CNN
F 1 "+12V" H 2515 2773 50  0000 C CNN
F 2 "" H 2500 2600 50  0001 C CNN
F 3 "" H 2500 2600 50  0001 C CNN
	1    2500 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 2600 2500 2750
$Comp
L power:GND #PWR02
U 1 1 6191FECB
P 2300 4550
F 0 "#PWR02" H 2300 4300 50  0001 C CNN
F 1 "GND" H 2305 4377 50  0000 C CNN
F 2 "" H 2300 4550 50  0001 C CNN
F 3 "" H 2300 4550 50  0001 C CNN
	1    2300 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 4550 2300 4400
$Comp
L power:GND #PWR04
U 1 1 61920827
P 2500 4550
F 0 "#PWR04" H 2500 4300 50  0001 C CNN
F 1 "GND" H 2505 4377 50  0000 C CNN
F 2 "" H 2500 4550 50  0001 C CNN
F 3 "" H 2500 4550 50  0001 C CNN
	1    2500 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2650 2750 2500 2750
Connection ~ 2500 2750
Wire Wire Line
	2500 2750 2500 2900
$Comp
L power:GND #PWR05
U 1 1 61929737
P 3000 2900
F 0 "#PWR05" H 3000 2650 50  0001 C CNN
F 1 "GND" H 3005 2727 50  0000 C CNN
F 2 "" H 3000 2900 50  0001 C CNN
F 3 "" H 3000 2900 50  0001 C CNN
	1    3000 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 2900 3000 2750
Wire Wire Line
	3000 2750 2850 2750
Wire Wire Line
	2500 4400 2500 4550
$Comp
L Driver_Motor:Pololu_Breakout_A4988 A2
U 1 1 6193D6AC
P 4300 3600
F 0 "A2" H 4050 4250 50  0000 C CNN
F 1 "Pololu_Breakout_A4988" H 5050 2850 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 4575 2850 50  0001 L CNN
F 3 "https://www.pololu.com/product/2980/pictures" H 4400 3300 50  0001 C CNN
	1    4300 3600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR06
U 1 1 6193D6B2
P 4300 2600
F 0 "#PWR06" H 4300 2450 50  0001 C CNN
F 1 "+5V" H 4315 2773 50  0000 C CNN
F 2 "" H 4300 2600 50  0001 C CNN
F 3 "" H 4300 2600 50  0001 C CNN
	1    4300 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 2600 4300 2900
$Comp
L power:+12V #PWR08
U 1 1 6193D6B9
P 4500 2600
F 0 "#PWR08" H 4500 2450 50  0001 C CNN
F 1 "+12V" H 4515 2773 50  0000 C CNN
F 2 "" H 4500 2600 50  0001 C CNN
F 3 "" H 4500 2600 50  0001 C CNN
	1    4500 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 2600 4500 2750
$Comp
L power:GND #PWR07
U 1 1 6193D6C0
P 4300 4550
F 0 "#PWR07" H 4300 4300 50  0001 C CNN
F 1 "GND" H 4305 4377 50  0000 C CNN
F 2 "" H 4300 4550 50  0001 C CNN
F 3 "" H 4300 4550 50  0001 C CNN
	1    4300 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 4550 4300 4400
$Comp
L power:GND #PWR09
U 1 1 6193D6C7
P 4500 4550
F 0 "#PWR09" H 4500 4300 50  0001 C CNN
F 1 "GND" H 4505 4377 50  0000 C CNN
F 2 "" H 4500 4550 50  0001 C CNN
F 3 "" H 4500 4550 50  0001 C CNN
	1    4500 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 2750 4500 2750
Connection ~ 4500 2750
Wire Wire Line
	4500 2750 4500 2900
$Comp
L power:GND #PWR010
U 1 1 6193D6DB
P 5000 2900
F 0 "#PWR010" H 5000 2650 50  0001 C CNN
F 1 "GND" H 5005 2727 50  0000 C CNN
F 2 "" H 5000 2900 50  0001 C CNN
F 3 "" H 5000 2900 50  0001 C CNN
	1    5000 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 2900 5000 2750
Wire Wire Line
	5000 2750 4850 2750
Wire Wire Line
	4500 4400 4500 4550
$Comp
L Driver_Motor:Pololu_Breakout_A4988 A3
U 1 1 61944875
P 6300 3600
F 0 "A3" H 6050 4250 50  0000 C CNN
F 1 "Pololu_Breakout_A4988" H 7050 2850 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 6575 2850 50  0001 L CNN
F 3 "https://www.pololu.com/product/2980/pictures" H 6400 3300 50  0001 C CNN
	1    6300 3600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR011
U 1 1 6194487B
P 6300 2600
F 0 "#PWR011" H 6300 2450 50  0001 C CNN
F 1 "+5V" H 6315 2773 50  0000 C CNN
F 2 "" H 6300 2600 50  0001 C CNN
F 3 "" H 6300 2600 50  0001 C CNN
	1    6300 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6300 2600 6300 2900
$Comp
L power:+12V #PWR013
U 1 1 61944882
P 6500 2600
F 0 "#PWR013" H 6500 2450 50  0001 C CNN
F 1 "+12V" H 6515 2773 50  0000 C CNN
F 2 "" H 6500 2600 50  0001 C CNN
F 3 "" H 6500 2600 50  0001 C CNN
	1    6500 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6500 2600 6500 2750
$Comp
L power:GND #PWR012
U 1 1 61944889
P 6300 4550
F 0 "#PWR012" H 6300 4300 50  0001 C CNN
F 1 "GND" H 6305 4377 50  0000 C CNN
F 2 "" H 6300 4550 50  0001 C CNN
F 3 "" H 6300 4550 50  0001 C CNN
	1    6300 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	6300 4550 6300 4400
$Comp
L power:GND #PWR014
U 1 1 61944890
P 6500 4550
F 0 "#PWR014" H 6500 4300 50  0001 C CNN
F 1 "GND" H 6505 4377 50  0000 C CNN
F 2 "" H 6500 4550 50  0001 C CNN
F 3 "" H 6500 4550 50  0001 C CNN
	1    6500 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 2750 6500 2750
Connection ~ 6500 2750
Wire Wire Line
	6500 2750 6500 2900
$Comp
L power:GND #PWR015
U 1 1 619448A4
P 7000 2900
F 0 "#PWR015" H 7000 2650 50  0001 C CNN
F 1 "GND" H 7005 2727 50  0000 C CNN
F 2 "" H 7000 2900 50  0001 C CNN
F 3 "" H 7000 2900 50  0001 C CNN
	1    7000 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 2900 7000 2750
Wire Wire Line
	7000 2750 6850 2750
Wire Wire Line
	6500 4400 6500 4550
$Comp
L Driver_Motor:Pololu_Breakout_A4988 A4
U 1 1 6194E62F
P 8300 3600
F 0 "A4" H 8050 4250 50  0000 C CNN
F 1 "Pololu_Breakout_A4988" H 9050 2850 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 8575 2850 50  0001 L CNN
F 3 "https://www.pololu.com/product/2980/pictures" H 8400 3300 50  0001 C CNN
	1    8300 3600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR016
U 1 1 6194E635
P 8300 2600
F 0 "#PWR016" H 8300 2450 50  0001 C CNN
F 1 "+5V" H 8315 2773 50  0000 C CNN
F 2 "" H 8300 2600 50  0001 C CNN
F 3 "" H 8300 2600 50  0001 C CNN
	1    8300 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 2600 8300 2900
$Comp
L power:+12V #PWR018
U 1 1 6194E63C
P 8500 2600
F 0 "#PWR018" H 8500 2450 50  0001 C CNN
F 1 "+12V" H 8515 2773 50  0000 C CNN
F 2 "" H 8500 2600 50  0001 C CNN
F 3 "" H 8500 2600 50  0001 C CNN
	1    8500 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	8500 2600 8500 2750
$Comp
L power:GND #PWR017
U 1 1 6194E643
P 8300 4550
F 0 "#PWR017" H 8300 4300 50  0001 C CNN
F 1 "GND" H 8305 4377 50  0000 C CNN
F 2 "" H 8300 4550 50  0001 C CNN
F 3 "" H 8300 4550 50  0001 C CNN
	1    8300 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 4550 8300 4400
$Comp
L power:GND #PWR019
U 1 1 6194E64A
P 8500 4550
F 0 "#PWR019" H 8500 4300 50  0001 C CNN
F 1 "GND" H 8505 4377 50  0000 C CNN
F 2 "" H 8500 4550 50  0001 C CNN
F 3 "" H 8500 4550 50  0001 C CNN
	1    8500 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	8650 2750 8500 2750
Connection ~ 8500 2750
Wire Wire Line
	8500 2750 8500 2900
$Comp
L power:GND #PWR020
U 1 1 6194E65E
P 9000 2900
F 0 "#PWR020" H 9000 2650 50  0001 C CNN
F 1 "GND" H 9005 2727 50  0000 C CNN
F 2 "" H 9000 2900 50  0001 C CNN
F 3 "" H 9000 2900 50  0001 C CNN
	1    9000 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9000 2900 9000 2750
Wire Wire Line
	9000 2750 8850 2750
Wire Wire Line
	8500 4400 8500 4550
Text GLabel 1900 3500 0    40   Input ~ 0
~MOT0_EN
Text GLabel 1900 3600 0    50   Input ~ 0
MOT0_STEP
Text GLabel 1900 3700 0    50   Input ~ 0
MOT0_DIR
Text GLabel 1900 3900 0    50   Input ~ 0
MOT0_MS1
Text GLabel 1900 4000 0    50   Input ~ 0
MOT0_MS2
Text GLabel 1900 4100 0    50   Input ~ 0
MOT0_MS3
Text GLabel 2800 3500 2    50   Input ~ 0
MOT0_1B
Text GLabel 2800 3600 2    50   Input ~ 0
MOT0_1A
Text GLabel 2800 3700 2    50   Input ~ 0
MOT0_2A
Text GLabel 2800 3800 2    50   Input ~ 0
MOT0_2B
Text GLabel 3900 3500 0    40   Input ~ 0
~MOT1_EN
Text GLabel 3900 3600 0    50   Input ~ 0
MOT1_STEP
Text GLabel 3900 3700 0    50   Input ~ 0
MOT1_DIR
Text GLabel 3900 3900 0    50   Input ~ 0
MOT1_MS1
Text GLabel 3900 4000 0    50   Input ~ 0
MOT1_MS2
Text GLabel 3900 4100 0    50   Input ~ 0
MOT1_MS3
Text GLabel 4800 3500 2    50   Input ~ 0
MOT1_1B
Text GLabel 4800 3600 2    50   Input ~ 0
MOT1_1A
Text GLabel 4800 3700 2    50   Input ~ 0
MOT1_2A
Text GLabel 4800 3800 2    50   Input ~ 0
MOT1_2B
Text GLabel 5900 3500 0    40   Input ~ 0
~MOT2_EN
Text GLabel 5900 3600 0    50   Input ~ 0
MOT2_STEP
Text GLabel 5900 3700 0    50   Input ~ 0
MOT2_DIR
Text GLabel 5900 3900 0    50   Input ~ 0
MOT2_MS1
Text GLabel 5900 4000 0    50   Input ~ 0
MOT2_MS2
Text GLabel 5900 4100 0    50   Input ~ 0
MOT2_MS3
Text GLabel 6800 3500 2    50   Input ~ 0
MOT2_1B
Text GLabel 6800 3600 2    50   Input ~ 0
MOT2_1A
Text GLabel 6800 3700 2    50   Input ~ 0
MOT2_2A
Text GLabel 6800 3800 2    50   Input ~ 0
MOT2_2B
Text GLabel 7900 3500 0    40   Input ~ 0
~MOT3_EN
Text GLabel 7900 3600 0    50   Input ~ 0
MOT3_STEP
Text GLabel 7900 3700 0    50   Input ~ 0
MOT3_DIR
Text GLabel 7900 3900 0    50   Input ~ 0
MOT3_MS1
Text GLabel 7900 4000 0    50   Input ~ 0
MOT3_MS2
Text GLabel 7900 4100 0    50   Input ~ 0
MOT3_MS3
Text GLabel 8800 3500 2    50   Input ~ 0
MOT3_1B
Text GLabel 8800 3600 2    50   Input ~ 0
MOT3_1A
Text GLabel 8800 3700 2    50   Input ~ 0
MOT3_2A
Text GLabel 8800 3800 2    50   Input ~ 0
MOT3_2B
$Comp
L Device:Jumper_NC_Small JP1
U 1 1 619721BB
P 1700 3200
F 0 "JP1" H 1700 3412 50  0000 C CNN
F 1 "NC" H 1700 3321 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 1700 3200 50  0001 C CNN
F 3 "~" H 1700 3200 50  0001 C CNN
	1    1700 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 3200 1800 3200
Wire Wire Line
	1600 3200 1550 3200
Wire Wire Line
	1550 3200 1550 3300
Wire Wire Line
	1550 3300 1900 3300
$Comp
L Device:Jumper_NC_Small JP2
U 1 1 61975490
P 3700 3200
F 0 "JP2" H 3700 3412 50  0000 C CNN
F 1 "NC" H 3700 3321 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 3700 3200 50  0001 C CNN
F 3 "~" H 3700 3200 50  0001 C CNN
	1    3700 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 3200 3800 3200
Wire Wire Line
	3600 3200 3550 3200
Wire Wire Line
	3550 3200 3550 3300
Wire Wire Line
	3550 3300 3900 3300
$Comp
L Device:Jumper_NC_Small JP3
U 1 1 619769BC
P 5700 3200
F 0 "JP3" H 5700 3412 50  0000 C CNN
F 1 "NC" H 5700 3321 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 5700 3200 50  0001 C CNN
F 3 "~" H 5700 3200 50  0001 C CNN
	1    5700 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 3200 5800 3200
Wire Wire Line
	5600 3200 5550 3200
Wire Wire Line
	5550 3200 5550 3300
Wire Wire Line
	5550 3300 5900 3300
$Comp
L Device:Jumper_NC_Small JP4
U 1 1 619779BB
P 7700 3200
F 0 "JP4" H 7700 3412 50  0000 C CNN
F 1 "NC" H 7700 3321 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm" H 7700 3200 50  0001 C CNN
F 3 "~" H 7700 3200 50  0001 C CNN
	1    7700 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	7900 3200 7800 3200
Wire Wire Line
	7600 3200 7550 3200
Wire Wire Line
	7550 3200 7550 3300
Wire Wire Line
	7550 3300 7900 3300
$Comp
L Device:CP1_Small C1
U 1 1 61AB75C2
P 2750 2750
F 0 "C1" V 2850 2750 50  0000 C CNN
F 1 "100uF" V 2650 2750 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D12.5mm_P5.00mm" H 2750 2750 50  0001 C CNN
F 3 "~" H 2750 2750 50  0001 C CNN
	1    2750 2750
	0    -1   -1   0   
$EndComp
$Comp
L Device:CP1_Small C2
U 1 1 61AB9BEA
P 4750 2750
F 0 "C2" V 4850 2750 50  0000 C CNN
F 1 "100uF" V 4650 2750 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D12.5mm_P5.00mm" H 4750 2750 50  0001 C CNN
F 3 "~" H 4750 2750 50  0001 C CNN
	1    4750 2750
	0    -1   -1   0   
$EndComp
$Comp
L Device:CP1_Small C3
U 1 1 61ABA585
P 6750 2750
F 0 "C3" V 6850 2750 50  0000 C CNN
F 1 "100uF" V 6650 2750 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D12.5mm_P5.00mm" H 6750 2750 50  0001 C CNN
F 3 "~" H 6750 2750 50  0001 C CNN
	1    6750 2750
	0    -1   -1   0   
$EndComp
$Comp
L Device:CP1_Small C4
U 1 1 61ABB008
P 8750 2750
F 0 "C4" V 8850 2750 50  0000 C CNN
F 1 "100uF" V 8650 2750 50  0000 C CNN
F 2 "Capacitor_THT:CP_Radial_D12.5mm_P5.00mm" H 8750 2750 50  0001 C CNN
F 3 "~" H 8750 2750 50  0001 C CNN
	1    8750 2750
	0    -1   -1   0   
$EndComp
$EndSCHEMATC