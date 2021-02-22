from rest_framework import serializers
import gnupg
gnupghome="/home/janak/.gnupg"
# gnupghome="/root/.gnupg"

class DecryptMessageSerializer(serializers.Serializer):
    passphrase = serializers.CharField()
    message = serializers.CharField()

    def validate(self, data):
        passphrase = data.get("schedule")
        if passphrase == '':
            raise serializers.ValidationError(
                {"message": "Please provide passphrase" }
            )
        return data

    def decrypt_message(self):
        gpg = gnupg.GPG(gnupghome=gnupghome)
        print("\n\n=======================================")
        print("meessage = ", str(self.data['message']))
        decrypted_data = gpg.decrypt(str(self.data['message']), passphrase="janak")
        print(decrypted_data.ok)
        print(decrypted_data.status)
        print(decrypted_data.stderr)
        print(decrypted_data)
        return decrypted_data



class encryptMessageSerializer(serializers.Serializer):
    passphrase = serializers.CharField()
    message = serializers.CharField()

    def validate(self, data):
        passphrase = data.get("schedule")
        if passphrase == '':
            raise serializers.ValidationError(
                {"message": "Please provide passphrase" }
            )
        return data

    def encrypt_message(self):
        gpg = gnupg.GPG(gnupghome=gnupghome)
        encrypted_data = gpg.encrypt(self.data['message'], 'janak@gmail.com')
        res = {
            "ok": encrypted_data.ok,
            "status": encrypted_data.status,
            "stderr": encrypted_data.stderr,
            "encrypted_str": str(encrypted_data)
        }
        decrypted_data = gpg.decrypt(res['encrypted_str'], passphrase='janak')
        res['decrypted_str'] = decrypted_data.data
        print("\n\n=======================================\n\n\n")
        print(res)
        return res

