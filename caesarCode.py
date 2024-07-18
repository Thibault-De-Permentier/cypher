from cypher import Cypher
class CaesarCode(Cypher):

    def crypt(textToCrypt,spacing):
        cryptedText = ''
        for char in textToCrypt:
            cryptedText = cryptedText + Cypher.allTheCharacter[ (Cypher.allTheCharacter.index(char) + spacing)%len(Cypher.allTheCharacter) ]  
        return cryptedText

    def decrypt(textToDecrypt,spacing):
        decryptedText = ''
        for char in textToDecrypt:
            decryptedText = decryptedText + Cypher.allTheCharacter[ (Cypher.allTheCharacter.index(char) - spacing)%len(Cypher.allTheCharacter) ]  
        return decryptedText