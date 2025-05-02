import os

def fix_label_files(labels_path):
    if not os.path.exists(labels_path):
        print("❌ Folder tidak ditemukan:", labels_path)
        return
    
    count = 0
    for filename in os.listdir(labels_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(labels_path, filename)
            print(f"🔧 Memproses: {filename}")
            with open(file_path, 'r') as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    parts[0] = '0'
                    new_lines.append(' '.join(parts) + '\n')

            with open(file_path, 'w') as f:
                f.writelines(new_lines)
            
            count += 1
    
    print(f"✅ Selesai memproses {count} file .txt")

# Perbaiki label di folder train dan test
train_labels = r'D:\IPB\SEMESTER 6\Viskom\bib detection project\train\labels'
test_labels = r'D:\IPB\SEMESTER 6\Viskom\bib detection project\test\labels'

print("\nMemperbaiki label training...")
fix_label_files(train_labels)
print("\nMemperbaiki label testing...")
fix_label_files(test_labels)