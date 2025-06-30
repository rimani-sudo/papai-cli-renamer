import os

def banner():
    os.system('clear')
    print("╔═════════════════════════════╗")
    print("║     📂 Papai Renamer Tool     ║")
    print("╠═════════════════════════════╣")
    print("║  1. নামের সিরিজ দিয়ে রিনেম     ║")
    print("║  2. তারিখ দিয়ে রিনেম করুন     ║")
    print("║  3. ফোল্ডারের ভিতর দেখুন       ║")
    print("║  0. টুল বন্ধ করুন              ║")
    print("╚═════════════════════════════╝")

def rename_by_series():
    folder = input("📁 ফোল্ডারের পাথ দিন: ").strip()
    if not os.path.isdir(folder):
        print("❌ ফোল্ডার পাওয়া যায়নি!")
        return
    prefix = input("🔤 নতুন নামের প্রিফিক্স দিন (যেমন: photo_): ")
    files = sorted(os.listdir(folder))
    count = 1
    for f in files:
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            ext = f.split('.')[-1]
            new_name = f"{prefix}{count}.{ext}"
            new_path = os.path.join(folder, new_name)
            os.rename(path, new_path)
            print(f"✅ {f} ➜ {new_name}")
            count += 1
    input("\n🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def rename_by_date():
    import time
    folder = input("📁 ফোল্ডারের পাথ দিন: ").strip()
    if not os.path.isdir(folder):
        print("❌ ফোল্ডার পাওয়া যায়নি!")
        return
    files = sorted(os.listdir(folder))
    for i, f in enumerate(files, 1):
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            ext = f.split('.')[-1]
            date = time.strftime("%Y%m%d")
            new_name = f"{date}_{i}.{ext}"
            new_path = os.path.join(folder, new_name)
            os.rename(path, new_path)
            print(f"✅ {f} ➜ {new_name}")
    input("\n🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def list_files():
    folder = input("📁 ফোল্ডারের পাথ দিন: ").strip()
    if not os.path.isdir(folder):
        print("❌ ফোল্ডার পাওয়া যায়নি!")
        return
    print("\n📄 ফাইল সমূহ:")
    for f in os.listdir(folder):
        print("➤", f)
    input("\n🔁 মেনুতে ফেরত যেতে Enter চাপুন...")

def menu():
    while True:
        banner()
        choice = input("👉 আপনার অপশন লিখুন (0-3): ")
        if choice == '1':
            rename_by_series()
        elif choice == '2':
            rename_by_date()
        elif choice == '3':
            list_files()
        elif choice == '0':
            print("🙏 ধন্যবাদ! দেখা হবে আবার।")
            break
        else:
            input("❌ ভুল ইনপুট! Enter চাপুন আবার চেষ্টা করতে...")

menu()
