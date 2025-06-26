import time
import random
import sys
from itertools import cycle

class Renkler:
    KIRMIZI = '\033[91m'
    YEŞİL = '\033[92m'
    SARI = '\033[93m'
    MAVİ = '\033[94m'
    PEMBE = '\033[95m'
    CYAN = '\033[96m'
    KALIN = '\033[1m'
    ALT_ÇİZGİ = '\033[4m'
    SON = '\033[0m'

def yavaş_yazı(text, gecikme=0.01, yeni_satır=True, renk=None):
    if renk:
        print(renk, end='', flush=True)
    for harf in text:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    if yeni_satır:
        print()
    if renk:
        print(Renkler.SON, end='', flush=True)

def dosya_silme_animasyonu():
    sistem_dizinleri = [
        "/bin", "/sbin", "/usr/bin", "/usr/sbin", "/usr/local/bin",
        "/lib", "/lib64", "/usr/lib", "/usr/lib64", "/etc",
        "/var", "/tmp", "/root", "/home", "/boot",
        "/dev", "/proc", "/sys", "/opt", "/mnt", "/media"
    ]

    dosya_tipleri = [
        ("lib", ".so", ".a"),
        ("conf", ".conf", ".cfg"),
        ("log", ".log", ""),
        ("cache", ".cache", ""),
        ("tmp", ".tmp", ""),
        ("init", "", ""),
        ("db", ".db", ".sqlite"),
        ("py", ".py", ""),
        ("sh", ".sh", "")
    ]

    animasyon = cycle(["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"])
    toplam_dosya = random.randint(15000, 25000)
    silinen = 0

    yavaş_yazı(f"\n{Renkler.MAVİ}Dosya sistemi taranıyor... {toplam_dosya} dosya bulundu{Renkler.SON}", 0.01)
    time.sleep(2)

    # Kritik dosyaların silinmesi
    kritik_dosyalar = [
        "/bin/bash", "/bin/sh", "/usr/bin/python",
        "/usr/bin/perl", "/usr/bin/gcc", "/usr/bin/make",
        "/etc/passwd", "/etc/shadow", "/etc/hosts",
        "/etc/fstab", "/etc/network/interfaces",
        "/boot/vmlinuz", "/boot/initrd.img",
        "/lib/systemd/systemd", "/sbin/init",
        "/usr/lib/os-release", "/var/log/syslog"
    ]

    for dosya in kritik_dosyalar:
        yavaş_yazı(f"{Renkler.KIRMIZI}Siliniyor: {dosya}{Renkler.SON}", 0.005)
        silinen += 1
        if random.random() < 0.3:
            sys.stdout.write(f"\r{next(animasyon)} {silinen}/{toplam_dosya} dosya silindi")
            sys.stdout.flush()
        time.sleep(0.02)

    # Rastgele dosya silme (ÇOOOOOOOOOK UZUN)
    while silinen < toplam_dosya:
        dizin = random.choice(sistem_dizinleri)
        tip = random.choice(dosya_tipleri)
        dosya = f"{tip[0]}_{random.randint(1, 10000)}{random.choice(tip[1:])}"
        yol = f"{dizin}/{dosya}"

        # Her 100 dosyada bir animasyon güncelle
        if silinen % 100 == 0:
            sys.stdout.write(f"\r{next(animasyon)} {silinen}/{toplam_dosya} dosya silindi")
            sys.stdout.flush()

        # %5 ihtimalle tam yolu göster
        if random.random() < 0.05:
            yavaş_yazı(f"{Renkler.KIRMIZI}Siliniyor: {yol}{Renkler.SON}", 0.001)

        silinen += 1
        time.sleep(0.001)

    sys.stdout.write(f"\r{' ' * 50}\r")
    sys.stdout.flush()
    yavaş_yazı(f"{Renkler.KIRMIZI}\nToplam {silinen} dosya başarıyla silindi{Renkler.SON}", 0.03)

def sistem_çöküşü():
    hata_mesajları = [
        "Kernel panic - not syncing: VFS: Unable to mount root fs",
        "BUG: unable to handle kernel NULL pointer dereference",
        "systemd[1]: Failed to start Login Service",
        "EXT4-fs error (device sda1): ext4_find_entry: reading directory",
        "XFS (sda1): Metadata corruption detected",
        "sd 0:0:0:0: [sda] tag#0 FAILED Result: hostbyte=DID_BAD_TARGET",
        "Watchdog detected hard LOCKUP on cpu 3",
        "NETDEV WATCHDOG: eth0 (e1000e): transmit queue 0 timed out",
        "ata1.00: exception Emask 0x0 SAct 0x0 SErr 0x0 action 0x6 frozen",
        "thermal thermal_zone0: critical temperature reached (110 C)"
    ]

    for _ in range(25):
        hata = random.choice(hata_mesajları)
        yavaş_yazı(f"{Renkler.KIRMIZI}{hata}{Renkler.SON}", 0.01)
        time.sleep(0.1)

    yavaş_yazı(f"\n{Renkler.KIRMIZI}{Renkler.KALIN}KRİTİK HATA: Dosya sistemi çöktü{Renkler.SON}", 0.05)
    time.sleep(1)

    # Dramatik çöküş animasyonu
    for i in range(10, 0, -1):
        yavaş_yazı(f"{Renkler.KIRMIZI}Sistem kapanıyor... {i}{Renkler.SON}", 0.1, True)
        time.sleep(0.3)

    print(f"{Renkler.KIRMIZI}{Renkler.KALIN}", end='')
    for _ in range(15):
        print("".join(random.choices("01!@#$%^&*()_+-=[]{}|;':\",./<>?\\", k=80)))
        time.sleep(0.05)
    print(Renkler.SON)

    yavaş_yazı("\nSİSTEM ÇÖKTÜ", 0.1)
    time.sleep(2)

def ana_program():
    # Komut girişi
    yavaş_yazı(f"{Renkler.SARI}user@pc:~$ {Renkler.SON}", False)
    yavaş_yazı("sudo rm -rf /*", 0.1)
    time.sleep(0.5)

    # Şifre girişi
    yavaş_yazı(f"{Renkler.KIRMIZI}[sudo] password for user: {Renkler.SON}", False)
    time.sleep(1)
    for _ in range(8):
        print("*", end='', flush=True)
        time.sleep(random.uniform(0.05, 0.15))
    print()
    time.sleep(0.5)
    yavaş_yazı(f"{Renkler.YEŞİL}Yetki verildi{Renkler.SON}", 0.03)
    time.sleep(1)

    # Uzun uzun dosya silme
    dosya_silme_animasyonu()

    # Sistem çöküşü
    sistem_çöküşü()

    # Uyarı
    yavaş_yazı(f"\n{Renkler.YEŞİL}{Renkler.KALIN}UYARI:{Renkler.SON}", 0.05)
    yavaş_yazı(f"{Renkler.YEŞİL}Bu sadece bir simülasyondur. Hiçbir dosya silinmedi.{Renkler.SON}", 0.03)
    yavaş_yazı(f"{Renkler.YEŞİL}Gerçek sistemlerde 'sudo rm -rf /*' KULLANMAYIN!{Renkler.SON}", 0.03)

if __name__ == "__main__":
    ana_program()