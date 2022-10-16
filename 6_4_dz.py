text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def transrorm_text(text):
    text = list(filter(lambda x: not'абв' in x, text.split()))
    return ' '.join(text)

print(transrorm_text(text))