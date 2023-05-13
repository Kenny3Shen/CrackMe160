Name = input()
serial = len(Name) * 0x17cfb + ord(Name[0])
print(f"AKA-{serial}")

'''
00402412   .  50            push eax                                       ;  eax 123456
00402413   .  8B1A          mov ebx,dword ptr ds:[edx]
00402415   .  FF15 E4404000 call dword ptr ds:[<&MSVBVM50.__vbaLenBstr>]   ;  msvbvm50.__vbaLenBstr
0040241B   .  8BF8          mov edi,eax                                    ;  edi = len(Name) = 0x6
0040241D   .  8B4D E8       mov ecx,dword ptr ss:[ebp-0x18]                ;  ecx = 0x71a7f4 = '123456'
00402420   .  69FF FB7C0100 imul edi,edi,0x17CFB                           ;  edi = edi * 0x17cfb = 0x8ede2
00402426   .  51            push ecx                                       ;  ecx = 0x71a7f4 123456
00402427   .  0F80 91020000 jo Afkayas_.004026BE
0040242D   .  FF15 F8404000 call dword ptr ds:[<&MSVBVM50.#rtcAnsiValueBst>;  msvbvm50.rtcAnsiValueBstr
00402433   .  0FBFD0        movsx edx,ax                                   ;  edx = 31 = '1'
00402436   .  03FA          add edi,edx                                    ;  edi = edi + edx = edi + 0x31 = 0x8ee13
00402438   .  0F80 80020000 jo Afkayas_.004026BE
0040243E   .  57            push edi    
0040243F   .  FF15 E0404000 call dword ptr ds:[<&MSVBVM50.__vbaStrI4>]     ;  msvbvm50.__vbaStrI4
00402445   .  8BD0          mov edx,eax                                    ;  eax = 585235 = 0x8ee13
00402447   .  8D4D E0       lea ecx,dword ptr ss:[ebp-0x20]
0040244A   .  FF15 70414000 call dword ptr ds:[<&MSVBVM50.__vbaStrMove>]   ;  msvbvm50.__vbaStrMove
00402450   .  8BBD 50FFFFFF mov edi,dword ptr ss:[ebp-0xB0]
00402456   .  50            push eax                                       ;  eax = '585235'
00402457   .  57            push edi                                       ;  edi = 27ed204
00402458   .  FF93 A4000000 call dword ptr ds:[ebx+0xA4]                   ;  msvbvm50.74110D32
0040245E   .  85C0          test eax,eax                                   ;  eax == 0
00402460   .  7D 12         jge short Afkayas_.00402474                    ;  大于等于跳过
'''


