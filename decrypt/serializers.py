from rest_framework import serializers
import gnupg


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
        # decrypted_data = gpg.decrypt(self.data['message'])
        # print("\n\n=======================================\n\n\n")
        # print(decrypted_data)
        return 100