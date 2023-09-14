import os

def convert_video_to_mp3(video_path, output_folder):
    video_name = os.path.splitext(os.path.basename(video_path))[0]  # Video ismini uzantısız alma
    output_path = os.path.join(output_folder, f"{video_name}.mp3")  # Video ismini mp3 uzantısına aktarma

    os.makedirs(output_folder, exist_ok=True)  # Klasörü oluştur

    ffmpeg_cmd = f'ffmpeg -i "{video_path}" -vn -acodec libmp3lame "{output_path}"'
    os.system(ffmpeg_cmd)

def convert_videos_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith((".mp4", ".avi", ".mkv")):
                video_path = os.path.join(root, file)
                convert_video_to_mp3(video_path, output_folder)

def main():
    while True:
        print("1. Tek bir videoyu MP3'e dönüştür")
        print("2. Bir klasördeki tüm videoları MP3'e dönüştür")
        print("3. Çıkış")

        choice = input("Seçiminizi yapın (1/2/3): ")

        if choice == "1":
            video_path = input("Çevrilecek video dosyasının konumunu girin: ")
            if video_path.lower() == "exit":
                break
            output_folder = input("MP3 dosyasının kaydedileceği klasörü girin: ")
            convert_video_to_mp3(video_path, output_folder)
        elif choice == "2":
            input_folder = input("Klasörün konumunu girin: ")
            if input_folder.lower() == "exit":
                break
            convert_videos_in_folder(input_folder, os.path.join(input_folder, "mp3"))
        elif choice == "3":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
