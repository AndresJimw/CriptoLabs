from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

binPrivKey = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCfQfirYVXgzT90v6SqgeID7q/WK1XaVTNGVFolDUOcrXl/egRG 4iag5tiTbrMYCQ8CSTYn7q0U4AmBXihlbWDqf6MMk6OEoDxdWZTiG1MmQ1wZikFE s7sYSog/poYleCeYW8kVzHNWnt9IuQWekIg6ZHkwp4NE/aW8HxvEwYRqCQIDAQAB AoGAE6rkiFmxbt06GHNwZQQ8QssP2Q2qARgjiGxzY38DWg6MYiNR8uUL6zQHDBIQ OQgpW9lpwD24D0tpsRnNOFVtMeafcxmykX+qHGtNeKJuTtqSm2eTI6gNbC8iosGT XJEPM8tc/dfZ2sDobLfi0alWFOzWo8vKaLnnAdMHoZ8mDo8CQQDCMx08JVlTW1zl
+4UTEnyyYmIezw5ORfMqPtN1LpQ4ptYnHNMVJPWcpRwBYZfHlPOPtuVwo6gzv82G QpgQsd4PAkEA0fA8e8R6JbeUR1HxsqWeCnPz3Ahq5Ya5WA6HyJQml9aDVqKDDp2L 3AcqsvFEKJ/T34r31so2yW6hj2yFBnzOZwJBAIqanrgJ1CpJYBGJJd6J6FQNIgjp MUWuaTJyqsvNFd8lPF2oFgPWYDKQKV/W/tRkvD2LhVCSjf95WsADkbMAsAMCQAHo wWQOwV2eccbERAJv5yQJMeqKWQ6FTyIx36I/VqqC1Obwy2hSnnb9ybGe6BPGgFLE HMTjSeRDEU0Qm5UXhXkCQQCPlZJqlgksBN/TULHC4RgsXIx+oFylBrkiFamYsuEt Kn52h41pX7FI5TXcqIDPw+uqAu50JnwDR0dLYY6fvIce
-----END RSA PRIVATE KEY-----
"""

ciphertext = base64.b64decode("fIVuuWFLVANs9MjatXbIbtH7/n0dBpDirXKi82jZovXS/krxy43cP0J9jlNz4dqxLgdiqtRe1AcymX06JUo1SrcqDEh3l QxoU1KUvV7jG9GE3pSxHq4dQlcWdHz95b9go6QYbe/5S/uJgolR+S9qaDE8tXYysP8FeXIPd0dXxHo=")

privKeyObj = RSA.import_key(binPrivKey)
cipher = PKCS1_OAEP.new(privKeyObj)
message = cipher.decrypt(ciphertext)

print("====Decrypted===")
print("Message:", message)
