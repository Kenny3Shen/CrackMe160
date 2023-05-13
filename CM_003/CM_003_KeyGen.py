Name = input()
Serial = 0x15B38 * len(Name) + ord(Name[0])
Serial = (Serial + 2.0) * 3 - 2.0 - (-15.0)
print(f"{int(Serial)}")

'''
004081F2   .  50            push eax                                   ;  eax = "123456"
004081F3   .  8B1A          mov ebx,dword ptr ds:[edx]                 ;  ebx = 0x2313078
004081F5   .  FF15 F8B04000 call dword ptr ds:[<&MSVBVM50.__vbaLenBstr>;  msvbvm50.__vbaLenBstr
004081FB   .  8BF8          mov edi,eax                                ;  edi = 0x6 = len(eax)
004081FD   .  8B4D E8       mov ecx,dword ptr ss:[ebp-0x18]            ;  ecx = "123456"
00408200   .  69FF 385B0100 imul edi,edi,0x15B38                       ;  edi = 0x82350 = edi * 0x15b38
00408206   .  51            push ecx
00408207   .  0F80 B7050000 jo AfKayAs_.004087C4                       ;  ovelflow detect
0040820D   .  FF15 0CB14000 call dword ptr ds:[<&MSVBVM50.#rtcAnsiValu>;  msvbvm50.rtcAnsiValueBstr
00408213   .  0FBFD0        movsx edx,ax                               ;  edx = 0x31
00408216   .  03FA          add edi,edx                                ;  edi = edi + edx = 0x82381
00408218   .  0F80 A6050000 jo AfKayAs_.004087C4                       ;  ovelflow detect
0040821E   .  57            push edi
0040821F   .  FF15 F4B04000 call dword ptr ds:[<&MSVBVM50.__vbaStrI4>] ;  msvbvm50.__vbaStrI4
00408225   .  8BD0          mov edx,eax                                ;  edx = eax = 0x82381 = "533377"
00408227   .  8D4D E0       lea ecx,dword ptr ss:[ebp-0x20]
0040822A   .  FF15 94B14000 call dword ptr ds:[<&MSVBVM50.__vbaStrMove>;  msvbvm50.__vbaStrMove
00408230   .  8BBD 50FFFFFF mov edi,dword ptr ss:[ebp-0xB0]            ;  edi =  0x231e37c
00408236   .  50            push eax
00408237   .  57            push edi
00408238   .  FF93 A4000000 call dword ptr ds:[ebx+0xA4]               ;  msvbvm50.74110D32
0040823E   .  85C0          test eax,eax                               ;  eax == 0 jge

004082E6   .  52            push edx                                   ;  edx = "533377"
004082E7   .  8B19          mov ebx,dword ptr ds:[ecx]                 ;  ebx = [0x2313078]
004082E9   .  FF15 74B14000 call dword ptr ds:[<&MSVBVM50.__vbaR8Str>] ;  msvbvm50.__vbaR8Str
004082EF   .  D905 08104000 fld dword ptr ds:[0x401008]                ;  ST0 = f10.0  ST1 = 533377.0
004082F5   .  833D 00904000>cmp dword ptr ds:[0x409000],0x0
004082FC   .  75 08         jnz short AfKayAs_.00408306
004082FE   .  D835 0C104000 fdiv dword ptr ds:[0x40100C]               ;  ST0 = 10.0 / 5.0 = 2.0
00408304   .  EB 0B         jmp short AfKayAs_.00408311
00408306   >  FF35 0C104000 push dword ptr ds:[0x40100C]
0040830C   .  E8 578DFFFF   call <jmp.&MSVBVM50._adj_fdiv_m32>
00408311   >  83EC 08       sub esp,0x8                                ;  esp = esp - 0x8 = 0x19f06c
00408314   .  DFE0          fstsw ax                                   ;  eax = 0x3900
00408316   .  A8 0D         test al,0xD
00408318   .  0F85 A1040000 jnz AfKayAs_.004087BF
0040831E   .  DEC1          faddp st(1),st                             ;  ST0 = ST0 + ST1 = 533377.0 + 2.0 = 533379.0
00408320   .  DFE0          fstsw ax                                   ;  eax = 0x3900
00408322   .  A8 0D         test al,0xD
00408324   .  0F85 95040000 jnz AfKayAs_.004087BF
0040832A   .  DD1C24        fstp qword ptr ss:[esp]
0040832D   .  FF15 48B14000 call dword ptr ds:[<&MSVBVM50.__vbaStrR8>] ;  msvbvm50.__vbaStrR8
00408333   .  8BD0          mov edx,eax                                ;  edx = eax = "533379"
00408335   .  8D4D E4       lea ecx,dword ptr ss:[ebp-0x1C]
00408338   .  FF15 94B14000 call dword ptr ds:[<&MSVBVM50.__vbaStrMove>;  msvbvm50.__vbaStrMove
0040833E   .  899D 34FFFFFF mov dword ptr ss:[ebp-0xCC],ebx
00408344   .  8B9D 58FFFFFF mov ebx,dword ptr ss:[ebp-0xA8]
0040834A   .  50            push eax
0040834B   .  8B85 34FFFFFF mov eax,dword ptr ss:[ebp-0xCC]            ;  eax = [0x2313078]
00408351   .  53            push ebx
00408352   .  FF90 A4000000 call dword ptr ds:[eax+0xA4]
00408358   .  85C0          test eax,eax

004083F2   .  52            push edx                                   ;  edx = "533379"
004083F3   .  8B19          mov ebx,dword ptr ds:[ecx]
004083F5   .  FF15 74B14000 call dword ptr ds:[<&MSVBVM50.__vbaR8Str>] ;  msvbvm50.__vbaR8Str
004083FB   .  DC0D 10104000 fmul qword ptr ds:[0x401010]               ;  ST0 = 1600137.0 = 533379.0 * 3
00408401   .  83EC 08       sub esp,0x8
00408404   .  DC25 18104000 fsub qword ptr ds:[0x401018]               ;  STO = 1600135.0 = ST0 - 2.0
0040840A   .  DFE0          fstsw ax                                   ;  eax = 0x3900
0040840C   .  A8 0D         test al,0xD
0040840E   .  0F85 AB030000 jnz AfKayAs_.004087BF
00408414   .  DD1C24        fstp qword ptr ss:[esp]
00408417   .  FF15 48B14000 call dword ptr ds:[<&MSVBVM50.__vbaStrR8>] ;  msvbvm50.__vbaStrR8
0040841D   .  8BD0          mov edx,eax                                ;  edx = eax = "1600135"
0040841F   .  8D4D E4       lea ecx,dword ptr ss:[ebp-0x1C]
00408422   .  FF15 94B14000 call dword ptr ds:[<&MSVBVM50.__vbaStrMove>;  msvbvm50.__vbaStrMove
00408428   .  899D 2CFFFFFF mov dword ptr ss:[ebp-0xD4],ebx
0040842E   .  8B9D 58FFFFFF mov ebx,dword ptr ss:[ebp-0xA8]
00408434   .  50            push eax
00408435   .  8B85 2CFFFFFF mov eax,dword ptr ss:[ebp-0xD4]
0040843B   .  53            push ebx
0040843C   .  FF90 A4000000 call dword ptr ds:[eax+0xA4]
00408442   .  85C0          test eax,eax

004084DC   .  52            push edx                                   ;  edx = "1600135"
004084DD   .  8B19          mov ebx,dword ptr ds:[ecx]
004084DF   .  FF15 74B14000 call dword ptr ds:[<&MSVBVM50.__vbaR8Str>] ;  msvbvm50.__vbaR8Str
004084E5   .  DC25 20104000 fsub qword ptr ds:[0x401020]               ;  ST0 = 1600150.0 = ST0 - (-15.0)
004084EB   .  83EC 08       sub esp,0x8
004084EE   .  DFE0          fstsw ax                                   ;  eax = 0x3900
004084F0   .  A8 0D         test al,0xD
004084F2   .  0F85 C7020000 jnz AfKayAs_.004087BF
004084F8   .  DD1C24        fstp qword ptr ss:[esp]
004084FB   .  FF15 48B14000 call dword ptr ds:[<&MSVBVM50.__vbaStrR8>] ;  msvbvm50.__vbaStrR8
00408501   .  8BD0          mov edx,eax                                ;  edx = eax = "1600150"
00408503   .  8D4D E4       lea ecx,dword ptr ss:[ebp-0x1C]
00408506   .  FF15 94B14000 call dword ptr ds:[<&MSVBVM50.__vbaStrMove>;  msvbvm50.__vbaStrMove
0040850C   .  899D 24FFFFFF mov dword ptr ss:[ebp-0xDC],ebx
00408512   .  8B9D 58FFFFFF mov ebx,dword ptr ss:[ebp-0xA8]
00408518   .  50            push eax
00408519   .  8B85 24FFFFFF mov eax,dword ptr ss:[ebp-0xDC]
0040851F   .  53            push ebx
00408520   .  FF90 A4000000 call dword ptr ds:[eax+0xA4]
00408526   .  85C0          test eax,eax

'''