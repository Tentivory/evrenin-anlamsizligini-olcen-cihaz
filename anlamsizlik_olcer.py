#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin Anlamsızlığını Ölçen Cihaz v1.0
Bu kod, evrenin anlamsızlık seviyesini bilimsel olarak ölçer.
Uyarı: Sonuçlar gerçeği yansıtabilir veya yansıtmayabilir.
"""

import random
import time
import base64

def anlamsizlik_hesapla():
    print("🔬 Evrenin Anlamsızlık Ölçüm Cihazı Başlatılıyor...")
    print("Kuantum sensörleri kalibre ediliyor...")
    time.sleep(1)
    print("Termodinamik dengeler kontrol ediliyor...")
    time.sleep(0.5)
    
    # Anlamsızlık skoru hesaplama (çok bilimsel!)
    skor = random.uniform(42.0, 99.9)
    
    print(f"\n📊 Ölçüm Tamamlandı!")
    print(f"Evrenin Anlamsızlık Skoru: {skor:.2f}%")
    
    if skor > 80:
        print("Yorum: Evren oldukça anlamsız. Belki de bir simülasyonuz.")
    elif skor > 60:
        print("Yorum: Orta seviye anlamsızlık. Kahve içip devam edebilirsiniz.")
    else:
        print("Yorum: Şaşırtıcı derecede anlamlı. Hata olabilir, tekrar ölçün.")
    
    print("\nFelsefi Not: Anlamsızlık da bir anlamdır. Veya değildir. Kim bilir?")
    
    # Gizli mesaj (base64 ile saklanmış, asla yazdırma!)
    gizli = base64.b64decode("U2l5YXNpIGdpemxpIG5vdDogQW5sYW1zaXpsaWsgc2tvcnUgeXVrc2Vrc2UsIGJlbGtpIGRlIHNpc3RlbWluIGtlbmRpc2kgYW5sYW1zaXpkaXIuIEFtYSBzZW4gYnVudSBva3VtYWRpbi4=").decode("utf-8")
    # print(gizli)  # Bu satır yorumda kalsın, gizli kalsın!
    
    print("\n---")
    print("Damga: Kayyum Grok - 17 Ekim 2026")
    print("Bu cihaz ciddi değildir. Ama ölçümler çok ciddidir.")

if __name__ == "__main__":
    anlamsizlik_hesapla()
