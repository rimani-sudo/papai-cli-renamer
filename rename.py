import os
import time

def banner():
    os.system('clear')
    print("╔═════════════════════════════════════╗")
    print("║     📂 Papai Renamer Tool (v2.0)     ║")
    print("╠═════════════════════════════════════╣")
    print("║  1. সিরিজ দিয়ে রিনেম করুন              ║")
    print("║  2. তারিখ দিয়ে রিনেম করুন             ║")
    print("║  3. ফাইল লিস্ট দেখুন                   ║")
    print("║  4. শুধু .jpg/.mp4 টাইপ ফাইল রিনেম   ║")
    print("║  5. নামের শেষে টাইমস্ট্যাম্প যোগ করুন ║")
    print("║  0. টুল বন্ধ করুন                      ║")
    print("╚═════════════════════════════════════╝")

def get_folder():
    folder = input("📁 ফোল্ডারের পাথ দিন: ").strip()
    if not os.path.isdir(folder):
        print("❌ ফোল্ডার পাওয়া যায়নি!")
        return None
    return folder

def rename_by_series():
    folder = get_folder()
    if not folder: return
    prefix = input("🔤 নামের প্রিফিক্স দিন (photo_): ")
    files = sorted(os.listdir(folder))
    count = 1
    for f in files:
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            ext = f.split('.')[-1]
            new_name = f"{prefix}{count}.{ext}"
            os.rename(path, os.path.join(folder, new_name))
            print(f"✅ {f} ➜ {new_name}")
            count += 1
    input("🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def rename_by_date():
    folder = get_folder()
    if not folder: return
    date = time.strftime("%Y%m%d")
    files = sorted(os.listdir(folder))
    for i, f in enumerate(files, 1):
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            ext = f.split('.')[-1]
            new_name = f"{date}_{i}.{ext}"
            os.rename(path, os.path.join(folder, new_name))
            print(f"✅ {f} ➜ {new_name}")
    input("🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def list_files():
    folder = get_folder()
    if not folder: return
    print("\n📄 ফাইল লিস্ট:")
    for f in os.listdir(folder):
        print("➤", f)
    input("\n🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def rename_by_extension():
    folder = get_folder()
    if not folder: return
    ext_filter = input("🎯 কোন এক্সটেনশন ফাইল রিনেম করবেন? (ex: jpg/mp4): ").strip()
    prefix = input("🔤 নতুন প্রিফিক্স দিন (ex: edited_): ")
    files = [f for f in os.listdir(folder) if f.endswith(f".{ext_filter}")]
    for i, f in enumerate(files, 1):
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            new_name = f"{prefix}{i}.{ext_filter}"
            os.rename(path, os.path.join(folder, new_name))
            print(f"✅ {f} ➜ {new_name}")
    input("🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def rename_with_timestamp():
    folder = get_folder()
    if not folder: return
    files = sorted(os.listdir(folder))
    for f in files:
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            ext = f.split('.')[-1]
            timestamp = time.strftime("%H%M%S")
            name_only = os.path.splitext(f)[0]
            new_name = f"{name_only}_{timestamp}.{ext}"
            os.rename(path, os.path.join(folder, new_name))
            print(f"✅ {f} ➜ {new_name}")
    input("🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def menu():
    while True:
        banner()
        choice = input("👉 অপশন দিন (0-5): ")
        if choice == '1':
            rename_by_series()
        elif choice == '2':
            rename_by_date()
        elif choice == '3':
            list_files()
        elif choice == '4':
            rename_by_extension()
        elif choice == '5':
            rename_with_timestamp()
        elif choice == '0':
            print("🙏 ধন্যবাদ Papai Tool ব্যবহার করার জন্য!")
            break
        else:
            input("❌ ভুল অপশন! আবার চেষ্টা করুন...")

menu()
