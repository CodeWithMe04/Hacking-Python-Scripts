import hashlib

def convert_text_to_sha1(text):
    process = hashlib.sha1(
        text.encode()
    ).hexdigest()

    return process

def main():
    user_sha = input("Enter the SHA1 to crack:  ")
    cleaned_user_sha1 = user_sha.strip().lower()

    with open('./password.txt') as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password)

            if cleaned_user_sha1 == converted_sha1:
                print(f"Password found: {password}")
                return
            
    print("Could not found Password")

if __name__ == '__main__':
    main()