import argparse
import sys
from pathlib import Path

# Add parent directory to path to import hash_analyzer
sys.path.append(str(Path(__file__).parent.parent))
from hash_analysis.hash_analyzer import compute_hash, compute_hash_with_salt

def main():
    parser = argparse.ArgumentParser(description='Hash Analiz Aracı CLI')
    subparsers = parser.add_subparsers(dest='command', help='Komutlar')

    # Hash hesaplama komutu
    hash_parser = subparsers.add_parser('hash', help='Hash hesaplama')
    hash_parser.add_argument('password', help='Hash değeri hesaplanacak parola')
    hash_parser.add_argument('--algorithm', '-a', choices=['md5', 'sha1', 'sha256'],
                           default='md5', help='Hash algoritması (varsayılan: md5)')
    hash_parser.add_argument('--salt', '-s', help='Salt değeri (opsiyonel)')

    # Hash analizi komutu
    analyze_parser = subparsers.add_parser('analyze', help='Hash analizi')
    analyze_parser.add_argument('hash', help='Analiz edilecek hash değeri')
    analyze_parser.add_argument('--algorithm', '-a', choices=['md5', 'sha1', 'sha256'],
                              help='Hash algoritması (otomatik tespit edilemezse belirtilmeli)')

    args = parser.parse_args()

    if args.command == 'hash':
        if args.salt:
            result = compute_hash_with_salt(args.password, args.salt, args.algorithm)
            print(f"Parola: {args.password}")
            print(f"Salt: {args.salt}")
            print(f"{args.algorithm.upper()} hash: {result}")
        else:
            result = compute_hash(args.password, args.algorithm)
            print(f"Parola: {args.password}")
            print(f"{args.algorithm.upper()} hash: {result}")

    elif args.command == 'analyze':
        # TODO: Hash analizi özelliklerini ekle
        print(f"Hash analizi özelliği henüz eklenmedi: {args.hash}")
        if args.algorithm:
            print(f"Belirtilen algoritma: {args.algorithm}")

    else:
        parser.print_help()

if __name__ == '__main__':
    main() 