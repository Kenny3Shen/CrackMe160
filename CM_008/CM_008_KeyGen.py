print("SynTaX 2oo1")

'''
00401D73   .  51            push ecx                                 ;  ecx = Key
00401D74   .  68 541A4000   push Andréna.00401A54                    ;  UNICODE "SynTaX 2oo1"
00401D79   .  FF15 08314000 call dword ptr ds:[<&MSVBVM50.__vbaStrCm>;  msvbvm50.__vbaStrCmp
00401D7F   .  8BF8          mov edi,eax                              ;  Andréna.00401870
00401D81   .  8D4D D8       lea ecx,dword ptr ss:[ebp-0x28]
00401D84   .  F7DF          neg edi
00401D86   .  1BFF          sbb edi,edi
00401D88   .  47            inc edi
00401D89   .  F7DF          neg edi
00401D8B   .  FF15 5C314000 call dword ptr ds:[<&MSVBVM50.__vbaFreeS>;  msvbvm50.__vbaFreeStr
00401D91   .  8D4D D4       lea ecx,dword ptr ss:[ebp-0x2C]
00401D94   .  FF15 60314000 call dword ptr ds:[<&MSVBVM50.__vbaFreeO>;  msvbvm50.__vbaFreeObj
00401D9A   .  66:3BFE       cmp di,si
00401D9D      0F84 A0000000 je Andréna.00401E43                      ;  key jump

'''
