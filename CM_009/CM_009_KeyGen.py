Name = input()
key = list(str(sum(map(ord, Name)) * 1234567890))
key[3] = '-'
key[8] = '-'
print(f"{''.join(key)}")

'''
00402132      85C0          test eax,eax                                            ;  eax = 0x1 != 0 循环结束标志
00402134      0F84 9C000000 je Andréna.004021D6
0040213A      8D55 94       lea edx,dword ptr ss:[ebp-0x6C]
0040213D   .  8D45 DC       lea eax,dword ptr ss:[ebp-0x24]
00402140   .  52            push edx
00402141   .  50            push eax
00402142   .  C745 9C 01000>mov dword ptr ss:[ebp-0x64],0x1
00402149   .  895D 94       mov dword ptr ss:[ebp-0x6C],ebx
0040214C   .  FF15 90414000 call dword ptr ds:[<&MSVBVM50.__vbaI4Var>]              ;  msvbvm50.__vbaI4Var
00402152   .  8D4D BC       lea ecx,dword ptr ss:[ebp-0x44]
00402155   .  50            push eax
00402156   .  8D55 84       lea edx,dword ptr ss:[ebp-0x7C]
00402159   .  51            push ecx
0040215A   .  52            push edx
0040215B   .  FF15 38414000 call dword ptr ds:[<&MSVBVM50.#rtcMidCharVar_632>]      ;  msvbvm50.rtcMidCharVar
00402161   .  8D45 84       lea eax,dword ptr ss:[ebp-0x7C]
00402164   .  8D4D A8       lea ecx,dword ptr ss:[ebp-0x58]
00402167   .  50            push eax
00402168   .  51            push ecx
00402169   .  FF15 70414000 call dword ptr ds:[<&MSVBVM50.__vbaStrVarVal>]          ;  msvbvm50.__vbaStrVarVal
0040216F   .  50            push eax                                                ;  eax = "1"  eax = "2" to ecx = "6"
00402170   .  FF15 0C414000 call dword ptr ds:[<&MSVBVM50.#rtcAnsiValueBstr_516>]   ;  msvbvm50.rtcAnsiValueBstr
00402176   .  66:8985 4CFFF>mov word ptr ss:[ebp-0xB4],ax                           ;  eax = 0x31 eax = 0x32 to eax = 0x36
0040217D   .  8D55 CC       lea edx,dword ptr ss:[ebp-0x34]
00402180   .  8D85 44FFFFFF lea eax,dword ptr ss:[ebp-0xBC]
00402186   .  52            push edx
00402187   .  8D8D 74FFFFFF lea ecx,dword ptr ss:[ebp-0x8C]
0040218D   .  50            push eax
0040218E   .  51            push ecx
0040218F   .  899D 44FFFFFF mov dword ptr ss:[ebp-0xBC],ebx
00402195   .  FF15 94414000 call dword ptr ds:[<&MSVBVM50.__vbaVarAdd>]             ;  ecx = 0x96 ecx = 0xca ecx = 0xFF ecx = 0x135
0040219B   .  8BD0          mov edx,eax
0040219D   .  8D4D CC       lea ecx,dword ptr ss:[ebp-0x34]
004021A0   .  FFD6          call esi                                                ;  msvbvm50.__vbaVarMove
004021A2   .  8D4D A8       lea ecx,dword ptr ss:[ebp-0x58]
004021A5   .  FF15 B8414000 call dword ptr ds:[<&MSVBVM50.__vbaFreeStr>]            ;  msvbvm50.__vbaFreeStr
004021AB   .  8D55 84       lea edx,dword ptr ss:[ebp-0x7C]
004021AE   .  8D45 94       lea eax,dword ptr ss:[ebp-0x6C]
004021B1   .  52            push edx
004021B2   .  50            push eax
004021B3   .  53            push ebx
004021B4   .  FFD7          call edi                                                ;  msvbvm50.__vbaFreeVarList
004021B6   .  83C4 0C       add esp,0xC
004021B9   .  8D8D E8FEFFFF lea ecx,dword ptr ss:[ebp-0x118]
004021BF   .  8D95 F8FEFFFF lea edx,dword ptr ss:[ebp-0x108]
004021C5   .  8D45 DC       lea eax,dword ptr ss:[ebp-0x24]
004021C8   .  51            push ecx
004021C9   .  52            push edx
004021CA   .  50            push eax
004021CB   .  FF15 AC414000 call dword ptr ds:[<&MSVBVM50.__vbaVarForNext>]         ;  msvbvm50.__vbaVarForNext
004021D1   .^ E9 5CFFFFFF   jmp Andréna.00402132                                    ;  eax = 1  Loop six times and eax = 0
004021D6   >  8D4D CC       lea ecx,dword ptr ss:[ebp-0x34]
004021D9   .  8D95 54FFFFFF lea edx,dword ptr ss:[ebp-0xAC]
004021DF   .  51            push ecx                                                ;  ecx = 0x19f130
004021E0   .  8D45 94       lea eax,dword ptr ss:[ebp-0x6C]
004021E3   .  52            push edx
004021E4   .  50            push eax
004021E5   .  C785 5CFFFFFF>mov dword ptr ss:[ebp-0xA4],0x499602D2                  ;  0x499602d2 = 1234567890
004021EF   .  C785 54FFFFFF>mov dword ptr ss:[ebp-0xAC],0x3
004021F9   .  FF15 5C414000 call dword ptr ds:[<&MSVBVM50.__vbaVarMul>]             ;  msvbvm50.__vbaVarMul
004021FF   .  8BD0          mov edx,eax                                             ;  ST7 = 381481478010.0 = 0x499602D2 * 0x135
00402201   .  8D4D CC       lea ecx,dword ptr ss:[ebp-0x34]
00402204   .  FFD6          call esi                                                ;  msvbvm50.__vbaVarMove
00402206   .  8B1D A0414000 mov ebx,dword ptr ds:[<&MSVBVM50.__vbaMidStmtVar>]      ;  msvbvm50.__vbaMidStmtVar
0040220C   .  8D4D CC       lea ecx,dword ptr ss:[ebp-0x34]
0040220F   .  51            push ecx
00402210   .  6A 04         push 0x4                                                ;  insert location 0x4
00402212   .  8D95 54FFFFFF lea edx,dword ptr ss:[ebp-0xAC]
00402218   .  6A 01         push 0x1
0040221A   .  52            push edx
0040221B   .  C785 5CFFFFFF>mov dword ptr ss:[ebp-0xA4],Andréna.00401C34            ;  UNICODE "-"
00402225   .  C785 54FFFFFF>mov dword ptr ss:[ebp-0xAC],0x8
0040222F   .  FFD3          call ebx                                                ;  <&MSVBVM50.__vbaMidStmtVar>
00402231   .  8D45 CC       lea eax,dword ptr ss:[ebp-0x34]                         ;  eax = "ck"
00402234   .  8D8D 54FFFFFF lea ecx,dword ptr ss:[ebp-0xAC]
0040223A   .  50            push eax
0040223B   .  6A 09         push 0x9                                                ;  insert location 0x9
0040223D   .  6A 01         push 0x1
0040223F   .  51            push ecx
00402240   .  C785 5CFFFFFF>mov dword ptr ss:[ebp-0xA4],Andréna.00401C34            ;  UNICODE "-"
0040224A   .  C785 54FFFFFF>mov dword ptr ss:[ebp-0xAC],0x8
00402254   .  FFD3          call ebx
00402256   .  8B45 08       mov eax,dword ptr ss:[ebp+0x8]
00402259   .  50            push eax
0040225A   .  8B10          mov edx,dword ptr ds:[eax]
0040225C   .  FF92 04030000 call dword ptr ds:[edx+0x304]
00402262   .  50            push eax
00402263   .  8D45 A4       lea eax,dword ptr ss:[ebp-0x5C]
00402266   .  50            push eax
00402267   .  FF15 24414000 call dword ptr ds:[<&MSVBVM50.__vbaObjSet>]             ;  msvbvm50.__vbaObjSet
0040226D   .  8BD8          mov ebx,eax
0040226F   .  8D55 A8       lea edx,dword ptr ss:[ebp-0x58]
00402272   .  52            push edx
00402273   .  53            push ebx
00402274   .  8B0B          mov ecx,dword ptr ds:[ebx]
00402276   .  FF91 A0000000 call dword ptr ds:[ecx+0xA0]
0040227C   .  85C0          test eax,eax
0040227E   .  7D 12         jge short Andréna.00402292
00402280   .  68 A0000000   push 0xA0
00402285   .  68 201C4000   push Andréna.00401C20
0040228A   .  53            push ebx
0040228B   .  50            push eax
0040228C   .  FF15 14414000 call dword ptr ds:[<&MSVBVM50.__vbaHresultCheckObj>]    ;  msvbvm50.__vbaHresultCheckObj
00402292   >  8B45 A8       mov eax,dword ptr ss:[ebp-0x58]                         ;  eax = "111111" key
00402295   .  8D4D CC       lea ecx,dword ptr ss:[ebp-0x34]                         ;  ecx = [0x19f130] = "381-8147-010"
00402298   .  8945 9C       mov dword ptr ss:[ebp-0x64],eax
0040229B   .  8D45 94       lea eax,dword ptr ss:[ebp-0x6C]
0040229E   .  50            push eax
0040229F   .  51            push ecx
004022A0   .  C745 A8 00000>mov dword ptr ss:[ebp-0x58],0x0
004022A7   .  C745 94 08800>mov dword ptr ss:[ebp-0x6C],0x8008
004022AE   .  FF15 48414000 call dword ptr ds:[<&MSVBVM50.__vbaVarTstEq>]           ;  msvbvm50.__vbaVarTstEq
004022B4   .  8D4D A4       lea ecx,dword ptr ss:[ebp-0x5C]
004022B7   .  8BD8          mov ebx,eax
004022B9   .  FF15 B4414000 call dword ptr ds:[<&MSVBVM50.__vbaFreeObj>]            ;  msvbvm50.__vbaFreeObj
004022BF   .  8D4D 94       lea ecx,dword ptr ss:[ebp-0x6C]
004022C2   .  FF15 00414000 call dword ptr ds:[<&MSVBVM50.__vbaFreeVar>]            ;  msvbvm50.__vbaFreeVar
004022C8   .  66:85DB       test bx,bx
004022CB      0F84 C0000000 je Andréna.00402391                                     ;  key jump

'''