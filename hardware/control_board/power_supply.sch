EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 5 5
Title "Airhockey Control Board"
Date "2021-11-05"
Rev "A"
Comp "Olin Electric Motorsports"
Comment1 "Designer: Wesley Soo-Hoo"
Comment2 "Principles of Integrated Engineering"
Comment3 ""
Comment4 ""
$EndDescr
Text GLabel 5900 3650 3    50   Input ~ 0
ESTOP_L
Text GLabel 6250 3650 3    50   Input ~ 0
ESTOP_H
Text GLabel 3950 3850 0    50   Input ~ 0
PWR_SW_L
Text GLabel 3950 3650 0    50   Input ~ 0
PWR_SW_H
$Comp
L power:+5V #PWR051
U 1 1 61A8E0F0
P 7350 2850
F 0 "#PWR051" H 7350 2700 50  0001 C CNN
F 1 "+5V" H 7365 3023 50  0000 C CNN
F 2 "" H 7350 2850 50  0001 C CNN
F 3 "" H 7350 2850 50  0001 C CNN
	1    7350 2850
	1    0    0    -1  
$EndComp
Text GLabel 7550 3350 2    50   Input ~ 0
~PS_ON
$Comp
L Device:R_Small_US R3
U 1 1 61A8EADE
P 7350 3100
F 0 "R3" H 7418 3146 50  0000 L CNN
F 1 "R_10K" H 7418 3055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 7350 3100 50  0001 C CNN
F 3 "~" H 7350 3100 50  0001 C CNN
	1    7350 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	7350 3200 7350 3350
Wire Wire Line
	7350 3350 7550 3350
Wire Wire Line
	7350 3000 7350 2850
$Comp
L Transistor_FET:BSS138 Q1
U 1 1 61A92686
P 7250 3650
F 0 "Q1" H 7454 3696 50  0000 L CNN
F 1 "BSS138" H 7454 3605 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 7450 3575 50  0001 L CIN
F 3 "https://www.onsemi.com/pub/Collateral/BSS138-D.PDF" H 7250 3650 50  0001 L CNN
	1    7250 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	7350 3450 7350 3350
Connection ~ 7350 3350
$Comp
L power:GND #PWR052
U 1 1 61A9C523
P 7350 4050
F 0 "#PWR052" H 7350 3800 50  0001 C CNN
F 1 "GND" H 7355 3877 50  0000 C CNN
F 2 "" H 7350 4050 50  0001 C CNN
F 3 "" H 7350 4050 50  0001 C CNN
	1    7350 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	7350 4050 7350 3950
$Comp
L Device:R_Small_US R2
U 1 1 61A9CC4C
P 7100 3950
F 0 "R2" V 7200 3950 50  0000 C CNN
F 1 "R_10K" V 7000 3950 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 7100 3950 50  0001 C CNN
F 3 "~" H 7100 3950 50  0001 C CNN
	1    7100 3950
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7200 3950 7350 3950
Connection ~ 7350 3950
Wire Wire Line
	7350 3950 7350 3850
Wire Wire Line
	7000 3950 6900 3950
Wire Wire Line
	6900 3950 6900 3650
Wire Wire Line
	6900 3650 7050 3650
Wire Wire Line
	6250 3650 6900 3650
Connection ~ 6900 3650
Text Label 6900 3650 2    50   ~ 0
PS_ON_SIG
Text GLabel 5550 3650 0    50   Input ~ 0
PWR_ON_OUTPUT
Wire Wire Line
	5550 3650 5900 3650
$Comp
L power:GND #PWR050
U 1 1 61AA0499
P 4050 3950
F 0 "#PWR050" H 4050 3700 50  0001 C CNN
F 1 "GND" H 4055 3777 50  0000 C CNN
F 2 "" H 4050 3950 50  0001 C CNN
F 3 "" H 4050 3950 50  0001 C CNN
	1    4050 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4050 3950 4050 3850
Wire Wire Line
	4050 3850 3950 3850
Wire Wire Line
	4050 3650 3950 3650
$Comp
L Device:R_Small_US R1
U 1 1 61AA3ECC
P 4050 3400
F 0 "R1" H 4118 3446 50  0000 L CNN
F 1 "R_10K" H 4118 3355 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4050 3400 50  0001 C CNN
F 3 "~" H 4050 3400 50  0001 C CNN
	1    4050 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4050 3500 4050 3650
$Comp
L power:+5V #PWR049
U 1 1 61AA27C2
P 4050 3250
F 0 "#PWR049" H 4050 3100 50  0001 C CNN
F 1 "+5V" H 4065 3423 50  0000 C CNN
F 2 "" H 4050 3250 50  0001 C CNN
F 3 "" H 4050 3250 50  0001 C CNN
	1    4050 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4050 3300 4050 3250
Text GLabel 4050 3650 2    50   Input ~ 0
PWR_SW
$EndSCHEMATC
