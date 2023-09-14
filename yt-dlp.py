import os

def download_video_with_ytdlp(video_link):
    ytdlp_cmd = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" -o "C:\\Users\\fevzi\\Desktop\\%(upload_date)s\\%(title)s [%(id)s].%(ext)s" {video_link}'
    
    print("İndirme işlemi başlatılıyor...")
    os.system(ytdlp_cmd)
    print("İndirme işlemi tamamlandı.")
    
def download_videolist_with_ytdlp(video_link):
    ytdlp_cmd = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --yes-playlist -o "C:\\Users\\fevzi\\Desktop\\Video_List\\%(upload_date)s\\%(title)s [%(id)s].%(ext)s" {video_link}'
    
    print("İndirme işlemi başlatılıyor...")
    os.system(ytdlp_cmd)
    print("İndirme işlemi tamamlandı.")
    
def download_videotxtlist_with_ytdlp(txt_link):
    txt_link = txt_link.strip('"')  # Çift tırnak işaretlerini kaldır
    if not os.path.exists(txt_link):
        print("Geçerli bir metin dosyası yolunu girmelisiniz.")
    else:
        ytdlp_cmd = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" -a {txt_link} -o "C:\\Users\\fevzi\\Desktop\\Video_Txt_List\\%(title)s [%(id)s].%(ext)s" {txt_link}'
        
        print("İndirme işlemi başlatılıyor...")
        os.system(ytdlp_cmd)
        print("İndirme işlemi tamamlandı.")

if __name__ == "__main__":
    while True:
        print("İndirme işlemi yapmak istediğiniz türü seçin:")
        print("1. Tek Video İndirme")
        print("2. Video Listesi İndirme")
        print("3. Video Listesi İndirme (Metin Dosyası Kullanarak)")
        print("4. Çıkış")
        
        choice = input("Seçiminizi yapın (1/2/3/4): ")
        
        if choice == "1":
            video_link = input("İndirilecek video linkini girin: ")
            if not video_link.startswith("http"):
                print("Geçerli bir video linki girmelisiniz.")
            else:
                download_video_with_ytdlp(video_link)
                input("Devam etmek için bir tuşa basın...")
        elif choice == "2":
            video_link = input("İndirilecek video listesi linkini girin: ")
            if not video_link.startswith("http"):
                print("Geçerli bir video listesi linki girmelisiniz.")
            else:
                download_videolist_with_ytdlp(video_link)
                input("Devam etmek için bir tuşa basın...")
        elif choice == "3":
            txt_link = input("İndirilecek video listesi metin dosyasının yolunu girin: ")
            txt_link = txt_link.strip('"')  # Çift tırnak işaretlerini kaldır
            if not os.path.exists(txt_link):
                print("Geçerli bir metin dosyası yolunu girmelisiniz.")
            else:
                download_videotxtlist_with_ytdlp(txt_link)
                input("Devam etmek için bir tuşa basın...")
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
