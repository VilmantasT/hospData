let allData = [["1555","32979            EGLĖ PATKAUSKIENĖ","12","2020-06-30"],["1579","16587            ROLANDAS JANULAITIS","2","2020-06-30"],["1583","31769            NERIJUS UBARTAS","26","2020-06-30"],["1584","16021            LAISVUTĖ BALTRŪNAITĖ","1","2020-06-30"],["1598","24200            AUDRONĖ BUKAUSKIENĖ","2","2020-06-30"],["1602","275            BANGUOLĖ TEODORA KVEDARAVIČIENĖ","23","2020-06-30"],["1602","146            DANGYRAS ČIUPLINSKAS","5","2020-06-30"],["1602","16587            ROLANDAS JANULAITIS","1","2020-06-30"],["1603","305            ELENA ŠAKELIENĖ","3","2020-06-30"],["1610","146            DANGYRAS ČIUPLINSKAS","46","2020-06-30"],["1617","287            ZENONAS NARIČIUS","1","2020-06-30"],["1623","262            VITALIJA JUKONIENĖ","1","2020-06-30"],["1679","32979            EGLĖ PATKAUSKIENĖ","0","2020-06-30"],["2701","146            DANGYRAS ČIUPLINSKAS","2","2020-06-30"],["2701","287            ZENONAS NARIČIUS","7","2020-06-30"],["2702","32979            EGLĖ PATKAUSKIENĖ","12","2020-06-30"],["2737","276            OLGERTAS KVEDARAVIČIUS","1","2020-06-30"],["2737","33038            MARTYNAS TUMONIS","5","2020-06-30"],["2738","33358            INDRĖ DAGIENĖ","12","2020-06-30"],["2838","12331            LEONIDAS SOLOGUBOVAS","1","2020-06-30"],["2838","13956            VALDAS MIKALSKIS","6","2020-06-30"],["2838","146            DANGYRAS ČIUPLINSKAS","1","2020-06-30"],["2838","33358            INDRĖ DAGIENĖ","4","2020-06-30"],["2838","16021            LAISVUTĖ BALTRŪNAITĖ","1","2020-06-30"],["2838","262            VITALIJA JUKONIENĖ","2","2020-06-30"],["2838","26538            RENATA VAIČIULIENĖ","8","2020-06-30"],["2838","34260            MANTAS ŽIBAS","6","2020-06-30"],["3072","26538            RENATA VAIČIULIENĖ","1","2020-06-30"],["3238","16587            ROLANDAS JANULAITIS","2","2020-06-30"],["3238","31769            NERIJUS UBARTAS","1","2020-06-30"],["3239","16587            ROLANDAS JANULAITIS","2","2020-06-30"],["3239","31769            NERIJUS UBARTAS","3","2020-06-30"],["3241","32467            INDRĖ KERŠULYTĖ","0","2020-06-30"],["3300","32979            EGLĖ PATKAUSKIENĖ","8","2020-06-30"],["3324","13956            VALDAS MIKALSKIS","4","2020-06-30"],["3516","26538            RENATA VAIČIULIENĖ","7","2020-06-30"],["3516","146            DANGYRAS ČIUPLINSKAS","1","2020-06-30"],["3516","16020            EGIDIJUS GAIGALAS","2","2020-06-30"],["3516","255            DALIUS JAKUBĖNAS","3","2020-06-30"],["3516","262            VITALIJA JUKONIENĖ","1","2020-06-30"],["3516","276            OLGERTAS KVEDARAVIČIUS","2","2020-06-30"],["3516","305            ELENA ŠAKELIENĖ","3","2020-06-30"],["3516","32467            INDRĖ KERŠULYTĖ","2","2020-06-30"],["3516","33038            MARTYNAS TUMONIS","3","2020-06-30"],["3517","16587            ROLANDAS JANULAITIS","1","2020-06-30"],["3517","255            DALIUS JAKUBĖNAS","1","2020-06-30"],["3517","26538            RENATA VAIČIULIENĖ","2","2020-06-30"],["3517","276            OLGERTAS KVEDARAVIČIUS","1","2020-06-30"],["3517","30468            LAURA GABRĖNIENĖ","1","2020-06-30"],["3517","305            ELENA ŠAKELIENĖ","2","2020-06-30"],["3517","31769            NERIJUS UBARTAS","3","2020-06-30"],["3519","12331            LEONIDAS SOLOGUBOVAS","1","2020-06-30"],["3519","146            DANGYRAS ČIUPLINSKAS","4","2020-06-30"],["3519","16587            ROLANDAS JANULAITIS","3","2020-06-30"],["3519","255            DALIUS JAKUBĖNAS","2","2020-06-30"],["3519","276            OLGERTAS KVEDARAVIČIUS","7","2020-06-30"],["3519","31769            NERIJUS UBARTAS","2","2020-06-30"],["3519","32467            INDRĖ KERŠULYTĖ","6","2020-06-30"],["3519","33038            MARTYNAS TUMONIS","8","2020-06-30"],["3520","14028            AURELIJA MENKELIŪNIENĖ","1","2020-06-30"],["3520","255            DALIUS JAKUBĖNAS","1","2020-06-30"],["3520","26538            RENATA VAIČIULIENĖ","2","2020-06-30"],["3520","305            ELENA ŠAKELIENĖ","3","2020-06-30"],["3520","31769            NERIJUS UBARTAS","5","2020-06-30"],["3520","32467            INDRĖ KERŠULYTĖ","1","2020-06-30"],["3520","33038            MARTYNAS TUMONIS","1","2020-06-30"],["3520","34260            MANTAS ŽIBAS","0","2020-06-30"],["3680","32979            EGLĖ PATKAUSKIENĖ","19","2020-06-30"],["3716","262            VITALIJA JUKONIENĖ","2","2020-06-30"],["1579","31769            NERIJUS UBARTAS","7","2020-06-30"],["1583","16021            LAISVUTĖ BALTRŪNAITĖ","37","2020-06-30"],["1583","24200            AUDRONĖ BUKAUSKIENĖ","9","2020-06-30"],["1583","275            BANGUOLĖ TEODORA KVEDARAVIČIENĖ","10","2020-06-30"],["1583","305            ELENA ŠAKELIENĖ","26","2020-06-30"],["1584","146            DANGYRAS ČIUPLINSKAS","5","2020-06-30"],["1584","287            ZENONAS NARIČIUS","1","2020-06-30"],["1598","262            VITALIJA JUKONIENĖ","2","2020-06-30"],["1602","12331            LEONIDAS SOLOGUBOVAS","1","2020-06-30"],["1602","255            DALIUS JAKUBĖNAS","12","2020-06-30"],["1602","276            OLGERTAS KVEDARAVIČIUS","9","2020-06-30"],["1602","32467            INDRĖ KERŠULYTĖ","1","2020-06-30"],["1602","33038            MARTYNAS TUMONIS","23","2020-06-30"],["1603","33358            INDRĖ DAGIENĖ","3","2020-06-30"],["1610","371            ALDONA ELENA AUKŠTIKALNIENĖ","31","2020-06-30"],["1610","5437            LOLITA ČEPONIENĖ","46","2020-06-30"],["1617","311            MARIJA VALAITIENĖ","1","2020-06-30"],["1617","5017            SOFIJA NIJOLĖ BORTKEVIČIENĖ","1","2020-06-30"],["1623","10813            VIDA GASIŪNIENĖ","0","2020-06-30"],["1623","13956            VALDAS MIKALSKIS","0","2020-06-30"],["1623","26538            RENATA VAIČIULIENĖ","1","2020-06-30"],["1623","30468            LAURA GABRĖNIENĖ","1","2020-06-30"],["1623","34260            MANTAS ŽIBAS","1","2020-06-30"],["2838","16020            EGIDIJUS GAIGALAS","4","2020-06-30"],["3324","24686            JURGITA AUGUSTINAVIČIENĖ","4","2020-06-30"],["3516","14028            AURELIJA MENKELIŪNIENĖ","2","2020-06-30"],["3516","15204            SIGUTĖ GOBIENĖ","1","2020-06-30"],["3516","246            ALGIMANTAS GAILIŪNAS","2","2020-06-30"],["3517","283            RITA MACIENĖ","1","2020-06-30"]]