name = input()
serial = ord(name[0]) * 0x29 * 0x2
'serial = serial + serial'
print(f"CW-{serial}-CRACKED")

'''
0042FA82  |.  E8 D1AFFEFF   call Acid_bur.0041AA58
0042FA87  |.  8B45 F0       mov eax,[local.4]                        ;  eax = "123456"
0042FA8A  |.  0FB600        movzx eax,byte ptr ds:[eax]              ;  eax = 0x31
0042FA8D  |.  F72D 50174300 imul dword ptr ds:[0x431750]             ;  eax = eax * [0x431750] = 0x7d9 = eax * 0x29
0042FA93  |.  A3 50174300   mov dword ptr ds:[0x431750],eax          ;  [0x431750] = eax = 0x7d9
0042FA98  |.  A1 50174300   mov eax,dword ptr ds:[0x431750]          ;  eax = [0x431750] = 0x7d9
0042FA9D  |.  0105 50174300 add dword ptr ds:[0x431750],eax          ;  [0x431750] = [0x431750] + eax = 0xFB2 = 4018
0042FAA3  |.  8D45 FC       lea eax,[local.1]
0042FAA6  |.  BA ACFB4200   mov edx,Acid_bur.0042FBAC                ;  CW
0042FAAB  |.  E8 583CFDFF   call Acid_bur.00403708
0042FAB0  |.  8D45 F8       lea eax,[local.2]
0042FAB3  |.  BA B8FB4200   mov edx,Acid_bur.0042FBB8                ;  CRACKED
0042FAB8  |.  E8 4B3CFDFF   call Acid_bur.00403708
0042FABD  |.  FF75 FC       push [local.1]                           ;  Acid_bur.0042FBAC
0042FAC0  |.  68 C8FB4200   push Acid_bur.0042FBC8                   ;  -
0042FAC5  |.  8D55 E8       lea edx,[local.6]
0042FAC8  |.  A1 50174300   mov eax,dword ptr ds:[0x431750]          ;  eax = 0xFB2 = 4018
0042FACD  |.  E8 466CFDFF   call Acid_bur.00406718
0042FAD2  |.  FF75 E8       push [local.6]
0042FAD5  |.  68 C8FB4200   push Acid_bur.0042FBC8                   ;  -
0042FADA  |.  FF75 F8       push [local.2]                           ;  Acid_bur.0042FBB8
0042FADD  |.  8D45 F4       lea eax,[local.3]
0042FAE0  |.  BA 05000000   mov edx,0x5
0042FAE5  |.  E8 C23EFDFF   call Acid_bur.004039AC
0042FAEA  |.  8D55 F0       lea edx,[local.4]
0042FAED  |.  8B83 E0010000 mov eax,dword ptr ds:[ebx+0x1E0]
0042FAF3  |.  E8 60AFFEFF   call Acid_bur.0041AA58
0042FAF8  |.  8B55 F0       mov edx,[local.4]                        ;  edx = "111111"
0042FAFB  |.  8B45 F4       mov eax,[local.3]                        ;  eax = "CW-4018-CRACKED"
0042FAFE  |.  E8 F93EFDFF   call Acid_bur.004039FC
0042FB03      75 1A         jnz short Acid_bur.0042FB1F              ;  jump not zero 
'''