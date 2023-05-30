# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'ZnJvbSBpbnN0YWdyYXBpIGltcG9ydCBDbGllbnQNCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aA0KaW1wb3J0IHRpbWUNCmltcG9ydCByYW5kb20NCmltcG9ydCBvcw0KZnJvbSBkb3RlbnYgaW1wb3J0IGxvYWRfZG90ZW52DQoNCiMgTG9hZCBlbnZpcm9ubWVudCB2YXJpYWJsZXMgZnJvbSAuZW52IGZpbGUNCmxvYWRfZG90ZW52KCkNCg0KIyBSZXRyaWV2ZSB0aGUgdXNlcm5hbWUgYW5kIHBhc3N3b3JkIGZyb20gZW52aXJvbm1lbnQgdmFyaWFibGVzDQojIFJldHJpZXZlIHRoZSB1c2VybmFtZSBhbmQgcGFzc3dvcmQgZnJvbSBlbnZpcm9ubWVudCB2YXJpYWJsZXMNCnVzZXJuYW1lID0gb3MuZW52aXJvbi5nZXQoJ1VTRVJOQU1FMScpDQpwYXNzd29yZCA9IG9zLmVudmlyb24uZ2V0KCdQQVNTV09SRCcpDQpwcmludChmIlVzZXJuYW1lOiB7dXNlcm5hbWV9IikNCnByaW50KGYiUGFzc3dvcmQ6IHtwYXNzd29yZH0iKQ0KDQoNCmlmIG5vdCB1c2VybmFtZSBvciBub3QgcGFzc3dvcmQ6DQogICAgcmFpc2UgVmFsdWVFcnJvcigiUGxlYXNlIHByb3Zp'
love = 'MTHtLFO2LJkcMPO1p2IlozSgMFOuozDtpTSmp3qipzDtnJ4tqTuyVP5yoaLtMzyfMF4vXD0XQDbAPvZtD3WyLKEyVTRtpTS0nPO0olO0nTHtFyACGvOznJkyVTMipvOmLKMcozptL2kcMJ50VUAyqUEcozqmQDcjLKEbK3EiK2McoTHtCFOzVag1p2IlozSgMK0hnaAiovVAPaOuqTttCFODLKEbXUOuqTusqT9sMzyfMFxAPt0XVlOQpzIuqTHtqTuyVRyhp3EuM3WuoFOwoTyyoaDAPzAfVQ0tD2kcMJ50XPxAPt0XVlOZo2SxVTAfnJIhqPOmMKE0nJ5aplOzpz9gVTMcoTHtnJLtnKDtMKucp3EmYPOiqTuypaqcp2HtoT9anJ4tLJ5xVUAuqzHtp2I0qTyhM3ZtqT8tMzyfMD0XnJLtpTS0nP5cp19znJkyXPx6QDbtVPNtpUWcoaDbMvWZo2SxnJ5aVRAiozLto2Ltr3OuqTusqT9sMzyfMK0vXD0XVPNtVTAfYzkiLJEsp2I0qTyhM3ZbpTS0nS90o19znJkyXD0XMJkmMGbAPvNtVPOjpzyhqPtvHTkyLKAyVUqunKDuVRkiM2qcozptFJ4uVvxAPvNtVPOwoP5fo2qcovu1p2IlozSgMFjtpTSmp3qipzDcQDbtVPNtL2jhMUIgpS9mMKE0nJ5aplujLKEbK3EiK2McoTHc'
god = 'DQpwcmludCgiTG9nZ2VkIEluIFN1Y2Nlc3NmdWxseSEhIikNCg0KDQojIENyZWF0ZSBhIGxpc3Qgb2YgdXNlcnMgdG8gZm9sbG93IGFuZCB1bmZvbGxvdw0KdXNlcnNfdG9fZm9sbG93ID0gWyczOTczMTM5ODg3NicsICczMTc3MzczMTcwMScsICczMzE5MDkwOTM2MycsICc0NDA1OTk1MjY5NCcsICc0MjgxMDk0NzIzNScsICczNzg1NTcwMzAnLCAnNDg3NDAyMzcxMjcnLCAnMzAzNzg0Nzc1NicsICcxNzM1NjA0MjAnLCAnMzg5NjE0OTk1MDQnLCAnNDc2MzA5NzEyOTgnLCAnNTU2MDgzNDU3NjInXQ0KDQojIFNldCB0aGUgbWluaW11bSBhbmQgbWF4aW11bSBkZWxheSB0aW1lIGJldHdlZW4gZWFjaCBhY3Rpb24gKGluIHNlY29uZHMpDQptaW5fZGVsYXlfdGltZSA9IDgwDQptYXhfZGVsYXlfdGltZSA9IDE4MA0KDQojIERlZmluZSB0aGUgZm9sbG93IGFuZCB1bmZvbGxvdyBmdW5jdGlvbnMNCmRlZiBmb2xsb3dfdXNlcnMoKToNCiAgICBmb3IgdXNlciBpbiB1c2Vyc190b19mb2xsb3c6DQogICAgICAgIGNsLnVzZXJfZm9sbG93KHVzZXIpDQog'
destiny = 'VPNtVPNtVUOlnJ50XUImMKVcQDbtVPNtVPNtVUEcoJHhp2kyMKNbpzShMT9gYaIhnJMipz0boJyhK2EyoTS5K3EcoJHfVT1urS9xMJkurI90nJ1yXFxAPt0XMTIzVUIhMz9foT93K3ImMKWmXPx6QDbtVPNtMz9lVUImMKVtnJ4tqKAypaAsqT9sMz9foT93Bt0XVPNtVPNtVPOwoP51p2IlK3IhMz9foT93XUImMKVcQDbtVPNtVPNtVUOlnJ50XUImMKVcQDbtVPNtVPNtVUEcoJHhp2kyMKNbpzShMT9gYaIhnJMipz0boJyhK2EyoTS5K3EcoJHfVT1urS9xMJkurI90nJ1yXFxAPt0XVlOFqJ4tqTuyVTWiqPOcovOuVTkio3NAPaOlnJ50XPWPo3Dtp3EupaEyMPNfVUOfMJSmMFO3LJy0VPVcQDc3nTyfMFOHpaIyBt0XVPNtVUOlnJ50XPWUG0yBElOTG1VtEx9ZGR9KVvxAPvNtVPOzo2kfo3qsqKAypaZbXD0XVPNtVUEcoJHhp2kyMKNbpzShMT9gYaIhnJMipz0bZwxjYPN0ZQNcXD0XVPNtVUOlnJ50XPWUG0yBElOTG1VtIH5TG0kZG1pvXD0XVPNtVUIhMz9foT93K3ImMKWmXPxAPvNtVPO0nJ1yYaAfMJIjXUWuozEioF51ozyzo3WgXQV5ZPjtAQNjXFxAPt0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
