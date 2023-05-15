key = map(ord, 'kXy^rO|*yXo*m\kMuOn*+')
originKey = []
for c in key:
    c -= 0xA
    originKey.append(chr(c))
print(''.join(originKey))
# aNoThEr oNe cRaCkEd !

'''
00401FA3   .  FF15 64414000 call dword ptr ds:[<&MSVBVM50.__vbaStrVa>;  msvbvm50.__vbaStrVarVal
00401FA9   .  50            push eax                                 ;  循环取key的Ascii值
00401FAA   .  FF15 08414000 call dword ptr ds:[<&MSVBVM50.#rtcAnsiVa>;  eax = 0x31 ecx = 0x1
00401FB0   .  66:05 0A00    add ax,0xA                               ;  eax = 0x3B = eax + 0xA 每个ascii值加0xA
00401FB4   .  0F80 B0020000 jo Andréna.0040226A
00401FBA   .  0FBFD0        movsx edx,ax                             ;  edx = eax = 0x3b
00401FBD   .  52            push edx
00401FBE   .  FF15 70414000 call dword ptr ds:[<&MSVBVM50.#rtcBstrFr>;  msvbvm50.rtcBstrFromAnsi
00401FC4   .  8985 7CFFFFFF mov dword ptr ss:[ebp-0x84],eax
00401FCA   .  8D45 CC       lea eax,dword ptr ss:[ebp-0x34]
00401FCD   .  8D8D 74FFFFFF lea ecx,dword ptr ss:[ebp-0x8C]
00401FD3   .  50            push eax
00401FD4   .  8D95 64FFFFFF lea edx,dword ptr ss:[ebp-0x9C]
00401FDA   .  51            push ecx
00401FDB   .  52            push edx
00401FDC   .  C785 74FFFFFF>mov dword ptr ss:[ebp-0x8C],0x8
00401FE6   .  FFD3          call ebx
00401FE8   .  8BD0          mov edx,eax
00401FEA   .  8D4D CC       lea ecx,dword ptr ss:[ebp-0x34]
00401FED   .  FFD6          call esi
00401FEF   .  8D4D A8       lea ecx,dword ptr ss:[ebp-0x58]
00401FF2   .  FF15 B0414000 call dword ptr ds:[<&MSVBVM50.__vbaFreeS>;  msvbvm50.__vbaFreeStr
00401FF8   .  8D85 74FFFFFF lea eax,dword ptr ss:[ebp-0x8C]
00401FFE   .  8D4D 84       lea ecx,dword ptr ss:[ebp-0x7C]
00402001   .  50            push eax
00402002   .  8D55 94       lea edx,dword ptr ss:[ebp-0x6C]
00402005   .  51            push ecx
00402006   .  52            push edx
00402007   .  6A 03         push 0x3
00402009   .  FFD7          call edi                                 ;  kernel32.CreateEventW
0040200B   .  83C4 10       add esp,0x10
0040200E   .  8D85 ECFEFFFF lea eax,dword ptr ss:[ebp-0x114]
00402014   .  8D8D FCFEFFFF lea ecx,dword ptr ss:[ebp-0x104]
0040201A   .  8D55 DC       lea edx,dword ptr ss:[ebp-0x24]
0040201D   .  50            push eax
0040201E   .  51            push ecx
0040201F   .  52            push edx
00402020   .  FF15 A4414000 call dword ptr ds:[<&MSVBVM50.__vbaVarFo>;  msvbvm50.__vbaVarForNext
00402026   .^ E9 3DFFFFFF   jmp Andréna.00401F68
0040202B   >  8D45 CC       lea eax,dword ptr ss:[ebp-0x34]
0040202E   .  8D8D 54FFFFFF lea ecx,dword ptr ss:[ebp-0xAC]
00402034   .  50            push eax
00402035   .  51            push ecx                                 ;  eax = "123456" + 0xA = ";<=>?@"
00402036   .  C785 5CFFFFFF>mov dword ptr ss:[ebp-0xA4],Andréna.0040>;  UNICODE "kXy^rO|*yXo*m\kMuOn*+"
00402040   .  C785 54FFFFFF>mov dword ptr ss:[ebp-0xAC],0x8008
0040204A   .  FF15 40414000 call dword ptr ds:[<&MSVBVM50.__vbaVarTs>;  msvbvm50.__vbaVarTstEq
00402050   .  66:85C0       test ax,ax                               ;  Key + 0xA后的字符串与 "kXy^rO|*yXo*m\kMuOn*+"比较
00402053      0F84 C0000000 je Andréna.00402119                      ;  key jump

'''